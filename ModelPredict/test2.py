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
        self.time_cycle_start = 0
        self.time_cycle_end = 0

        # device information
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

        # cycle number
        self.frame_count = 0
        self.face_imwrite_step = 2
        self.face_imwrite_num = 0

        self.person = {}
        self.capture_width = 640
        self.capture_height = 480
        self.max_distance_1d = np.linalg.norm(np.array([self.capture_width, self.capture_height]))
        self.right_distance_2d_ratio = 2
        self.person_cover = 10
        self.face_match = 1.2

    def predict(self, im0):
        results = [self.model_fall(im0), self.model_face(im0)]
        return results

    def display_fps(self, im0):
        self.time_cycle_end = time()
        fps = 1 / np.round(self.time_cycle_end - self.time_cycle_start, 2)
        text = f'FPS: {int(fps)}'
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.0, 2)[0]
        gap = 10
        cv2.rectangle(im0, (20-gap, 70-text_size[1]-gap), (20+text_size[0]+gap, 70+gap), (255, 255, 255), -1)
        cv2.putText(im0, text, (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)
    
    def imwrite_face(self, face):
        os.makedirs(f"{cu_path}/goals_pre", exist_ok=True)
        if self.frame_count % self.face_imwrite_step == 0:
            self.face_imwrite_num += 1
            cv2.imwrite(f"{cu_path}/goals_pre/face_{self.frame_count}.jpg", face)
                
    def update_person(self, boxes_face, clss_face, face ,box, names):
        # 初始化facenet模型
        facenet_model = FaceNet()

        # 转化为Image格式
        face = Image.fromarray(np.uint8(face))
        
        # 判断是否为目标人脸
        for i in os.listdir(f"{cu_path}/PredictData/goals"):
            goal_face = Image.open(f"{cu_path}/PredictData/goals/{i}")
            probability = facenet_model.detect_image(goal_face, face)
            if probability < self.face_match:
                names[3] = i[:-4]

                # 匹配人脸与人体,并将人体box写入人物信息
                person_info_pre = []
                for box_new, cls_new in zip(boxes_face, clss_face):
                    if (
                        cls_new == 0.0
                        and box[0] > box_new[0]
                        and box[1] > box_new[1]
                        and box[2] < box_new[2]
                        and box[3] < box_new[3]
                    ):
                        person_info_pre.append(box_new)
                
                if len(person_info_pre) == 1:
                    self.person[names[3]] = [(person_info_pre[0][0] + person_info_pre[0][2]) / 2, (person_info_pre[0][1] + person_info_pre[0][3]) / 2, self.frame_count]
                elif len(person_info_pre) > 1:
                    box_person_right = [[self.max_distance_1d], []]
                    point_face = [(box[0] + box[2]) / 2, (box[1] + box[3]) / 2]
                    for box_new in person_info_pre:
                        point_person = [(box_new[0] + box_new[2]) / 2, (box_new[1] + box_new[3]) / 2]
                        distance_1d = np.linalg.norm(np.array(point_face) - np.array(point_person))
                        if distance_1d < box_person_right[0]:
                            box_person_right[0] = distance_1d
                            box_person_right[1] = box_new
                    self.person[names[3]] = [point_person[0], point_person[1], self.frame_count]
                else:
                    pass

        return names
    
    def judge_distance(self, box):
        for name, info in self.person.items():
            point_person_ul = np.array(box[0:2])
            point_person_lr = np.array(box[2:4])
            point_person_c = np.array([(box[0] + box[2]) / 2, (box[1] + box[3]) / 2])
            point_person_c_last = np.array(info[0:2])
            distance_1d_p = np.linalg.norm(point_person_ul - point_person_lr)
            distance_1d_p2p = np.linalg.norm(point_person_c - point_person_c_last)
            distance_2d_ratio = distance_1d_p2p / distance_1d_p
            if distance_2d_ratio < self.right_distance_2d_ratio:
                self.person[name] = [point_person_c[0], point_person_c[1], self.frame_count]

    
    def plot_bboxes(self, results, im0):
        boxes = []
        clss = []
        names = {0: "up", 1: "bending", 2:"down", 3: "face"}

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
                names = self.update_person(boxes_face, clss_face, face, box, names)

                # 将人脸框信息写入boxes, clss中
                boxes.append(box)
                clss.append(3)

            elif cls == 0.0 and 1.0 not in clss_face:
                if self.person == {}:
                    pass
                else:
                    # 判断是否是同一个人,如果是,更新人物信息
                    self.judge_distance()
        
        self.annotator = Annotator(im0, 3, names)

        result_fall = results[0]
        boxes_fall = result_fall[0].boxes.xyxy.cpu().tolist()
        clss_fall = result_fall[0].boxes.cls.cpu().tolist()

        for box, cls in zip(boxes_fall, clss_fall):
            boxes.append(box)
            clss.append(cls)
        
        for box, cls in zip(boxes, clss):
            self.annotator.box_label(box, label=names[int(cls)], color=colors(int(cls), True))
        
        return im0

    def __call__(self):
        cap = cv2.VideoCapture(self.capture_index)
        assert cap.isOpened()
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        frame_count = 0
        while True:
            self.time_cycle_start = time()
            ret, im0 = cap.read()
            assert ret
            results = self.predict(im0)
            im0 = self.plot_bboxes(results, im0)
            for name, info in self.person.items():
                if info[2] - self.frame_count > self.person_cover:
                    self.person.pop(name)

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