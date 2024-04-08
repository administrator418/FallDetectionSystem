import torch
import numpy as np
import cv2
from time import time
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from path import cu_path

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
        class_ids_total = []
        for result in results:
            class_ids = []
            self.annotator = Annotator(im0, 3, result[0].names)
            boxes = result[0].boxes.xyxy.cpu()
            clss = result[0].boxes.cls.cpu().tolist()
            names = result[0].names
            for box, cls in zip(boxes, clss):
                class_ids.append(cls)
                self.annotator.box_label(box, label=names[int(cls)], color=colors(int(cls), True))
            class_ids_total.append(class_ids)
        return im0, class_ids_total

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

od = ObjectDetection(0)
od()