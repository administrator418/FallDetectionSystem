import torch
import numpy as np
import cv2
import os
from time import time
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from path import cu_path
from PIL import Image
from predict_facenet import FaceNet

class ObjectDetection:
    def __init__(self, capture_index):
        # default parameters
        self.capture_index = capture_index
        self.email_sent = False

        # model information
        self.model_fall = YOLO(f"{cu_path}/yolov8n_fall.pt")
        self.model_face = YOLO(f"{cu_path}/yolov8n_face.pt")

        # visual information
        self.annotator = None
        self.start_time = 0
        self.end_time = 0

        # device information
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

        # cycle number
        self.cycle_num = 0
        self.face_imwrite_step = 2
        self.face_imwrite_num = 0

    def predict(self, im0):
        results = [self.model_fall(im0), self.model_face(im0)]
        return results

    def display_fps(self, im0):
        self.end_time = time()
        fps = 1 / np.round(self.end_time - self.start_time, 2)
        text = f'FPS: {int(fps)}'
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
                # if self.cycle_num % self.face_imwrite_step == 0:
                #     self.face_imwrite_num += 1
                #     cv2.imwrite(f"{cu_path}/goals_pre/face_{self.cycle_num}.jpg", face)
                
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

    def __call__(self):
        cap = cv2.VideoCapture(self.capture_index)
        assert cap.isOpened()
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        frame_count = 0
        while True:
            self.start_time = time()
            ret, im0 = cap.read()
            assert ret
            results = self.predict(im0)
            im0, class_ids_total = self.plot_bboxes(results, im0)

            for class_ids in class_ids_total:
                if len(class_ids) > 0:
                    if not self.email_sent:
                        # send_email(to_email, from_email, len(class_ids))
                        self.email_sent = True
                else:
                    self.email_sent = False

            self.display_fps(im0)
            cv2.imshow('YOLOv8 Detection', im0)
            frame_count += 1
            if cv2.waitKey(5) & 0xFF == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
        # server.quit()

od = ObjectDetection(capture_index=0)
od()