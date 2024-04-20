from PIL import Image
from ultralytics import YOLO
from FaceIdentify.nets.facenet import FaceNet

class PredictImage:
    def __init__(self, testspath, goalspath="Data/goals"):
        self.modelspath = {
            "fall_detection": "ModelPredict/yolov8_fall.pt",
            "face_detection": "ModelPredict/yolov8_face.pt",
            "face_indentify": "ModelPredict/facenet_mobilenet.pth"
        }
        self.testspath = testspath
        self.goalspath = goalspath
    
    def set_testspath(self, testspath):
        self.testspath = testspath
    
    def set_goalspath(self, goalspath):
        self.goalspath = goalspath
    
    def predict_image(self):
        # 导入模型
        models = {
            "fall_detection": YOLO(self.modelspath["fall_detection"]),
            "face_detection": YOLO(self.modelspath["face_detection"]),
            "face_indentify": FaceNet()

        }

        # 预测
        results = {
            "fall_detection": model_fall_detection(self.testspath),
            "face_detection": model_face_detection(self.testspath),
            "face_indentify": model_face_indentify(self.testspath)
        }

        # 生成图片
        # for r in results:
        #     im_array_fall = r.plot()  # plot a BGR numpy array of predictions
        #     im_fall = Image.fromarray(im_array_fall[..., ::-1])  # RGB PIL image
        #     im_fall.show()

        return results
