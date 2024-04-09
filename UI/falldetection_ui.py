# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'falldetection.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 655)
        MainWindow.setMinimumSize(QSize(1000, 655))
        MainWindow.setMaximumSize(QSize(1000, 655))
        self.action_Fall_Detection = QAction(MainWindow)
        self.action_Fall_Detection.setObjectName(u"action_Fall_Detection")
        self.action_Fall_Detection_2 = QAction(MainWindow)
        self.action_Fall_Detection_2.setObjectName(u"action_Fall_Detection_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 0, 640, 640))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(650, 6, 341, 591))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 0))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.comboBox_Method = QComboBox(self.layoutWidget)
        self.comboBox_Method.addItem("")
        self.comboBox_Method.addItem("")
        self.comboBox_Method.addItem("")
        self.comboBox_Method.addItem("")
        self.comboBox_Method.setObjectName(u"comboBox_Method")

        self.horizontalLayout_4.addWidget(self.comboBox_Method)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_FilePath = QLineEdit(self.layoutWidget)
        self.lineEdit_FilePath.setObjectName(u"lineEdit_FilePath")

        self.horizontalLayout_2.addWidget(self.lineEdit_FilePath)

        self.toolButton_FilePath = QToolButton(self.layoutWidget)
        self.toolButton_FilePath.setObjectName(u"toolButton_FilePath")

        self.horizontalLayout_2.addWidget(self.toolButton_FilePath)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_Start = QPushButton(self.layoutWidget)
        self.pushButton_Start.setObjectName(u"pushButton_Start")

        self.horizontalLayout.addWidget(self.pushButton_Start)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 24))
        self.menuFall_Detection = QMenu(self.menubar)
        self.menuFall_Detection.setObjectName(u"menuFall_Detection")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFall_Detection.menuAction())
        self.menuFall_Detection.addAction(self.action_Fall_Detection)
        self.menuFall_Detection.addSeparator()
        self.menuFall_Detection.addAction(self.action_Fall_Detection_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8dcc\u5012\u68c0\u6d4b\u7cfb\u7edf", None))
        self.action_Fall_Detection.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u7cfb\u7edf", None))
        self.action_Fall_Detection_2.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u7cfb\u7edf", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">\u8dcc\u5012\u68c0\u6d4b\u7cfb\u7edf</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f\u9009\u62e9\uff1a", None))
        self.comboBox_Method.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5e94\u7528\u6a21\u5f0f-\u5b9e\u65f6\u76d1\u63a7", None))
        self.comboBox_Method.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u6a21\u5f0f-\u5b9e\u65f6\u76d1\u63a7", None))
        self.comboBox_Method.setItemText(2, QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u6a21\u5f0f-\u56fe\u7247", None))
        self.comboBox_Method.setItemText(3, QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u6a21\u5f0f-\u89c6\u9891", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84:", None))
        self.toolButton_FilePath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_Start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.menuFall_Detection.setTitle(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf", None))
    # retranslateUi

