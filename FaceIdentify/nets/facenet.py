import torch
import torch.nn as nn
from torch.nn import functional as F
import torch.backends.cudnn as cudnn
import numpy as np
import matplotlib.pyplot as plt
from FaceIdentify.nets.mobelnet import mobilenet
from FaceIdentify.utils.utils import preprocess_input, resize_image, show_config
from Settings.json_settings import Settings


class facenet(nn.Module):
    def __init__(
        self,
        dropout_keep_prob=0.5,
        embedding_size=128,
        num_classes=None,
        mode="train",
        pretrained=False,
    ):
        super(facenet, self).__init__()
        self.backbone = mobilenet(pretrained)
        flat_shape = 1024
        self.avg = nn.AdaptiveAvgPool2d((1, 1))
        self.Dropout = nn.Dropout(1 - dropout_keep_prob)
        self.Bottleneck = nn.Linear(flat_shape, embedding_size, bias=False)
        self.last_bn = nn.BatchNorm1d(
            embedding_size, eps=0.001, momentum=0.1, affine=True
        )
        if mode == "train":
            self.classifier = nn.Linear(embedding_size, num_classes)

    def forward(self, x, mode="predict"):
        if mode == "predict":
            x = self.backbone(x)
            x = self.avg(x)
            x = x.view(x.size(0), -1)
            x = self.Dropout(x)
            x = self.Bottleneck(x)
            x = self.last_bn(x)
            x = F.normalize(x, p=2, dim=1)
            return x
        x = self.backbone(x)
        x = self.avg(x)
        x = x.view(x.size(0), -1)
        x = self.Dropout(x)
        x = self.Bottleneck(x)
        before_normalize = self.last_bn(x)

        x = F.normalize(before_normalize, p=2, dim=1)
        cls = self.classifier(before_normalize)
        return x, cls

    def forward_feature(self, x):
        x = self.backbone(x)
        x = self.avg(x)
        x = x.view(x.size(0), -1)
        x = self.Dropout(x)
        x = self.Bottleneck(x)
        before_normalize = self.last_bn(x)
        x = F.normalize(before_normalize, p=2, dim=1)
        return before_normalize, x

    def forward_classifier(self, x):
        x = self.classifier(x)
        return x

#--------------------------------------------#
#   使用自己训练好的模型预测需要修改2个参数
#   model_path和backbone需要修改！
#--------------------------------------------#
class facenet_image(object):
    _defaults = {
        #--------------------------------------------------------------------------#
        #   使用自己训练好的模型进行预测要修改model_path，指向logs文件夹下的权值文件
        #   训练好后logs文件夹下存在多个权值文件，选择验证集损失较低的即可。
        #   验证集损失较低不代表准确度较高，仅代表该权值在验证集上泛化性能较好。
        #--------------------------------------------------------------------------#
        "model_path"    : "FaceIdentify/facenet_mobilenet.pth",
        #--------------------------------------------------------------------------#
        #   输入图片的大小。
        #--------------------------------------------------------------------------#
        "input_shape"   : [160, 160, 3],
        #--------------------------------------------------------------------------#
        #   所使用到的主干特征提取网络
        #--------------------------------------------------------------------------#
        "backbone"      : "mobilenet",
        #-------------------------------------------#
        #   是否进行不失真的resize
        #-------------------------------------------#
        "letterbox_image"   : True,
        #-------------------------------------------#
        #   是否使用Cuda
        #   没有GPU可以设置成False
        #-------------------------------------------#
        "cuda"              : False,
    }

    @classmethod
    def get_defaults(cls, n):
        if n in cls._defaults:
            return cls._defaults[n]
        else:
            return "Unrecognized attribute name '" + n + "'"

    #---------------------------------------------------#
    #   初始化facenet
    #---------------------------------------------------#
    def __init__(self, **kwargs):
        settings = Settings()
        self.settings = settings.items

        self.__dict__.update(self._defaults)
        for name, value in kwargs.items():
            setattr(self, name, value)

        self.generate()
        
        show_config(**self._defaults)
        
    def generate(self):
        #---------------------------------------------------#
        #   载入模型与权值
        #---------------------------------------------------#
        print('Loading weights into state dict...')
        device      = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.net    = facenet(mode="predict").eval()
        self.net.load_state_dict(torch.load(self.model_path, map_location=device), strict=False)
        print('{} model loaded.'.format(self.model_path))

        if self.cuda:
            self.net = torch.nn.DataParallel(self.net)
            cudnn.benchmark = True
            self.net = self.net.cuda()
    
    #---------------------------------------------------#
    #   检测图片
    #---------------------------------------------------#
    def detect_image(self, image_1, image_2):
        #---------------------------------------------------#
        #   图片预处理，归一化
        #---------------------------------------------------#
        with torch.no_grad():
            image_1 = resize_image(image_1, [self.input_shape[1], self.input_shape[0]], letterbox_image=self.letterbox_image)
            image_2 = resize_image(image_2, [self.input_shape[1], self.input_shape[0]], letterbox_image=self.letterbox_image)
            
            photo_1 = torch.from_numpy(np.expand_dims(np.transpose(preprocess_input(np.array(image_1, np.float32)), (2, 0, 1)), 0))
            photo_2 = torch.from_numpy(np.expand_dims(np.transpose(preprocess_input(np.array(image_2, np.float32)), (2, 0, 1)), 0))
            
            if self.cuda:
                photo_1 = photo_1.cuda()
                photo_2 = photo_2.cuda()
                
            #---------------------------------------------------#
            #   图片传入网络进行预测
            #---------------------------------------------------#
            output1 = self.net(photo_1).cpu().numpy()
            output2 = self.net(photo_2).cpu().numpy()
            
            #---------------------------------------------------#
            #   计算二者之间的距离
            #---------------------------------------------------#
            l1 = np.linalg.norm(output1 - output2, axis=1)
            # print(l1)
        
        if l1 > self.settings['isSamePerson']:
            return False
        else:
            return True
