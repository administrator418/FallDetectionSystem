from UI.gui.uis.windows.main_window.functions_main_window import *
import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
from UI.gui.core.json_settings import Settings
from UI.gui.uis.windows.main_window import *
from UI.gui.widgets import *
from ModelPredict.predict_stream import PredictStream

# 调整 dpi
# ///////////////////////////////////////////////////////////////
# dpi = QApplication(sys.argv).primaryScreen().logicalDotsPerInch()
# print(f"DPI: {dpi}, 修改下面为DPI的int型")
os.environ["QT_FONT_DPI"] = "72"



# 主界面
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置主界面
        # 从 "gui\uis\main_window\ui_main.py" 导入 UI_MainWindow 类
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # 导入 settings
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # 设置主界面
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # 是否隐藏调整手柄
        SetupMainWindow.setup_gui(self)

        # 设置摄像头模式帧处理线程
        # ///////////////////////////////////////////////////////////////
        self.stream_thread = MainWindow.StreamThread(self)
        self.stream_thread.new_frame.connect(self.update_image_display)

        # 显示主界面
        # ///////////////////////////////////////////////////////////////
        self.show()

    # 摄像头模式帧处理线程
    class StreamThread(QThread):
        new_frame = Signal(QImage)

        def __init__(self, parent=None):
            super(MainWindow.StreamThread, self).__init__(parent)
            self.active = False

        def run(self):
            with PredictStream() as predict_stream:
                while self.active:
                    im0 = predict_stream.return_frame()
                    if im0 is None:
                        self.quit()  # 优雅地结束线程
                        break
                    height, width, channels = im0.shape
                    bytes_per_line = channels * width
                    q_img = QImage(im0.data, width, height, bytes_per_line, QImage.Format_RGB888)
                    self.new_frame.emit(q_img)

    # 更新图像显示
    # ///////////////////////////////////////////////////////////////
    def update_image_display(self, q_img):
        pixmap = QPixmap.fromImage(q_img)
        self.ui.load_pages.label_stream.setPixmap(pixmap)
        self.ui.load_pages.label_stream.setAlignment(Qt.AlignCenter)

    # 当按钮被点击时运行函数
    # 通过对象名称/按钮ID检查功能
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # 获取被点击的按钮
        btn = SetupMainWindow.setup_btns(self)

        # 左侧菜单栏
        # ///////////////////////////////////////////////////////////////
        
        # 主页按钮
        if btn.objectName() == "btn_home":
            # 选择菜单
            self.ui.left_menu.select_only_one(btn.objectName())

            # 导入页面
            MainFunctions.set_page(self, self.ui.load_pages.page_welcome)

        # 摄像头模式
        if btn.objectName() == "btn_stream":
            # 选择菜单
            self.ui.left_menu.select_only_one(btn.objectName())

            # 导入页面
            MainFunctions.set_page(self, self.ui.load_pages.page_stream)

        # 文件测试模式
        if btn.objectName() == "btn_files":
            # 选择菜单
            self.ui.left_menu.select_only_one(btn.objectName())

            # 导入页面
            MainFunctions.set_page(self, self.ui.load_pages.page_files)

        # 信息按钮
        if btn.objectName() == "btn_info":
            # C检查左列是否可见
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())

                # 显示/隐藏
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # 显示 / 隐藏
                    MainFunctions.toggle_left_column(self)
                
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # 更改左列菜单
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self, 
                    menu = self.ui.left_column.menus.menu_info,
                    title = "Information",
                    icon_path = Functions.set_svg_icon("icon_info.svg")
                )

        # 左侧设置按钮
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # 检查左列是否可见
            if not MainFunctions.left_column_is_visible(self):
                # 显示/隐藏
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # 显示/隐藏
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # 修改左列菜单
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self, 
                    menu = self.ui.left_column.menus.menu_settings,
                    title = "Settings",
                    icon_path = Functions.set_svg_icon("icon_settings.svg")
                )

        # 标题栏菜单
        # ///////////////////////////////////////////////////////////////
        
        # 摄像头模式页按钮
        if btn.objectName() == "btn_stream_start":
            self.stream_thread.active = True
            self.stream_thread.start()
        
        if btn.objectName() == "btn_stream_end":
            self.stream_thread.active = False
            self.stream_thread.wait()
            self.ui.load_pages.label_stream.clear()

        # 测试
        # print(f"Button {btn.objectName()}, clicked!")

    # 左侧菜单按钮被释放
    # 当按钮释放时运行函数
    # 通过对象名称/按钮ID检查功能
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # 获取被释放的按钮
        btn = SetupMainWindow.setup_btns(self)

        # 测试
        # print(f"Button {btn.objectName()}, released!")

    # 重新调整窗口大小
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # 鼠标拖拽窗口
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # 设置拖动窗口位置
        self.dragPos = event.globalPos()


# 主函数
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # 开始程序
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("UI/icon.ico"))
    window = MainWindow()

    # 退出程序
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec_())