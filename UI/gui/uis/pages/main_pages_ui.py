# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_welcome = QWidget()
        self.page_welcome.setObjectName(u"page_welcome")
        self.page_welcome.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_welcome)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_welcome)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 70))
        self.logo.setMaximumSize(QSize(300, 70))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)


        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_welcome)
        self.page_stream = QWidget()
        self.page_stream.setObjectName(u"page_stream")
        self.page_2_layout = QGridLayout(self.page_stream)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.label_stream = QLabel(self.page_stream)
        self.label_stream.setObjectName(u"label_stream")

        self.page_2_layout.addWidget(self.label_stream, 0, 0, 1, 2)

        self.btn_stream_start = QWidget(self.page_stream)
        self.btn_stream_start.setObjectName(u"btn_stream_start")
        self.btn_stream_start.setMinimumSize(QSize(0, 40))
        self.btn_stream_start.setMaximumSize(QSize(16777215, 40))
        self.btn_stream_start_layout = QVBoxLayout(self.btn_stream_start)
        self.btn_stream_start_layout.setSpacing(0)
        self.btn_stream_start_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_stream_start_layout.setObjectName(u"btn_stream_start_layout")

        self.page_2_layout.addWidget(self.btn_stream_start, 1, 0, 1, 1)

        self.btn_stream_end = QWidget(self.page_stream)
        self.btn_stream_end.setObjectName(u"btn_stream_end")
        self.btn_stream_end.setMinimumSize(QSize(0, 40))
        self.btn_stream_end.setMaximumSize(QSize(16777215, 40))
        self.btn_stream_end_layout = QVBoxLayout(self.btn_stream_end)
        self.btn_stream_end_layout.setSpacing(0)
        self.btn_stream_end_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_stream_end_layout.setObjectName(u"btn_stream_end_layout")

        self.page_2_layout.addWidget(self.btn_stream_end, 1, 1, 1, 1)

        self.pages.addWidget(self.page_stream)
        self.page_files = QWidget()
        self.page_files.setObjectName(u"page_files")
        self.page_3_layout = QGridLayout(self.page_files)
        self.page_3_layout.setSpacing(5)
        self.page_3_layout.setContentsMargins(5, 5, 5, 5)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.path_title_layout = QVBoxLayout()
        self.path_title_layout.setObjectName(u"path_title_layout")

        self.page_3_layout.addLayout(self.path_title_layout, 0, 0, 1, 6)

        self.path_line_edit_layout = QVBoxLayout()
        self.path_line_edit_layout.setObjectName(u"path_line_edit_layout")

        self.page_3_layout.addLayout(self.path_line_edit_layout, 1, 0, 1, 5)

        self.btn_path = QWidget(self.page_files)
        self.btn_path.setObjectName(u"btn_path")
        self.btn_path.setMinimumSize(QSize(0, 40))
        self.btn_path.setMaximumSize(QSize(16777215, 40))
        self.btn_path_layout = QVBoxLayout(self.btn_path)
        self.btn_path_layout.setSpacing(0)
        self.btn_path_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_path_layout.setObjectName(u"btn_path_layout")

        self.page_3_layout.addWidget(self.btn_path, 1, 5, 1, 1)

        self.label_files = QLabel(self.page_files)
        self.label_files.setObjectName(u"label_files")

        self.page_3_layout.addWidget(self.label_files, 2, 0, 1, 6)

        self.btn_files_start = QWidget(self.page_files)
        self.btn_files_start.setObjectName(u"btn_files_start")
        self.btn_files_start.setMinimumSize(QSize(0, 40))
        self.btn_files_start.setMaximumSize(QSize(16777215, 40))
        self.btn_files_start_layout = QVBoxLayout(self.btn_files_start)
        self.btn_files_start_layout.setSpacing(0)
        self.btn_files_start_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_files_start_layout.setObjectName(u"btn_files_start_layout")

        self.page_3_layout.addWidget(self.btn_files_start, 3, 0, 1, 3)

        self.btn_files_end = QWidget(self.page_files)
        self.btn_files_end.setObjectName(u"btn_files_end")
        self.btn_files_end.setMinimumSize(QSize(0, 40))
        self.btn_files_end.setMaximumSize(QSize(16777215, 40))
        self.btn_files_end_layout = QVBoxLayout(self.btn_files_end)
        self.btn_files_end_layout.setSpacing(0)
        self.btn_files_end_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_files_end_layout.setObjectName(u"btn_files_end_layout")

        self.page_3_layout.addWidget(self.btn_files_end, 3, 3, 1, 3)

        self.pages.addWidget(self.page_files)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcom to Fall Detection System", None))
        self.label_stream.setText("")
        self.label_files.setText("")
    # retranslateUi

