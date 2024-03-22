# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'falldetection.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QGraphicsView,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 665)
        self.action_Fall_Detection = QAction(MainWindow)
        self.action_Fall_Detection.setObjectName("action_Fall_Detection")
        self.action_Fall_Detection_2 = QAction(MainWindow)
        self.action_Fall_Detection_2.setObjectName("action_Fall_Detection_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setGeometry(QRect(0, 0, 640, 640))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(639, 21, 351, 561))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comboBox_2 = QComboBox(self.widget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName("comboBox_2")

        self.horizontalLayout_3.addWidget(self.comboBox_2)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName("label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.toolButton = QToolButton(self.widget)
        self.toolButton.setObjectName("toolButton")

        self.horizontalLayout_2.addWidget(self.toolButton)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 24))
        self.menuFall_Detection = QMenu(self.menubar)
        self.menuFall_Detection.setObjectName("menuFall_Detection")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFall_Detection.menuAction())
        self.menuFall_Detection.addAction(self.action_Fall_Detection)
        self.menuFall_Detection.addSeparator()
        self.menuFall_Detection.addAction(self.action_Fall_Detection_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.action_Fall_Detection.setText(
            QCoreApplication.translate("MainWindow", "\u5173\u4e8eFall Detection", None)
        )
        self.action_Fall_Detection_2.setText(
            QCoreApplication.translate("MainWindow", "\u9000\u51faFall Detection", None)
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:24pt;">\u8dcc\u5012\u68c0\u6d4b\u7cfb\u7edf</span></p></body></html>',
                None,
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow", "\u6a21\u5f0f\u9009\u62e9\uff1a", None
            )
        )
        self.comboBox.setItemText(
            0,
            QCoreApplication.translate(
                "MainWindow", "\u5e94\u7528\u6a21\u5f0f-\u5b9e\u65f6\u76d1\u63a7", None
            ),
        )
        self.comboBox.setItemText(
            1,
            QCoreApplication.translate(
                "MainWindow", "\u6d4b\u8bd5\u6a21\u5f0f-\u5b9e\u65f6\u76d1\u63a7", None
            ),
        )
        self.comboBox.setItemText(
            2,
            QCoreApplication.translate(
                "MainWindow", "\u6d4b\u8bd5\u6a21\u5f0f-\u56fe\u7247", None
            ),
        )
        self.comboBox.setItemText(
            3,
            QCoreApplication.translate(
                "MainWindow", "\u6d4b\u8bd5\u6a21\u5f0f-\u89c6\u9891", None
            ),
        )

        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow", "\u6a21\u578b\u9009\u62e9\uff1a", None
            )
        )
        self.comboBox_2.setItemText(
            0, QCoreApplication.translate("MainWindow", "FnF_real", None)
        )
        self.comboBox_2.setItemText(
            1, QCoreApplication.translate("MainWindow", "FnF_test", None)
        )
        self.comboBox_2.setItemText(
            2, QCoreApplication.translate("MainWindow", "Fall_test", None)
        )
        self.comboBox_2.setItemText(
            3, QCoreApplication.translate("MainWindow", "Face_test", None)
        )

        self.label.setText(
            QCoreApplication.translate("MainWindow", "\u6587\u4ef6\u8def\u5f84:", None)
        )
        self.toolButton.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", "\u5f00\u59cb", None)
        )
        self.menuFall_Detection.setTitle(
            QCoreApplication.translate("MainWindow", "Fall Detection", None)
        )

    # retranslateUi
