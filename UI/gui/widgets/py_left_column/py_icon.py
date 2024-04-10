from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

# 带有自定义颜色的图标
# ///////////////////////////////////////////////////////////////
class PyIcon(QWidget):
    def __init__(
        self,
        icon_path,
        icon_color
    ):
        super().__init__()

        # 属性
        self._icon_path = icon_path
        self._icon_color = icon_color

        # 初始化UI
        self.setup_ui()

    def setup_ui(self):
        # 布局
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)

        # 标签
        self.icon = QLabel()
        self.icon.setAlignment(Qt.AlignCenter)
        
        # 绘制器
        self.set_icon(self._icon_path, self._icon_color)

        # 添加到布局
        self.layout.addWidget(self.icon)

    def set_icon(self, icon_path, icon_color = None):
        # 取得颜色
        color = ""
        if icon_color != None:
            color = icon_color
        else:
            color = self._icon_color

        # 为图标应用自定义颜色
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)       
        painter.end()

        # 将处理后的图像设置到标签控件上
        self.icon.setPixmap(icon)

