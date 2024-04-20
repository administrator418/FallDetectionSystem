import os
from PIL import Image
from ultralytics import YOLO
from FaceIdentify.nets.facenet import facenet

class PredictImage:
    def __init__(
            self,
            testspath, goalspath="Data/goals",
            model_face_detection=False,
            model_fall_detection=False,
            model_face_indentify=False,
            goals_path="Data/goals"
        ):
        self.modelspath = {
            "fall_detection": "ModelPredict/yolov8_fall.pt",
            "face_detection": "ModelPredict/yolov8_face.pt",
            "face_indentify": "ModelPredict/facenet_mobilenet.pth"
        }
        self.testspath = testspath
        self.goalspath = goalspath
        self.model_face_detection = model_face_detection
        self.model_fall_detection = model_fall_detection
        self.model_face_indentify = model_face_indentify
        self.goals_path = goals_path

        self.right_distance_2d_ratio = 0.05
    
    def set_testspath(self, testspath):
        self.testspath = testspath
    
    def set_goalspath(self, goalspath):
        self.goalspath = goalspath
    
    def image_detection_predict(self, model_type):
        # 导入模型
        # model_type = "face_detection" or "posture_detection"
        model = YOLO(self.modelspath[model_type])

        # 预测
        results = model(self.testspath)

        # 生成图片
        # for r in results:
        #     im_array_fall = r.plot()  # plot a BGR numpy array of predictions
        #     im_fall = Image.fromarray(im_array_fall[..., ::-1])  # RGB PIL image
        #     im_fall.show()

        return results
    
    def image_identify_predict(self):
        model = facenet()

        test = Image.open(self.testspath)

        for goal in os.listdir(self.goalspath):
            goal = Image.open(f"{self.goalspath}/{goal}")
            if model.detect_image(goal, test):
                pass
                # 识别成功，返回一些值，使其可以输出到gui界面


