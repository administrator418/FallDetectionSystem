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

        # 循环次数
        self.cycle_num = 0

        # 人脸信息保存间隔
        self,face_imwrite_step = 2

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
        cv2.rectangle(
            im0,
            (20 - gap, 70 - text_size[1] - gap),
            (20 + text_size[0] + gap, 70 + gap),
            (255, 255, 255),
            -1,
        )
        cv2.putText(im0, text, (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)

    def plot_bboxes(self, results_fall, results_face, im0):
        class_ids = []
        self.annotator = Annotator(im0, 3, results_face[0].names)
        boxes = results_face[0].boxes.xyxy.cpu()
        clss = results_face[0].boxes.cls.cpu().tolist()
        names = results_face[0].names
        face_imwrite_step = 2
        os.makedirs("./ModelPredict/TestData/temp_face_images", exist_ok=True)
        for box, cls in zip(boxes, clss):
            flag = [-1, {0: 'Person', 1: 'jayden'}]
            # if int(cls) == 1:
            #     self.face_cycle_num += 1
            #     box_list = box.tolist()
            #     face = im0[int(box_list[1]) : int(box_list[3]), int(box_list[0]) : int(box_list[2])]
            #     if self.face_cycle_num % face_imwrite_step == 0:
            #         print(f"Writing face_{self.face_cycle_num}.jpg")
            #         cv2.imwrite(f"./ModelPredict/TestData/temp_face_images/face_{self.face_cycle_num}.jpg", face)
            #     face_img = Image.fromarray(np.uint8(face))
            #     goal_face = Image.open("./ModelPredict/TestData/images/goal.jpg")
            #     facenet_model = FaceNet()
            #     probability = facenet_model.detect_image(goal_face, face_img)
            #     if probability < 1.2:
            #         flag[0] = 1
            
            class_ids.append(cls)
            self.annotator.box_label(
                box, label=names[int(cls)] if flag[0] == -1 else flag[1][int(cls)], color=colors(int(cls), True)
            )


        return im0, class_ids

    def fall_time(self):
        return

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

            # 预测
            results_fall, results_face = self.predict(im0)

            # 画框
            im0 = self.plot_bboxes(results_fall, results_face, im0)

            # if 1 in class_ids:  # Only send email If not sent before
            #     if not self.flag['fall_notify']:
            #         if self.flag['fall_time'] == -1:
            #             self.flag['fall_time'] = time.time()
            #         elif time.time() - self.flag['fall_time'] > 10:
            #             send_email(to_email, from_email, 'fall')
            #             self.flag['fall_notify'] = True
            #         elif not self.flag['test']:
            #             send_email(to_email, from_email, 'test')
            #             self.flag['test'] = True
            # #else:

            self.display_fps(im0)
            cv2.imshow("Fall Detection", im0)
            frame_count += 1
            if cv2.waitKey(5) & 0xFF == ord("q"):
                break
        cap.release()
        cv2.destroyAllWindows()
        self.server.quit()


detector = PredictStream()
detector()
