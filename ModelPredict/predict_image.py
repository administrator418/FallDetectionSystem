from PIL import Image
from ultralytics import YOLO

# Load model
model = YOLO('./ModelPredict/yolov8n_fall.pt')

# Run inference
results = model('./ModelPredict/TestData/images/fall(1).jpg')  # results list

# Show the results
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('./ModelPredict/results.jpg')  # save image