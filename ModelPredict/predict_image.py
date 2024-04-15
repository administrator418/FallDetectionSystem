from PIL import Image
from ultralytics import YOLO

class PredictImage:
    def __init__(self, modelpath, filepath):
        self.modelpath = modelpath
        self.filepath = filepath
    
    def predict_image(self):
        # 导入模型
        model = YOLO(self.modelpath)

        # 预测
        results = model(self.filepath)

        # 生成图片
        # for r in results:
        #     im_array_fall = r.plot()  # plot a BGR numpy array of predictions
        #     im_fall = Image.fromarray(im_array_fall[..., ::-1])  # RGB PIL image
        #     im_fall.show()

        return results
