def predict_image(filepath):
    from PIL import Image
    from ultralytics import YOLO

    # 导入模型
    model_fall = YOLO("yolov8n_fall2.pt")
    model_face = YOLO("yolov8n_face.pt")

    # 预测
    results_fall = model_fall(filepath)
    results_face = model_face(filepath)

    # 生成图片
    for r in results_fall:
        im_array_fall = r.plot()  # plot a BGR numpy array of predictions
        im_fall = Image.fromarray(im_array_fall[..., ::-1])  # RGB PIL image
        im_fall.show()

    for r in results_face:
        im_array_face = r.plot()
        im_face = Image.fromarray(im_array_face[..., ::-1])
        im_face.show()
