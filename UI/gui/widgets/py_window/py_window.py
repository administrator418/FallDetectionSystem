from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
from Settings.json_settings import Settings
from .styles import Styles

# PY WINDOW
# ///////////////////////////////////////////////////////////////
class PyWindow(QFrame):
    def __init__(
        self,
        parent,
        layout = Qt.Vertical,
        margin = 0,
        spacing = 2,
        bg_color = "#2c313c",
        text_color = "#fff",
        text_font = "9pt 'Segoe UI'",
        border_radius = 10,
        border_size = 2,
        border_color = "#343b48",
        enable_shadow = True
    ):
        super().__init__()

        # 导入设置
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # 属性
        # ///////////////////////////////////////////////////////////////
        self.parent = parent
        self.layout = layout
        self.margin = margin
        self.bg_color = bg_color
        self.text_color = text_color
        self.text_font = text_font
        self.border_radius = border_radius
        self.border_size = border_size
        self.border_color = border_color
        self.enable_shadow = enable_shadow

        # 对象名称
        # ///////////////////////////////////////////////////////////////   
        self.setObjectName("pod_bg_app")

        # 应用样式表
        # /////////////////////////////////////////////////////////////// 
        self.set_stylesheet()

        # 添加布局
        # ///////////////////////////////////////////////////////////////
        if layout == Qt.Vertical:
            # 垂直布局
            self.layout = QHBoxLayout(self)
        else:
            # 水平布局
            self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(margin, margin, margin, margin)
        self.layout.setSpacing(spacing)

        # 添加阴影
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            if enable_shadow:
                self.shadow = QGraphicsDropShadowEffect()
                self.shadow.setBlurRadius(20)
                self.shadow.setXOffset(0)
                self.shadow.setYOffset(0)
                self.shadow.setColor(QColor(0, 0, 0, 160))
                self.setGraphicsEffect(self.shadow)

    # 更新并应用样式表
    # ///////////////////////////////////////////////////////////////
    def set_stylesheet(
        self,
        bg_color = None,
        border_radius = None,
        border_size = None,
        border_color = None,
        text_color = None,
        text_font = None
    ):
        # 检查背景颜色
        if bg_color != None: internal_bg_color = bg_color
        else: internal_bg_color = self.bg_color

        # 检查边界半径
        if border_radius != None: internal_border_radius = border_radius
        else: internal_border_radius = self.border_radius

        # 检查边界大小
        if border_size != None: internal_border_size = border_size
        else: internal_border_size = self.border_size

        # 检查边界颜色
        if border_color != None: internal_border_color = border_color
        else: internal_border_color = self.border_color

        # 检查文本颜色
        if text_color != None: internal_text_color = text_color
        else: internal_text_color = self.text_color

        # 检查文本字体
        if text_font != None: internal_text_font = text_font
        else: internal_text_font = self.text_font

        self.setStyleSheet(Styles.bg_style.format(
            _bg_color = internal_bg_color,
            _border_radius = internal_border_radius,
            _border_size = internal_border_size,
            _border_color = internal_border_color,
            _text_color = internal_text_color,
            _text_font = internal_text_font
        ))
        