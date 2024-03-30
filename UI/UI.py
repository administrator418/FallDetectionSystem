import sys
import os
sys.path.append(os.getcwd() + "/ModelPredict")
from Ui_falldetection import Ui_MainWindow
from predict_image import predict_image
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.method = {"应用模式-实时监控": 0, "测试模式-实时监控": 1, "测试模式-图片": 2, "测试模式-视频": 3}

        self.toolButton_FilePath.clicked.connect(self.openFile)

        self.pushButton_Start.clicked.connect(self.start)

    def openFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Image Files (*.jpg *.jpeg *.png);;Video Files (*.mp4 *.avi")
        self.lineEdit_FilePath.setText(filePath)

    def start(self):
        method = self.method[self.comboBox_Method.currentText()]
        filePath = self.lineEdit_FilePath.text()

        if method == 0:
            pass
        elif method == 1:
            pass
        elif method == 2:
            predict_image(filePath)

        elif method == 3:
            pass



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()