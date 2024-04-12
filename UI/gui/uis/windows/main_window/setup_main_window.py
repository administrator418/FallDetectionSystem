from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from .functions_main_window import *
import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from gui.widgets import *
from .ui_main import *
from .functions_main_window import *

# 
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # 设置主窗口
        # 从 "gui\uis\main_window\ui_main.py" 导入 UI_MainWindow 类
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # 添加左菜单
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "主页",
            "btn_tooltip" : "主页",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_stream.svg",
            "btn_id" : "btn_stream",
            "btn_text" : "摄像头模式",
            "btn_tooltip" : "摄像头模式",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_files.svg",
            "btn_id" : "btn_files",
            "btn_text" : "测试模式",
            "btn_tooltip" : "测试模式",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_info.svg",
            "btn_id" : "btn_info",
            "btn_text" : "应用信息",
            "btn_tooltip" : "显示应用信息",
            "show_top" : False,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_settings",
            "btn_text" : "设置",
            "btn_tooltip" : "打开设置",
            "show_top" : False,
            "is_active" : False
        }
    ]

    # 添加标题栏菜单
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        
    ]

    # 设置自定义小部件的自定义按钮
    # 当按钮被点击时获取 sender() 函数
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # 使用自定义参数设置主窗口
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # 程序名称
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # 移除标题栏
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # 添加拖拽手柄
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # 单击/释放 左侧菜单按钮时 左侧菜单/获取信号
        # ///////////////////////////////////////////////////////////////
        # 添加左菜单
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # 设置信号
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # 标题栏/ 添加额外按钮
        # ///////////////////////////////////////////////////////////////
        # 添加标题栏菜单
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # 设置信号
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # 设置标题
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("欢迎使用跌倒检测系统")

        # 设置左列信号
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # 设置初始页面/设置左右列菜单
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_welcome)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # 自定义小部件
        # 这里添加了使用Qt Designer创建的页面和列的自定义小部件。
        # 
        #
        # 加载页面、左栏和右栏的对象
        # 您可以使用以下对象访问 Qt Designer 项目内的对象：
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # 导入设置
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # 导入主题颜色
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # 左列
        # ///////////////////////////////////////////////////////////////

        # 页
        # ///////////////////////////////////////////////////////////////

        # 欢迎页 - 向欢迎页添加图标
        self.logo_svg = QSvgWidget(Functions.set_svg_image("logo_home.svg"))
        self.ui.load_pages.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        
        # ///////////////////////////////////////////////////////////////
        # 结束自定义小部件
        # ///////////////////////////////////////////////////////////////

    # 调整手柄大小和更改位置
    # 调整窗口大小时调整或更改位置
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)