from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
from .py_left_menu_button import PyLeftMenuButton
from .py_div import PyDiv
from UI.gui.core.functions import *

# 左侧菜单
# ///////////////////////////////////////////////////////////////
class PyLeftMenu(QWidget):
    # 信号
    clicked = Signal(object)
    released = Signal(object)

    def __init__(
        self,
        parent = None,
        app_parent = None,
        dark_one = "#1b1e23",
        dark_three = "#21252d",
        dark_four = "#272c36",
        bg_one = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        context_color = "#568af2",
        text_foreground = "#8a95aa",
        text_active = "#dce1ec",
        duration_time = 500,
        radius = 8,
        minimum_width = 50,
        maximum_width = 240,
        icon_path = "icon_menu.svg",
        icon_path_close = "icon_menu_close.svg",
        toggle_text = "Hide Menu",
        toggle_tooltip = "Show menu"
    ):
        super().__init__()

        # 属性
        # ///////////////////////////////////////////////////////////////
        self._dark_one = dark_one
        self._dark_three = dark_three
        self._dark_four = dark_four
        self._bg_one = bg_one
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active
        self._context_color = context_color
        self._text_foreground = text_foreground
        self._text_active = text_active
        self._duration_time = duration_time
        self._radius = radius
        self._minimum_width = minimum_width
        self._maximum_width = maximum_width
        self._icon_path = Functions.set_svg_icon(icon_path)
        self._icon_path_close = Functions.set_svg_icon(icon_path_close)

        # 设置父级
        self._parent = parent
        self._app_parent = app_parent

        # 初始化UI
        self.setup_ui()

        # 设置背景颜色
        self.bg.setStyleSheet(f"background: {dark_one}; border-radius: {radius};")

        # 切换按钮和分割菜单
        # ///////////////////////////////////////////////////////////////
        self.toggle_button = PyLeftMenuButton(
            app_parent, 
            text = toggle_text, 
            tooltip_text = toggle_tooltip,
            dark_one = self._dark_one,
            dark_three = self._dark_three,
            dark_four = self._dark_four,
            bg_one = self._bg_one,
            icon_color = self._icon_color,
            icon_color_hover = self._icon_color_active,
            icon_color_pressed = self._icon_color_pressed,
            icon_color_active = self._icon_color_active,
            context_color = self._context_color,
            text_foreground = self._text_foreground,
            text_active = self._text_active,
            icon_path = icon_path
        )
        self.toggle_button.clicked.connect(self.toggle_animation)
        self.div_top = PyDiv(dark_four)

        # 添加到顶部布局
        # ///////////////////////////////////////////////////////////////
        self.top_layout.addWidget(self.toggle_button)
        self.top_layout.addWidget(self.div_top)

        # 添加到底部布局
        # ///////////////////////////////////////////////////////////////
        self.div_bottom = PyDiv(dark_four)
        self.div_bottom.hide()
        self.bottom_layout.addWidget(self.div_bottom)

    # 向左侧菜单添加按钮并发出信号
    # ///////////////////////////////////////////////////////////////
    def add_menus(self, parameters):
        if parameters != None:
            for parameter in parameters:
                _btn_icon = parameter['btn_icon']
                _btn_id = parameter['btn_id']
                _btn_text = parameter['btn_text']
                _btn_tooltip = parameter['btn_tooltip']
                _show_top = parameter['show_top']
                _is_active = parameter['is_active']

                self.menu = PyLeftMenuButton(
                    self._app_parent,
                    text = _btn_text,
                    btn_id = _btn_id,
                    tooltip_text = _btn_tooltip,
                    dark_one = self._dark_one,
                    dark_three = self._dark_three,
                    dark_four = self._dark_four,
                    bg_one = self._bg_one,
                    icon_color = self._icon_color,
                    icon_color_hover = self._icon_color_active,
                    icon_color_pressed = self._icon_color_pressed,
                    icon_color_active = self._icon_color_active,
                    context_color = self._context_color,
                    text_foreground = self._text_foreground,
                    text_active = self._text_active,
                    icon_path = _btn_icon,
                    is_active = _is_active
                )
                self.menu.clicked.connect(self.btn_clicked)
                self.menu.released.connect(self.btn_released)

                # 添加到顶部或底部布局
                if _show_top:
                    self.top_layout.addWidget(self.menu)
                else:
                    self.div_bottom.show()
                    self.bottom_layout.addWidget(self.menu)

    # 按钮点击发出信号
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        self.clicked.emit(self.menu)
    
    def btn_released(self):
        self.released.emit(self.menu)

    # 展开/收起左侧菜单
    # ///////////////////////////////////////////////////////////////
    def toggle_animation(self):
        # 创建动画
        self.animation = QPropertyAnimation(self._parent, b"minimumWidth")
        self.animation.stop()
        if self.width() == self._minimum_width:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self._maximum_width)
            self.toggle_button.set_active_toggle(True)
            self.toggle_button.set_icon(self._icon_path_close)
        else:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self._minimum_width)
            self.toggle_button.set_active_toggle(False)
            self.toggle_button.set_icon(self._icon_path)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(self._duration_time)
        self.animation.start()

    # 选择唯一按钮
    # ///////////////////////////////////////////////////////////////
    def select_only_one(self, widget: str):
        for btn in self.findChildren(QPushButton):
            if btn.objectName() == widget:
                btn.set_active(True)
            else:
                btn.set_active(False)

    # 选择唯一选项卡按钮
    # ///////////////////////////////////////////////////////////////
    def select_only_one_tab(self, widget: str):
        for btn in self.findChildren(QPushButton):
            if btn.objectName() == widget:
                btn.set_active_tab(True)
            else:
                btn.set_active_tab(False)

    # 取消所有按钮
    # ///////////////////////////////////////////////////////////////
    def deselect_all(self):
        for btn in self.findChildren(QPushButton):
            btn.set_active(False)

    # 取消所有选项卡按钮
    # ///////////////////////////////////////////////////////////////
    def deselect_all_tab(self):
        for btn in self.findChildren(QPushButton):
            btn.set_active_tab(False)

    # 设置程序
    # ///////////////////////////////////////////////////////////////
    def setup_ui(self):
        # 添加菜单布局
        self.left_menu_layout = QVBoxLayout(self)
        self.left_menu_layout.setContentsMargins(0,0,0,0)

        # 背景框架
        self.bg = QFrame()

        # 顶部框架
        self.top_frame = QFrame()

        # 底部框架
        self.bottom_frame = QFrame()

        # 添加布局
        self._layout = QVBoxLayout(self.bg)
        self._layout.setContentsMargins(0,0,0,0)

        # 顶部布局
        self.top_layout = QVBoxLayout(self.top_frame)
        self.top_layout.setContentsMargins(0,0,0,0)
        self.top_layout.setSpacing(1)

        # 底部布局
        self.bottom_layout = QVBoxLayout(self.bottom_frame)
        self.bottom_layout.setContentsMargins(0,0,0,8)
        self.bottom_layout.setSpacing(1)

        # 添加到布局
        self._layout.addWidget(self.top_frame, 0, Qt.AlignTop)
        self._layout.addWidget(self.bottom_frame, 0, Qt.AlignBottom)

        # 添加背景到菜单布局
        self.left_menu_layout.addWidget(self.bg)

        

        

