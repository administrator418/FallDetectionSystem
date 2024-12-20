import torch
import torch.backends.cudnn as cudnn

from nets.facenet import facenet_image
from utils.dataloader import LFWDataset
from utils.utils_metrics import test

from path import lfw_path, casia_path

if __name__ == "__main__":
    #--------------------------------------#
    #   是否使用cuda
    #   没有GPU可以设置成False
    #--------------------------------------#
    cuda            = False
    #--------------------------------------------------------#
    #   输入图像大小，常用设置如[112, 112, 3]
    #--------------------------------------------------------#
    input_shape     = [160, 160, 3]
    #--------------------------------------#
    #   训练好的权值文件
    #--------------------------------------#
    model_path      = "FaceIdentify/facenet_mobilenet.pth"
    #--------------------------------------#
    #   LFW评估数据集的文件路径
    #   以及对应的txt文件
    #--------------------------------------#
    lfw_dir_path    = lfw_path
    lfw_pairs_path  = "FaceIdentify/lfw_pair.txt"
    #--------------------------------------#
    #   评估的批次大小和记录间隔
    #--------------------------------------#
    batch_size      = 256
    log_interval    = 1
    #--------------------------------------#
    #   ROC图的保存路径
    #--------------------------------------#
    png_save_path   = "FaceIdentify/roc_test.png"

    test_loader = torch.utils.data.DataLoader(
        LFWDataset(dir=lfw_dir_path, pairs_path=lfw_pairs_path, image_size=input_shape), batch_size=batch_size, shuffle=False)

    model = facenet_image(mode="predict")

    print('Loading weights into state dict...')
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.load_state_dict(torch.load(model_path, map_location=device), strict=False)
    model  = model.eval()

    if cuda:
        model = torch.nn.DataParallel(model)
        cudnn.benchmark = True
        model = model.cuda()

    test(test_loader, model, png_save_path, log_interval, batch_size, cuda)
