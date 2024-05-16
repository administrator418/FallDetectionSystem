import torch
import numpy as np
import cv2
import time
import os
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image
from FaceIdentify.nets.facenet import facenet_image
from Settings.json_settings import Settings
from MedicalInformation.MedicalInformation import get_medical_informations


class Predict:
    # 人物信息类
    class Info:
        def __init__(
                self, name="name",
                posture="posture",
                box_faceDetection=[],
                box_postureDetection=[],
                frame_while=-1,
                frame_last=-1,
                fall={
                    "last_up_frame": None,
                    "last_down_frame": None,
                    "isFall": False
                },
                isAlarm=False
            ):
            self.name = name
            self.posture = posture
            self.box_faceDetection = box_faceDetection
            self.box_postureDetection = box_postureDetection
            self.frame_while = frame_while
            self.frame_last = frame_last
            self.fall = fall
            self.isAlarm = isAlarm

    # 人物人脸信息类
    class InfoFaceNBody:
        def __init__(self, name="name", box_face=[], box_body=[]):
            self.name = name
            self.box_face = box_face
            self.box_body = box_body

    def __init__(self):
        # 处理器信息
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        # 摄像头信息
        self.cap = None
        self.capture_index = 0
        self.capture_width = 640
        self.capture_height = 480

        # 邮件信息
        self.password = "tpymueebnzojchcf"
        self.from_email = ("jaydentang418@qq.com")
        self.to_email = "jaydentang418@qq.com"

        self.server = smtplib.SMTP("smtp.qq.com:587")
        self.server.starttls()
        self.server.login(self.from_email, self.password)

        # 模型信息
        self.model_fall = YOLO("ModelPredict/yolov8n_fall.pt")
        self.model_face = YOLO("ModelPredict/yolov8n_face.pt")

        # 可视化信息
        self.annotator = None

        # 时间信息
        self.time_total_start = 0
        self.time_total_end = 0
        self.time_cycle_start = 0
        self.time_cycle_end = 0
        self.JudgeFall = 3 # 常量,判断跌倒信息帧数

        # 帧数信息
        self.frame_count = 0
        self.fps = -1

        # 人脸信息保存
        self.face_imwrite_step = 2
        self.face_imwrite_num = 0

        # 人物信息,格式为[info1, info2, ...],其中info1为info类
        self.infos = []

        # 人物信息,姿态
        self.postures_dir = ((0, "up"), (1, "bending"), (2, "down"))
        self.PostureJudge = 3 # 常量,姿态信息判断帧数

        # 人物超出监控范围,等待{self.over}帧覆盖信息
        self.cover = 20
        self.CoverXFps = 10

        # 最大一维欧式距离信息
        self.distance_1d_max = np.linalg.norm(np.array([self.capture_width, self.capture_height]))

        # 判断两个点是否是同一个人的二维欧式距离比例(二维欧式距离: 一维欧式距离的平方)
        self.right_distance_2d_ratio = 0.05

        # 测试模式文件类型
        self.file_type = "stream"

        # 导入外部设置
        settings = Settings()
        self.settings = settings.items

    def send_email(self, i):
        message = MIMEMultipart()
        message["From"] = self.from_email
        message["To"] = self.to_email

        # 邮件主题
        message["Subject"] = "警告！"

        # 查找医疗信息
        medical_informations = get_medical_informations()
        medical_information = None
        for info in medical_informations:
            if info.name == self.infos[i].name:
                medical_information = info
                break

        # 消息内容
        if self.infos[i].name != "name":
            message_body = (
                f"{self.infos[i].name}跌倒了!\n"
                + "医疗信息卡:\n"
                + "\t姓名: " + medical_information.name + "\n"
                + "\t出生日期: " + medical_information.brithday + "\n"
                + "\t血型: " + medical_information.blood_type + "\n"
                + "\t紧急联系人: " + medical_information.phone_number + "\n"
                + "\t健康状况: " + medical_information.health_conditions + "\n"
                + "\t过敏信息: " + medical_information.allergy_information + "\n"
                + "\t当前用药: " + medical_information.current_medications + "\n"
                + "\t手术史或重大医疗事件: " + medical_information.history_surgeries_N_medical_events + "\n"
                + "时间: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                )
        else:
            message_body = (
                f"有人跌倒了!\n"
                + "时间: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                )

        message.attach(MIMEText(message_body, "plain"))
        self.server.sendmail(self.from_email, self.to_email, message.as_string())

    def predict(self, im0):
        results = {"results_fall": self.model_fall(im0), "results_face": self.model_face(im0)}
        return results

    def display_fps(self, im0):
        self.time_cycle_end = time.time()
        self.fps = 1 / np.round(self.time_cycle_end - self.time_cycle_start, 2)
        self.cover = self.fps * self.CoverXFps
        text = f'FPS: {int(self.fps)}'
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.0, 2)[0]
        gap = 10
        cv2.rectangle(im0, (20 - gap, 70 - text_size[1] - gap), (20 + text_size[0] + gap, 70 + gap), (255, 255, 255), -1)
        cv2.putText(im0, text, (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)

    def imwrite_face(self, face):
        os.makedirs("Data/goals_pre", exist_ok=True)
        if self.frame_count % self.face_imwrite_step == 0:
            self.face_imwrite_num += 1
            cv2.imwrite(f"Data/goals_pre/face_{self.frame_count}.jpg", face)

    def update_info_face(self, info_faces, plot_names):
        # 判断是否为目标人脸
        for face in info_faces:
            # 与人物信息库匹配,如果匹配成功,更新信息
            isUpdate = False
            for j in range(len(self.infos)):
                box_base = self.infos[j].box_faceDetection
                if box_base == [] and self.infos[j].box_postureDetection != []:
                    box_base = self.infos[j].box_postureDetection
                if self.judge_distance_2d_byBox(face.box_body, box_base):
                    self.infos[j].name = face.name
                    self.infos[j].box_faceDetection = face.box_body
                    self.infos[j].frame_while = self.frame_count
                    isUpdate = True
                    break

            # 如果没有匹配成功,添加信息
            if not isUpdate:
                self.infos.append(self.Info(name=face.name, box_faceDetection=face.box_body, frame_while=self.frame_count))

        return plot_names

    def update_info_postures(self, results):
        results_fall = results["results_fall"]
        boxes = results_fall[0].boxes.xyxy.cpu().tolist()
        clss = results_fall[0].boxes.cls.cpu().tolist()

        # 更新姿态信息
        for box, cls in zip(boxes, clss):
            cls = int(cls)

            # 如果有此姿态,直接更新
            isUpdata = False
            for i in range(len(self.infos)):
                box_base = self.infos[i].box_postureDetection
                if box_base == [] and self.infos[i].box_faceDetection != []:
                    box_base = self.infos[i].box_faceDetection
                isRight = self.judge_distance_2d_byBox(box, box_base)
                if isRight:
                    if self.infos[i].posture == self.postures_dir[cls][1]:
                        self.infos[i].frame_last += 1
                    else:
                        if self.infos[i].frame_last > self.PostureJudge:
                            if self.infos[i].posture == "up" and cls == 2.0:
                                self.infos[i].fall["isFall"] = True
                            elif (
                                self.infos[i].fall["last_up_frame"]
                                and self.infos[i].fall["last_down_frame"]
                                and self.infos[i].fall["last_up_frame"] < self.infos[i].fall["last_down_frame"]
                                and self.infos[i].fall["last_down_frame"] - self.infos[i].fall["last_up_frame"] < self.JudgeFall
                            ):
                                self.infos[i].fall["isFall"] = True
                            else:
                                self.infos[i].fall["isFall"] = False
                        self.infos[i].posture = self.postures_dir[cls][1]
                        self.infos[i].frame_last = 1
                    self.infos[i].box_postureDetection = box
                    self.infos[i].frame_while = self.frame_count
                    isUpdata = True

            # 如果没有此姿态
            if not isUpdata:
                self.infos.append(self.Info(posture=self.postures_dir[cls][1], box_postureDetection=box, frame_while=self.frame_count, frame_last=1))

    def return_distance_1d(self, box_1, box_2):
        point_1 = np.array([(box_1[0] + box_1[2]) / 2, (box_1[1] + box_1[3]) / 2])
        point_2 = np.array([(box_2[0] + box_2[2]) / 2, (box_2[1] + box_2[3]) / 2])
        return np.linalg.norm(point_1 - point_2)

    def judge_distance_2d_byDistance(self, distance_1d, box_base):
        distance_2d_cu = distance_1d ** 2
        distance_2d_base = np.linalg.norm(np.array(box_base[0:2]) - np.array(box_base[2:4])) ** 2
        distance_2d_ratio = distance_2d_cu / distance_2d_base
        # print(f"distance_2d_ratio: {distance_2d_ratio}")
        if distance_2d_ratio < self.right_distance_2d_ratio:
            return True
        else:
            return False

    def judge_distance_2d_byBox(self, box_cu, box_base):
        if box_cu == [] or box_base == []:
            return False
        box_cu_center = np.array([(box_cu[0] + box_cu[2]) / 2, (box_cu[1] + box_cu[3]) / 2])
        box_base_center = np.array([(box_base[0] + box_base[2]) / 2, (box_base[1] + box_base[3]) / 2])
        distance_2d_cu = np.linalg.norm(box_cu_center - box_base_center) ** 2
        distance_2d_base = np.linalg.norm(np.array(box_base[0:2]) - np.array(box_base[2:4])) ** 2
        distance_2d_ratio = distance_2d_cu / distance_2d_base
        # print(f"distance_2d_ratio: {distance_2d_ratio}")
        if distance_2d_ratio < self.right_distance_2d_ratio:
            return True
        else:
            return False

    def plot_bboxes(self, results, im0):
        plot_boxes = []
        plot_clss = []
        plot_names = {0: "up", 1: "bending", 2:"down"}

        results_face = results["results_face"]
        boxes_face = results_face[0].boxes.xyxy.cpu().tolist()
        clss_face = results_face[0].boxes.cls.cpu().tolist()

        # 初始化facenet模型
        facenet_model = facenet_image()

        # 读取目标人脸,检测人脸
        info_faces = []
        info_faces_face = []
        info_faces_body = []

        face_id = 3
        for box, cls in zip(boxes_face, clss_face):
            if cls == 1.0:
                # 获得人脸信息,格式为BGR三维数组
                face = im0[int(box[1]) : int(box[3]), int(box[0]) : int(box[2])]
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                face = cv2.resize(face, self.settings["face_resolutions"])
                # 保存一些人脸图片
                if self.settings["save_face_image"]:
                    self.imwrite_face(face)
                face = Image.fromarray(np.uint8(face))

                # 与目标人脸库匹配,写入plot_names
                isAddFaces = False
                for i in os.listdir("Data/goals"):
                    goal_face = Image.open(f"Data/goals/{i}")
                    probability = facenet_model.detect_image(goal_face, face)
                    if probability == True:
                        plot_names[face_id] = i[:-4]
                        isAddFaces = True
                        break
                if not isAddFaces:
                    plot_names[face_id] = "face"

                # 将人脸框信息写入plot_boxes, plot_clss
                plot_boxes.append(box)
                plot_clss.append(face_id)

                # 写入info_faces
                info_faces_face.append(self.InfoFaceNBody(name=plot_names[face_id], box_face=box))

                face_id += 1

            elif cls == 0.0:
                # 写入info_faces
                info_faces_body.append(self.InfoFaceNBody(box_body=box))

        # 匹配人脸与人物信息
        for if_face in info_faces_face:
            for if_body in info_faces_body:
                distance_1d = self.return_distance_1d(if_face.box_face, if_body.box_body)
                if self.judge_distance_2d_byDistance(distance_1d, if_body.box_body):
                    info_faces.append(self.InfoFaceNBody(name=if_face.name, box_face=if_face.box_face, box_body=if_body.box_body))
                    break

        # 更新人物信息
        plot_names = self.update_info_face(info_faces, plot_names)

        self.annotator = Annotator(im0, 3, plot_names)

        results_fall = results["results_fall"]
        boxes_fall = results_fall[0].boxes.xyxy.cpu().tolist()
        clss_fall = results_fall[0].boxes.cls.cpu().tolist()

        for box, cls in zip(boxes_fall, clss_fall):
            plot_boxes.append(box)
            plot_clss.append(cls)

        for box, cls in zip(plot_boxes, plot_clss):
            self.annotator.box_label(box, label=plot_names[int(cls)], color=colors(int(cls), True))

        return im0

    def fall_detect(self, results):
        # 更新姿态信息
        self.update_info_postures(results)

        # 判断是否有人跌倒
        for i in range(len(self.infos)):
            if not self.infos[i].isAlarm and self.infos[i].fall["isFall"]:
                self.infos[i].isAlarm = True
                self.send_email(i)

    def clean(self):
        for info in self.infos:
            if self.frame_count - info.frame_while > self.cover:
                self.infos.remove(info)

    def print_infos(self):
        if self.infos == []:
            print("No person!")
        else:
            print(f"len(infos): {len(self.infos)}")
            for info in self.infos:
                print(
                    f"name: {info.name}, "
                    f"posture: {info.posture}, "
                    f"box_faceDetection: {info.box_faceDetection}, "
                    f"box_postureDetection: {info.box_postureDetection}, "
                    f"frame_while: {info.frame_while}, "
                    f"frame_last: {info.frame_last}, "
                    f"fall: {info.fall}, "
                    f"isAlarm: {info.isAlarm}"
                )

    def return_im0(self, file_type="stream", test=None):
        self.file_type = file_type
        # 从摄像头获取视频流
        if file_type == "stream":
            self.cap = cv2.VideoCapture(self.capture_index)
            assert self.cap.isOpened()

            # 设置摄像头参数
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.settings["cap_resolutions"][0])
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.settings["cap_resolutions"][1])
        
            # 读取视频帧,返回ret(布尔值,表示帧是否被成功读取)和im0(BGR三维数组,视频帧本身)
            ret, im0 = self.cap.read()
            assert ret

        # 读取图片
        elif file_type == "image":
            im0 = cv2.imread(test)
            assert im0 is not None

        # 读取视频中的帧
        elif file_type == "video":
            im0 = test
            
        # 转化为RGB格式
        im0 = cv2.cvtColor(im0, cv2.COLOR_BGR2RGB)
        
        # 记录系统运行开始时间
        self.time_cycle_start = time.time()

        # 记录帧数
        self.frame_count += 1

        # 预测
        results = self.predict(im0)

        # 画框
        im0 = self.plot_bboxes(results, im0)

        # 判断是否有人跌倒,并发送报警信息
        self.fall_detect(results)

        # 清理过期信息
        self.clean()

        # 显示FPS
        self.display_fps(im0)

        # 返回视频帧
        return im0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):   
        if self.file_type == "stream":
            self.cap.release()
        
        # 关闭邮件服务器
        self.server.quit()
        print("Exit!")
