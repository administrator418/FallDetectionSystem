from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

# 自定义顶部菜单
# ///////////////////////////////////////////////////////////////
class PyDiv(QWidget):
    def __init__(self, color):
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0,5,0,5)
        self.frame_line = QFrame()
        self.frame_line.setStyleSheet(f"background: {color};")
        self.frame_line.setMaximumWidth(1)
        self.frame_line.setMinimumWidth(1)
        self.layout.addWidget(self.frame_line)
        self.setMaximumWidth(20)
        self.setMinimumWidth(20)
