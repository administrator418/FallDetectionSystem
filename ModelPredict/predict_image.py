import os
from PIL import Image
from ultralytics import YOLO
from FaceIdentify.nets.facenet import facenet_image

class PredictImageOVideo:
    def __init__(
            self,
            testspath,
            goalspath="Data/goals"
        ):

        self.testspath = testspath
        self.goalspath = goalspath
        
        self.ImageOVideo = None
        self.right_distance_2d_ratio = 0.05
    
    def set_testspath(self, testspath):
        self.testspath = testspath
    
    def set_goalspath(self, goalspath):
        self.goalspath = goalspath

    def set_ImageOVideo(self):
        if self.testspath.endswith(".jpg") or self.testspath.endswith(".png"):
            self.ImageOVideo = "Image"
        elif self.testspath.endswith(".mp4") or self.testspath.endswith(".avi"):
            self.ImageOVideo = "Video"
    
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
        model = facenet_image()

        test = Image.open(self.testspath)

        for goal in os.listdir(self.goalspath):
            goal = Image.open(f"{self.goalspath}/{goal}")
            if model.detect_image(goal, test):
                pass
                # 识别成功，返回一些值，使其可以输出到gui界面


