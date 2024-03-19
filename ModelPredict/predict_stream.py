import torch
import numpy as np
import cv2
import time
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password = "tpymueebnzojchcf"
from_email = "jaydentang895@qq.com"  # must match the email used to generate the password
to_email = "jaydentang895@qq.com"  # receiver email

server = smtplib.SMTP('smtp.qq.com:587')
server.starttls()
server.login(from_email, password)

def send_email(to_email, from_email, warntype):
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = "警告！"
    
    # Add in the message body
    if warntype == 'fall':
        message_body = '老人摔倒了！' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    elif warntype == 'intrude':
        message_body = '有人闯入！'
    elif warntype == 'test':
        message_body = '测试！' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    message.attach(MIMEText(message_body, 'plain'))
    server.sendmail(from_email, to_email, message.as_string())

class ObjectDetection:
    def __init__(self, capture_index):
        # default parameters
        self.capture_index = capture_index

        # flag information
        self.flag = {
            'fall': False,
        }

        # model information
        self.model = YOLO("./ModelPredict/yolov8n_fall2.pt")

        # visual information
        self.annotator = None

        # time information
        self.start_time_total = 0
        self.end_time_total = 0
        self.start_time_cycle = 0
        self.end_time_cycle = 0
        self.start_time_fall = 0
        self.end_time_fall = 0

        # device information
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

    def predict(self, im0):
        results = self.model(im0)
        return results

    def display_fps(self, im0):
        self.end_time_cycle = time.time()
        fps = 1 / np.round(self.end_time_cycle - self.start_time_cycle, 2)
        text = f'FPS: {int(fps)}'
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.0, 2)[0]
        gap = 10
        cv2.rectangle(im0, (20 - gap, 70 - text_size[1] - gap), (20 + text_size[0] + gap, 70 + gap), (255, 255, 255), -1)
        cv2.putText(im0, text, (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)

    def plot_bboxes(self, results, im0):
        class_ids = []
        self.annotator = Annotator(im0, 3, results[0].names)
        boxes = results[0].boxes.xyxy.cpu()
        clss = results[0].boxes.cls.cpu().tolist()
        names = results[0].names
        for box, cls in zip(boxes, clss):
            class_ids.append(cls)
            self.annotator.box_label(box, label=names[int(cls)], color=colors(int(cls), True))
        return im0, class_ids
    
    def fall_time(self):
        return

    def __call__(self):
        cap = cv2.VideoCapture(self.capture_index)
        assert cap.isOpened()
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        frame_count = 0
        while True:
            self.start_time_cycle = time.time()
            ret, im0 = cap.read()
            assert ret
            results = self.predict(im0)
            im0, class_ids = self.plot_bboxes(results, im0)

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
            cv2.imshow('Fall Detection', im0)
            frame_count += 1
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        server.quit()

detector = ObjectDetection(capture_index=1)
detector()