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
    def __init__(self):
        # 邮件信息
        self.password = "tpymueebnzojchcf"
        self.from_email = ("jaydentang418@qq.com")
        self.to_email = "jaydentang418@qq.com"

        self.server = smtplib.SMTP("smtp.qq.com:587")
        self.server.starttls()
        self.server.login(self.from_email, self.password)

        # 模型信息
        self.model_fall = YOLO(f"{cu_path}/yolov8n_fall.pt")
        self.model_face = YOLO(f"{cu_path}/yolov8n_face.pt")

        # 可视化信息
        self.annotator = None

        # 时间信息
        self.time_total_start = 0
        self.time_total_end = 0
        self.time_cycle_start = 0
        self.time_cycle_end = 0

        # 帧数信息
        self.frame_count = 0

        # 人脸信息保存
        self.face_imwrite_step = 2
        self.face_imwrite_num = 0

        # 人物信息
        self.person = {}

        # 设备信息
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def send_email(self, warntype):
        message = MIMEMultipart()
        message["From"] = self.from_email
        message["To"] = self.to_email
        message["Subject"] = "警告！"

        # Add in the message body
        if warntype == "fall":
            message_body = "老人摔倒了！" + time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime()
            )
        elif warntype == "intrude":
            message_body = "有人闯入！"
        elif warntype == "test":
            message_body = "测试！" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        message.attach(MIMEText(message_body, "plain"))
        self.server.sendmail(self.from_email, self.to_email, message.as_string())
    
    def predict(self, im0):
        results = [self.model_fall(im0), self.model_face(im0)]
        return results

    def display_fps(self, im0):
        self.time_cycle_end = time.time()
        fps = 1 / np.round(self.time_cycle_end - self.time_cycle_start, 2)
        text = f"FPS: {int(fps)}"
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.0, 2)[0]
        gap = 10
        cv2.rectangle(im0, (20 - gap, 70 - text_size[1] - gap), (20 + text_size[0] + gap, 70 + gap), (255, 255, 255), -1)
        cv2.putText(im0, text, (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)

    def plot_bboxes(self, results, im0):
        class_ids = []

        boxes = []
        clss = []
        names = {0: "up", 1: "bending", 2:"down", 3: "face"}

        result_face = results[1]
        boxes_face = result_face[0].boxes.xyxy.cpu().tolist()
        clss_face = result_face[0].boxes.cls.cpu().tolist()

        # 读取目标人脸,检测人脸
        for box, cls in zip(boxes_face, clss_face):
            if int(cls) == 1:
                # 获得人脸信息,格式为BGR三维数组
                face = im0[int(box[1]) : int(box[3]), int(box[0]) : int(box[2])]
                
                # # 保存一些人脸图片
                # os.makedirs(f"{cu_path}/goals_pre", exist_ok=True)
                # if self.frame_count % self.face_imwrite_step == 0:
                #     self.face_imwrite_num += 1
                #     cv2.imwrite(f"{cu_path}/goals_pre/face_{self.frame_count}.jpg", face)
                
                # 将人脸信息与目标人脸进行比对
                facenet_model = FaceNet()
                face_img = Image.fromarray(np.uint8(face))
                for i in os.listdir(f"{cu_path}/goals"):
                    goal_face = Image.open(f"{cu_path}/goals/{i}")
                    probability = facenet_model.detect_image(goal_face, face_img)
                    if probability < 1.2:
                        names[3] = i[:-4]
                
                # 将人脸框信息写入boxes, clss中
                boxes.append(box)
                clss.append(3)

        self.annotator = Annotator(im0, 3, names)

        result_fall = results[0]
        boxes_fall = result_fall[0].boxes.xyxy.cpu()
        clss_fall = result_fall[0].boxes.cls.cpu().tolist()

        for box, cls in zip(boxes_fall, clss_fall):
            #class_ids.append(cls)
            boxes.append(box)
            clss.append(cls)
        
        for box, cls in zip(boxes, clss):
            self.annotator.box_label(box, label=names[int(cls)], color=colors(int(cls), True))
        
        return im0, class_ids
    
    def fall_detect(self):
        pass

    def __call__(self):
        # 从摄像头获取视频流
        cap = cv2.VideoCapture(1)
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

            # 判断是否有人摔倒,并发送报警信息
            self.fall_detect()

            # 显示FPS
            self.display_fps(im0)

            # 显示视频帧
            cv2.imshow("Fall Detection", im0)

            # 读取键盘输入,如果输入为q,则退出
            if cv2.waitKey(5) & 0xFF == ord("q"):
                break
        
        # 释放摄像头,关闭窗口,关闭邮件服务器
        cap.release()
        cv2.destroyAllWindows()
        self.server.quit()

detector = PredictStream()
detector()
