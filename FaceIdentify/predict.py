import os
import random
from PIL import Image
from FaceIdentify.nets.facenet import facenet_image


def random_files_from_directory(directory_path, num_files=2):
    # 获取目录中的所有文件列表
    files = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]
    
    # 如果文件数量少于要随机选择的文件数量，返回全部文件
    if len(files) < num_files:
        return files
    
    # 随机选择并返回文件
    return random.sample(files, num_files)


if __name__ == "__main__":
    model = facenet_image()

    # # 截取图片随机测试模式
    # for i in range(50):
    #     selected_files = random_files_from_directory('/Users/jayden/Documents/FallDetectionSystem/Data/goals_pre')
    
    #     img1 = Image.open(f"/Users/jayden/Documents/FallDetectionSystem/Data/goals_pre/" + selected_files[0])
    #     img2 = Image.open(f"/Users/jayden/Documents/FallDetectionSystem/Data/goals_pre/" + selected_files[1])

    #     probability = model.detect_image(img1, img2)
    #     print(probability)

    # 选定图片测试模式
    img1_path = "/Users/jayden/Documents/FallDetectionSystem/Data/goals_pre/face_4.jpg"
    img2_path = "/Users/jayden/Library/CloudStorage/OneDrive-jaydentang/Datasets/lfw/Andre_Agassi/Andre_Agassi_0010.jpg"

    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    probability = model.detect_image(img1, img2)
    print(probability)
