from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

# 圆形进度条
class PyCircularProgress(QWidget):
    def __init__(
        self,
        value = 0,
        progress_width = 10,
        is_rounded = True,
        max_value = 100,
        progress_color = "#ff79c6",
        enable_text = True,
        font_family = "Segoe UI",
        font_size = 12,
        suffix = "%",
        text_color = "#ff79c6",
        enable_bg = True,
        bg_color = "#44475a"
    ):
        QWidget.__init__(self)

        # 自定义属性
        self.value = value
        self.progress_width = progress_width
        self.progress_rounded_cap = is_rounded
        self.max_value = max_value
        self.progress_color = progress_color
        # 文本
        self.enable_text = enable_text
        self.font_family = font_family
        self.font_size = font_size
        self.suffix = suffix
        self.text_color = text_color
        # 背景
        self.enable_bg = enable_bg
        self.bg_color = bg_color

    # 添加阴影
    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 80))
            self.setGraphicsEffect(self.shadow)

    # 设置值
    def set_value(self, value):
        self.value = value
        self.repaint() # 更改值后渲染进度条


    # 绘制事件(在这里设计圆形进度条)
    def paintEvent(self, e):
        # 设置进度条参数
        width = self.width() - self.progress_width
        height = self.height() - self.progress_width
        margin = self.progress_width / 2
        value =  self.value * 360 / self.max_value

        # 绘制
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) # remove pixelated edges
        paint.setFont(QFont(self.font_family, self.font_size))

        # 创建QRect对象
        rect = QRect(0, 0, self.width(), self.height())
        paint.setPen(Qt.NoPen)

        # 创建QPen对象
        pen = QPen()             
        pen.setWidth(self.progress_width)
        # 设置进度条线帽
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # 如果设置启用背景, 则绘制背景
        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)  
            paint.drawArc(margin, margin, width, height, 0, 360 * 16)

        # 创建圆弧/圆形进度
        pen.setColor(QColor(self.progress_color))
        paint.setPen(pen)      
        paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)       

        # 创建文本
        if self.enable_text:
            pen.setColor(QColor(self.text_color))
            paint.setPen(pen)
            paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

        # 结束
        paint.end()