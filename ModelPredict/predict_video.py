import cv2
from ultralytics import YOLO

class PredictVideo:
    def __init__(self, modelpath, filepath):
        self.modelpath = modelpath
        self.filepath = filepath
    
    def predict_video(self):
        # 导入模型
        model = YOLO(self.modelpath)

        # 打开视频文件
        cap = cv2.VideoCapture(self.filepath)

        # 循环遍历视频帧
        while cap.isOpened():
            # 从视频中读取一帧
            success, frame = cap.read()

            # 如果成功读取帧
            if success:
                # 在帧上运行 YOLOv8 推理
                results = model(frame)

                # 在帧上可视化结果
                annotated_frame = results[0].plot()
                clss = results[0].boxes.cls.cpu().tolist()

                # 显示帧
                cv2.imshow("Fall Detection", annotated_frame)

                # 如果按 'q' 键则退出循环
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                break
        
        # 释放视频捕获对象并关闭显示窗口
        cap.release()
        cv2.destroyAllWindows()
