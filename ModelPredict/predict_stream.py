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
from predict_facenet import FaceNet
from path import cu_path


class PredictStream:
    # 信息类
    class info:
        def __init__(self, name="name", posture="posture", box_face=[], box_fall=[], frame_while=-1, frame_last=-1, isFall=False, isSendEmail=False):
            self.name = name
            self.posture = posture
            self.box_face = box_face
            self.box_fall = box_fall
            self.frame_while = frame_while
            self.frame_last = frame_last
            self.isFall = isFall
            self.isSendEmail = isSendEmail

            self.posture_dir = ((0, "up"), (1, "bending"), (2, "down"))
            self.PostureJudge = 3 # 常量,姿态信息判断帧数
    
    def __init__(self):
        # 处理器信息
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        # 摄像头信息
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
        self.model_fall = YOLO(f"{cu_path}/PredictData/models/yolov8n_fall.pt")
        self.model_face = YOLO(f"{cu_path}/PredictData/models/yolov8n_face.pt")

        # 可视化信息
        self.annotator = None

        # 时间信息
        self.time_total_start = 0
        self.time_total_end = 0
        self.time_cycle_start = 0
        self.time_cycle_end = 0

        # 帧数信息
        self.frame_count = 0
        self.fps = -1

        # 人脸匹配值
        self.face_match = 1.2

        # 人脸信息保存
        self.face_imwrite_step = 2
        self.face_imwrite_num = 0

        # 人物信息,格式为[info1, info2, ...],其中info1为info类
        self.infos = []
        # 人物超出监控范围,等待{self.over}帧覆盖信息
        self.cover = self.fps * 5

        # 最大一维欧式距离信息
        self.max_distance_1d = np.linalg.norm(np.array([self.capture_width, self.capture_height]))
        
        # 判断两个点是否是同一个人的二维欧式距离比例(二维欧式距离: 一维欧式距离的平方)
        self.right_distance_2d_ratio = 0.4

    def send_email(self):
        message = MIMEMultipart()
        message["From"] = self.from_email
        message["To"] = self.to_email

        # 邮件主题
        message["Subject"] = "警告！"

        # 消息内容
        message_body = (
            "老人跌倒了！" 
            + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            )
       
        message.attach(MIMEText(message_body, "plain"))
        self.server.sendmail(self.from_email, self.to_email, message.as_string())
    
    def predict(self, im0):
        results = [self.model_fall(im0), self.model_face(im0)]
        return results

    def display_fps(self, im0):
        self.time_cycle_end = time.time()
        self.fps = 1 / np.round(self.time_cycle_end - self.time_cycle_start, 2)
        text = f'FPS: {int(self.fps)}'
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.0, 2)[0]
        gap = 10
        cv2.rectangle(im0, (20 - gap, 70 - text_size[1] - gap), (20 + text_size[0] + gap, 70 + gap), (255, 255, 255), -1)
        cv2.putText(im0, text, (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)

    def imwrite_face(self, face):
        os.makedirs(f"{cu_path}/goals_pre", exist_ok=True)
        if self.frame_count % self.face_imwrite_step == 0:
            self.face_imwrite_num += 1
            cv2.imwrite(f"{cu_path}/goals_pre/face_{self.frame_count}.jpg", face)
    
    def update_info_person(self, boxes_face, clss_face, face ,box, plot_names):
        # 初始化facenet模型
        facenet_model = FaceNet()

        # 转化为Image格式
        face = Image.fromarray(np.uint8(face))
        
        # 判断是否为目标人脸
        for i in os.listdir(f"{cu_path}/PredictData/goals"):
            goal_face = Image.open(f"{cu_path}/PredictData/goals/{i}")
            probability = facenet_model.detect_image(goal_face, face)
            if probability < self.face_match:
                plot_names[3] = i[:-4]

                # 匹配人脸与人体,并将人体box写入信息变量
                # 筛选1: 人脸在人体内
                person_box_pre = []
                for person_box, cls_new in zip(boxes_face, clss_face):
                    if (
                        cls_new == 0.0
                        and box[0] > person_box[0]
                        and box[1] > person_box[1]
                        and box[2] < person_box[2]
                        and box[3] < person_box[3]
                    ):
                        person_box_pre.append(person_box)
                
                # 筛选2: 人脸与所有人体中距离最近的人体
                if len(person_box_pre) == 1:
                    info = self.info(name=plot_names[3], box_face=box, frame_while=self.frame_count)
                    self.infos.append(info)
                elif len(person_box_pre) > 1:
                    person_box_right = [[self.max_distance_1d], []]
                    point_face = [(box[0] + box[2]) / 2, (box[1] + box[3]) / 2]
                    for person_box in person_box_pre:
                        point_person = [(person_box[0] + person_box[2]) / 2, (person_box[1] + person_box[3]) / 2]
                        distance_1d = np.linalg.norm(np.array(point_face) - np.array(point_person))
                        if distance_1d < person_box_right[0]:
                            person_box_right[0] = distance_1d
                            person_box_right[1] = person_box
                    info = self.info(name=plot_names[3], box_face=person_box_right[1][0:4], frame_while=self.frame_count)
                else:
                    pass

        return plot_names
    
    def judge_distance_2d(self, box_cu1, box_cu2, box_base):
        box_cu1_center = np.array([(box_cu1[0] + box_cu1[2]) / 2, (box_cu1[1] + box_cu1[3]) / 2])
        box_cu2_center = np.array([(box_cu2[0] + box_cu2[2]) / 2, (box_cu2[1] + box_cu2[3]) / 2])
        distance_2d_cu = np.linalg.norm(box_cu1_center - box_cu2_center) ** 2
        distance_2d_base = np.linalg.norm(np.array(box_base[0:2]) - np.array(box_base[2:4])) ** 2
        distance_2d_ratio = distance_2d_cu / distance_2d_base
        if distance_2d_ratio < self.right_distance_2d_ratio:
            return True
        else:
            return False
    
    def plot_bboxes(self, results, im0):
        plot_boxes = []
        plot_clss = []
        plot_names = {0: "up", 1: "bending", 2:"down", 3: "face"}

        result_face = results[1]
        boxes_face = result_face[0].boxes.xyxy.cpu().tolist()
        clss_face = result_face[0].boxes.cls.cpu().tolist()

        # 读取目标人脸,检测人脸
        for box, cls in zip(boxes_face, clss_face):
            if cls == 1.0:
                # 获得人脸信息,格式为BGR三维数组
                face = im0[int(box[1]) : int(box[3]), int(box[0]) : int(box[2])]
                
                # # 保存一些人脸图片
                # self.imwrite_face(face)

                # 将人脸信息与目标人脸进行比对,并写入人物信息
                plot_names = self.update_info_person(boxes_face, clss_face, face, box, plot_names)

                # 将人脸框信息写入boxes, clss中
                plot_boxes.append(box)
                plot_clss.append(3)
            
            elif cls == 0.0 and 1.0 not in clss_face:
                if self.infos == {}:
                    pass
                else:
                    # 判断是否是同一个人,如果是,更新人物信息
                    for i in range(len(self.infos)):
                        isRight = self.judge_distance_2d(box, self.infos[i].box_face, self.infos[i].box_face)
                        if isRight:
                            self.infos[i].box_face = box
                            self.infos[i].frame_while = self.frame_count
                            break

        self.annotator = Annotator(im0, 3, plot_names)

        result_fall = results[0]
        boxes_fall = result_fall[0].boxes.xyxy.cpu().tolist()
        clss_fall = result_fall[0].boxes.cls.cpu().tolist()

        for box, cls in zip(boxes_fall, clss_fall):
            plot_boxes.append(box)
            plot_clss.append(cls)
        
        for box, cls in zip(plot_boxes, plot_clss):
            self.annotator.box_label(box, label=plot_names[int(cls)], color=colors(int(cls), True))
        
        return im0
    
    def update_info_postures(self, results):
        boxes = results.boxes.xyxy.cpu().tolist()
        clss = results.boxes.cls.cpu().tolist()

        # 更新姿态信息
        for box, cls in zip(boxes, clss):
            # 如果有此姿态,直接更新
            isUpdata = False
            for i in range(len(self.infos)):
                isRight = self.judge_distance_2d(box, self.infos[i].box_fall, self.infos[i].box_fall)
                if isRight:
                    if self.infos[i].posture == self.postures_dir[cls]:
                        self.infos[i].frame_last += 1
                    else:
                        if self.infos[i].frame_last > self.posture_judge:
                            if self.infos[i].posture == "up" and cls == 2.0:
                                self.infos[i].isFall = True
                            else:
                                self.infos[i].isFall = False
                        self.infos[i].posture = self.postures_dir[cls]
                        self.infos[i].frame_last = 1
                    self.infos[i].box_fall = box
                    self.infos[i].frame_while = self.frame_count
                    isUpdata = True
        
            # 如果没有此姿态
            if not isUpdata:
                self.postures.append([box, self.postures_dir[cls], self.frame_count, 1, False, False])

    def fall_detect(self, results):
        # 更新姿态信息
        self.update_info_postures(results[1])
        
        # 判断是否有人跌倒
        for i in range(len(self.postures)):
            if not self.infos[i].isSendEmail and self.infos[i].isFall and self.infos[i].frame_last > self.posture_judge:
                self.infos[i].isSendEmail = True
                self.send_email()

    def clean(self):
        for info in self.infos:
            if self.frame_count - info.frame_while > self.cover:
                self.infos.remove(info)

    def __call__(self):
        # 从摄像头获取视频流
        cap = cv2.VideoCapture(self.capture_index)
        assert cap.isOpened()

        # 设置摄像头参数
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        while True:
            # 记录系统运行开始时间
            self.time_cycle_start = time.time()

            # 读取视频帧,返回ret(布尔值,表示帧是否被成功读取)和im0(BGR三维数组,视频帧本身)
            ret, im0 = cap.read()
            assert ret

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

            # 显示视频帧
            cv2.imshow("Fall Detection System", im0)

            # 读取键盘输入,如果输入为q,则退出
            if cv2.waitKey(5) & 0xFF == ord("q"):
                break
        
        # 释放摄像头,关闭窗口,关闭邮件服务器
        cap.release()
        cv2.destroyAllWindows()
        self.server.quit()

detector = PredictStream()
detector()
