from PIL import Image
from .nets.facenet import facenet_image


def predict(image_test_path, image_goals_path):
    RightProbability = 1.2

    model = facenet_image()

    image_test = Image.open(image_test_path)
    for image_goal in image_goals_path:
        image_goal = Image.open(image_goal)
        probability = model.detect_image(image_test, image_goal)
        if probability < RightProbability:
            return True
        else:
            return False
