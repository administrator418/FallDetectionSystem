from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("按钮", self)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
