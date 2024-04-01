import os
from PIL import Image

from predict_facenet import FaceNet

if __name__ == "__main__":
    model = FaceNet()
    
    goal_data = "./ModelPredict/TestData/images/goal.jpg"
    test_data = "/ModelPredict/TestData/temp_face_images"

    probability_max = -1
    probability_max_image = -1

    for i in os.listdir("." + test_data):
        image_1 = os.getcwd() + test_data + "/" + i
        try:
            image_1 = Image.open(image_1)
        except:
            print('Image_1 Open Error! Try again!')
            continue

        image_2 = goal_data
        try:
            image_2 = Image.open(image_2)
        except:
            print('Image_2 Open Error! Try again!')
            continue
        
        probability = model.detect_image(image_1,image_2)
        
        if probability > probability_max:
            probability_max = probability
            probability_max_image = i

    print(probability_max, probability_max_image)