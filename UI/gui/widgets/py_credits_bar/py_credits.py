from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

# 显示版权和版本信息
# ///////////////////////////////////////////////////////////////
class PyCredits(QWidget):
    def __init__(
        self,
        copyright,
        version,
        bg_two,
        font_family,
        text_size,
        text_description_color,
        radius = 8,
        padding = 10
    ):
        super().__init__()

        # 属性
        self._copyright = copyright
        self._version = version
        self._bg_two = bg_two
        self._font_family = font_family
        self._text_size = text_size
        self._text_description_color = text_description_color
        self._radius = radius
        self._padding = padding

        # 调用setup_ui()
        self.setup_ui()

    def setup_ui(self):
        # 添加布局
        self.widget_layout = QHBoxLayout(self)
        self.widget_layout.setContentsMargins(0,0,0,0)

        # 背景样式
        style = f"""
        #bg_frame {{
            border-radius: {self._radius}px;
            background-color: {self._bg_two};
        }}
        .QLabel {{
            font: {self._text_size}pt "{self._font_family}";
            color: {self._text_description_color};
            padding-left: {self._padding}px;
            padding-right: {self._padding}px;
        }}
        """

        # 背景框架, 应用上面的样式
        self.bg_frame = QFrame()
        self.bg_frame.setObjectName("bg_frame")
        self.bg_frame.setStyleSheet(style)

        # 将背景框架添加到布局
        self.widget_layout.addWidget(self.bg_frame)

        # 背景布局设置
        self.bg_layout = QHBoxLayout(self.bg_frame)
        self.bg_layout.setContentsMargins(0,0,0,0)

        # 添加版权信息
        self.copyright_label = QLabel(self._copyright)
        self.copyright_label.setAlignment(Qt.AlignVCenter)

        # 添加版本信息
        self.version_label = QLabel(self._version)
        self.version_label.setAlignment(Qt.AlignVCenter)

        # 添加分隔符
        self.separator = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # 将标签和分隔符添加到布局
        self.bg_layout.addWidget(self.copyright_label)
        self.bg_layout.addSpacerItem(self.separator)
        self.bg_layout.addWidget(self.version_label)
