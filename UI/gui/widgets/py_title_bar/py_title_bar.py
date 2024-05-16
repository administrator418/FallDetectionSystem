from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
from UI.gui.core.functions import *
from Settings.json_settings import Settings
from .py_div import PyDiv
from .py_title_button import PyTitleButton

# 全局变量
# ///////////////////////////////////////////////////////////////
_is_maximized = False
_old_size = QSize()

# 顶部栏
# 具有移动应用程序、最大化、还原、最小化、关闭按钮和额外按钮的顶部栏
# ///////////////////////////////////////////////////////////////
class PyTitleBar(QWidget):
    # 信号
    clicked = Signal(object)
    released = Signal(object)

    def __init__(
        self,
        parent,
        app_parent,
        logo_image = "logo_top_100x22.svg",
        logo_width = 100,
        buttons = None,
        dark_one = "#1b1e23",
        bg_color = "#343b48",
        div_color = "#3c4454",
        btn_bg_color = "#343b48",
        btn_bg_color_hover = "#3c4454",
        btn_bg_color_pressed = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        context_color = "#6c99f4",
        text_foreground = "#8a95aa",
        radius = 8,
        font_family = "Segoe UI",
        title_size = 10,
        is_custom_title_bar = True,
    ):
        super().__init__()

        settings = Settings()
        self.settings = settings.items

        # 参数
        self._logo_image = logo_image
        self._dark_one = dark_one
        self._bg_color = bg_color
        self._div_color = div_color
        self._parent = parent
        self._app_parent = app_parent
        self._btn_bg_color = btn_bg_color
        self._btn_bg_color_hover = btn_bg_color_hover
        self._btn_bg_color_pressed = btn_bg_color_pressed  
        self._context_color = context_color
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active
        self._font_family = font_family
        self._title_size = title_size
        self._text_foreground = text_foreground
        self._is_custom_title_bar = is_custom_title_bar

        # 初始化UI
        self.setup_ui()

        # 添加背景颜色
        self.bg.setStyleSheet(f"background-color: {bg_color}; border-radius: {radius}px;")

        # 设置图标和宽度
        self.top_logo.setMinimumWidth(logo_width)
        self.top_logo.setMaximumWidth(logo_width)
        # self.top_logo.setPixmap(Functions.set_svg_image(logo_image))

        # 移动窗口/最大化/还原
        # ///////////////////////////////////////////////////////////////
        def moveWindow(event):
            # 最大化
            if parent.isMaximized():
                self.maximize_restore()
                # self.resize(_old_size)
                curso_x = parent.pos().x()
                curso_y = event.globalPos().y() - QCursor.pos().y()
                parent.move(curso_x, curso_y)
            # 移动窗口
            if event.buttons() == Qt.LeftButton:
                parent.move(parent.pos() + event.globalPos() - parent.dragPos)
                parent.dragPos = event.globalPos()
                event.accept()

        # 移动程序小部件
        if is_custom_title_bar:
            self.top_logo.mouseMoveEvent = moveWindow
            self.div_1.mouseMoveEvent = moveWindow
            self.title_label.mouseMoveEvent = moveWindow
            self.div_2.mouseMoveEvent = moveWindow
            self.div_3.mouseMoveEvent = moveWindow

        # 最大化/还原
        if is_custom_title_bar:
            self.top_logo.mouseDoubleClickEvent = self.maximize_restore
            self.div_1.mouseDoubleClickEvent = self.maximize_restore
            self.title_label.mouseDoubleClickEvent = self.maximize_restore
            self.div_2.mouseDoubleClickEvent = self.maximize_restore

        # 将小部件添加到标题栏
        # ///////////////////////////////////////////////////////////////
        self.bg_layout.addWidget(self.top_logo)
        self.bg_layout.addWidget(self.div_1)
        self.bg_layout.addWidget(self.title_label)
        self.bg_layout.addWidget(self.div_2)

        # 添加按钮
        # ///////////////////////////////////////////////////////////////
        self.minimize_button.released.connect(lambda: parent.showMinimized())
        self.maximize_restore_button.released.connect(lambda: self.maximize_restore())
        self.close_button.released.connect(lambda: parent.close())

        # 额外按钮布局
        self.bg_layout.addLayout(self.custom_buttons_layout)

        # 添加按钮
        if is_custom_title_bar:            
            self.bg_layout.addWidget(self.minimize_button)
            self.bg_layout.addWidget(self.maximize_restore_button)
            self.bg_layout.addWidget(self.close_button)

    # 将按钮添加到标题栏
    # 添加按钮和发射信号
    # ///////////////////////////////////////////////////////////////
    def add_menus(self, parameters):
        if parameters != None and len(parameters) > 0:
            for parameter in parameters:
                _btn_icon = Functions.set_svg_icon(parameter['btn_icon'])
                _btn_id = parameter['btn_id']
                _btn_tooltip = parameter['btn_tooltip']
                _is_active = parameter['is_active']

                self.menu = PyTitleButton(
                    self._parent,
                    self._app_parent,
                    btn_id = _btn_id,
                    tooltip_text = _btn_tooltip,
                    dark_one = self._dark_one,
                    bg_color = self._bg_color,
                    bg_color_hover = self._btn_bg_color_hover,
                    bg_color_pressed = self._btn_bg_color_pressed,
                    icon_color = self._icon_color,
                    icon_color_hover = self._icon_color_active,
                    icon_color_pressed = self._icon_color_pressed,
                    icon_color_active = self._icon_color_active,
                    context_color = self._context_color,
                    text_foreground = self._text_foreground,
                    icon_path = _btn_icon,
                    is_active = _is_active
                )
                self.menu.clicked.connect(self.btn_clicked)
                self.menu.released.connect(self.btn_released)

                # 添加到布局
                self.custom_buttons_layout.addWidget(self.menu)

            # 添加分隔
            if self._is_custom_title_bar:
                self.custom_buttons_layout.addWidget(self.div_3)

    # 标题栏发射信号
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        self.clicked.emit(self.menu)
    
    def btn_released(self):
        self.released.emit(self.menu)

    # 设置标题栏文本
    # ///////////////////////////////////////////////////////////////
    def set_title(self, title):
        self.title_label.setText(title)

    # 最大化/还原
    # maximize and restore parent window
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self, e = None):
        global _is_maximized
        global _old_size
        
        # 更改UI,调整手柄
        def change_ui():
            if _is_maximized:
                self._parent.ui.central_widget_layout.setContentsMargins(0,0,0,0)
                self._parent.ui.window.set_stylesheet(border_radius = 0, border_size = 0)
                self.maximize_restore_button.set_icon(
                    Functions.set_svg_icon("icon_restore.svg")
                )
            else:
                self._parent.ui.central_widget_layout.setContentsMargins(10,10,10,10)
                self._parent.ui.window.set_stylesheet(border_radius = 10, border_size = 2)
                self.maximize_restore_button.set_icon(
                    Functions.set_svg_icon("icon_maximize.svg")
                )

        # 检查事件
        if self._parent.isMaximized():
            _is_maximized = False
            self._parent.showNormal()
            change_ui()
        else:
            _is_maximized = True
            _old_size = QSize(self._parent.width(), self._parent.height())
            self._parent.showMaximized()
            change_ui()

    # 设置程序
    # ///////////////////////////////////////////////////////////////
    def setup_ui(self):
        # 添加菜单布局
        self.title_bar_layout = QVBoxLayout(self)
        self.title_bar_layout.setContentsMargins(0,0,0,0)

        # 添加背景
        self.bg = QFrame()

        # 添加背景布局
        self.bg_layout = QHBoxLayout(self.bg)
        self.bg_layout.setContentsMargins(10,0,5,0)
        self.bg_layout.setSpacing(0)

        # 分割
        self.div_1 = PyDiv(self._div_color)
        self.div_2 = PyDiv(self._div_color)
        self.div_3 = PyDiv(self._div_color)

        # 在应用程序的标题栏中创建一个视觉识别元素
        self.top_logo = QLabel()
        self.top_logo_layout = QVBoxLayout(self.top_logo)
        self.top_logo_layout.setContentsMargins(0,0,0,0)
        self.logo_svg = QSvgWidget()
        self.logo_svg.load(Functions.set_svg_image(self._logo_image))
        self.top_logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        # 标题标签
        self.title_label = QLabel()
        self.title_label.setAlignment(Qt.AlignVCenter)
        self.title_label.setStyleSheet(f'font: {self._title_size}pt "{self._font_family}"')

        # 自定义按钮布局
        self.custom_buttons_layout = QHBoxLayout()
        self.custom_buttons_layout.setContentsMargins(0,0,0,0)
        self.custom_buttons_layout.setSpacing(3)

        # 最小化按钮
        self.minimize_button = PyTitleButton(
            self._parent,
            self._app_parent,
            tooltip_text = "Close app",
            dark_one = self._dark_one,
            bg_color = self._btn_bg_color,
            bg_color_hover = self._btn_bg_color_hover,
            bg_color_pressed = self._btn_bg_color_pressed,
            icon_color = self._icon_color,
            icon_color_hover = self._icon_color_hover,
            icon_color_pressed = self._icon_color_pressed,
            icon_color_active = self._icon_color_active,
            context_color = self._context_color,
            text_foreground = self._text_foreground,
            radius = 6,
            icon_path = Functions.set_svg_icon("icon_minimize.svg")
        )

        # 最大化/还原
        self.maximize_restore_button = PyTitleButton(
            self._parent,
            self._app_parent,
            tooltip_text = "Maximize app",
            dark_one = self._dark_one,
            bg_color = self._btn_bg_color,
            bg_color_hover = self._btn_bg_color_hover,
            bg_color_pressed = self._btn_bg_color_pressed,
            icon_color = self._icon_color,
            icon_color_hover = self._icon_color_hover,
            icon_color_pressed = self._icon_color_pressed,
            icon_color_active = self._icon_color_active,
            context_color = self._context_color,
            text_foreground = self._text_foreground,
            radius = 6,
            icon_path = Functions.set_svg_icon("icon_maximize.svg")
        )

        # 关闭按钮
        self.close_button = PyTitleButton(
            self._parent,
            self._app_parent,
            tooltip_text = "Close app",
            dark_one = self._dark_one,
            bg_color = self._btn_bg_color,
            bg_color_hover = self._btn_bg_color_hover,
            bg_color_pressed = self._context_color,
            icon_color = self._icon_color,
            icon_color_hover = self._icon_color_hover,
            icon_color_pressed = self._icon_color_active,
            icon_color_active = self._icon_color_active,
            context_color = self._context_color,
            text_foreground = self._text_foreground,
            radius = 6,
            icon_path = Functions.set_svg_icon("icon_close.svg")
        )

        # 添加到布局
        self.title_bar_layout.addWidget(self.bg)