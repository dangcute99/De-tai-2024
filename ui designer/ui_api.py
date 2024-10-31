# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apiIHPoEb.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import anh_rc

class Ui_API(object):
    def setupUi(self, API):
        if API.objectName():
            API.setObjectName(u"API")
        API.resize(905, 376)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(API.sizePolicy().hasHeightForWidth())
        API.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(6)
        API.setFont(font)
        API.setFocusPolicy(Qt.NoFocus)
        API.setContextMenuPolicy(Qt.CustomContextMenu)
        API.setLayoutDirection(Qt.RightToLeft)
        API.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        API.setToolButtonStyle(Qt.ToolButtonIconOnly)
        API.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(API)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(210, 0, 691, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dong_1 = QLabel(self.verticalLayoutWidget)
        self.dong_1.setObjectName(u"dong_1")
        font1 = QFont()
        font1.setFamily(u"Times")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.dong_1.setFont(font1)
        self.dong_1.setLayoutDirection(Qt.LeftToRight)
        self.dong_1.setStyleSheet(u" color: rgb(45, 38, 255)")
        self.dong_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dong_1)

        self.dong_2 = QLabel(self.verticalLayoutWidget)
        self.dong_2.setObjectName(u"dong_2")
        font2 = QFont()
        font2.setFamily(u"Times")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.dong_2.setFont(font2)
        self.dong_2.setStyleSheet(u" color: rgb(255, 64, 16)")
        self.dong_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dong_2)

        self.anh_bc = QLabel(self.centralwidget)
        self.anh_bc.setObjectName(u"anh_bc")
        self.anh_bc.setGeometry(QRect(10, 0, 190, 190))
        self.anh_bc.setPixmap(QPixmap(u":/pic/anh.png"))
        self.anh_bc.setScaledContents(True)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(200, 80, 691, 231))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.dong_5 = QLabel(self.gridLayoutWidget)
        self.dong_5.setObjectName(u"dong_5")
        font3 = QFont()
        font3.setPointSize(10)
        self.dong_5.setFont(font3)
        self.dong_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.dong_5, 6, 3, 1, 1)

        self.taikhoan = QLineEdit(self.gridLayoutWidget)
        self.taikhoan.setObjectName(u"taikhoan")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.taikhoan.sizePolicy().hasHeightForWidth())
        self.taikhoan.setSizePolicy(sizePolicy1)
        self.taikhoan.setMinimumSize(QSize(300, 25))
        self.taikhoan.setMaximumSize(QSize(300, 25))
        self.taikhoan.setFont(font3)
        self.taikhoan.setAcceptDrops(True)
        self.taikhoan.setStyleSheet(u"")

        self.gridLayout.addWidget(self.taikhoan, 5, 2, 1, 1)

        self.login_button = QPushButton(self.gridLayoutWidget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setFont(font3)
        self.login_button.setFocusPolicy(Qt.WheelFocus)
        self.login_button.setLayoutDirection(Qt.RightToLeft)
        self.login_button.setStyleSheet(u"QPushButton {\n"
"        color: rgb(0,0,0);\n"
"        background-color: rgb(250,250,250);\n"
"        border: 1px solid black;\n"
"        border-radius: 10px; \n"
"        padding: 5px;  \n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(0,212,255,0.5); \n"
"        \n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(0,212,255,1);\n"
"    }")
        self.login_button.setCheckable(False)

        self.gridLayout.addWidget(self.login_button, 8, 2, 1, 1)

        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font3)
        self.checkBox.setLayoutDirection(Qt.LeftToRight)
        self.checkBox.setStyleSheet(u"  QCheckBox {\n"
"        color: rgb(0,0,0);  \n"
"    }\n"
"    QCheckBox::indicator {\n"
"        width: 12px;\n"
"        height: 12px;\n"
"        border-radius:5px;\n"
"    }\n"
"    QCheckBox::indicator:unchecked {\n"
"        background-color: white;  \n"
"        border: 1px solid black;\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"        background-color: blue;\n"
"        border: 1px solid black;\n"
"    }")

        self.gridLayout.addWidget(self.checkBox, 7, 2, 1, 1)

        self.dong_4 = QLabel(self.gridLayoutWidget)
        self.dong_4.setObjectName(u"dong_4")
        self.dong_4.setFont(font3)
        self.dong_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.dong_4, 5, 3, 1, 1)

        self.taikhoan1_2 = QLineEdit(self.gridLayoutWidget)
        self.taikhoan1_2.setObjectName(u"taikhoan1_2")
        sizePolicy1.setHeightForWidth(self.taikhoan1_2.sizePolicy().hasHeightForWidth())
        self.taikhoan1_2.setSizePolicy(sizePolicy1)
        self.taikhoan1_2.setMinimumSize(QSize(300, 25))
        self.taikhoan1_2.setMaximumSize(QSize(300, 25))
        self.taikhoan1_2.setFont(font3)
        self.taikhoan1_2.setAcceptDrops(True)
        self.taikhoan1_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.taikhoan1_2, 6, 2, 1, 1)

        self.dong_3 = QLabel(self.gridLayoutWidget)
        self.dong_3.setObjectName(u"dong_3")
        self.dong_3.setMaximumSize(QSize(16777215, 48))
        self.dong_3.setSizeIncrement(QSize(20, 20))
        self.dong_3.setBaseSize(QSize(20, 40))
        font4 = QFont()
        font4.setFamily(u"Times")
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setWeight(75)
        self.dong_3.setFont(font4)
        self.dong_3.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.dong_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.dong_3, 4, 1, 1, 2)

        self.sql_setting = QPushButton(self.centralwidget)
        self.sql_setting.setObjectName(u"sql_setting")
        self.sql_setting.setGeometry(QRect(10, 330, 41, 41))
        font5 = QFont()
        font5.setFamily(u"dripicons-v2")
        font5.setPointSize(16)
        self.sql_setting.setFont(font5)
        self.sql_setting.setFocusPolicy(Qt.TabFocus)
        self.sql_setting.setContextMenuPolicy(Qt.CustomContextMenu)
        self.sql_setting.setStyleSheet(u"QPushButton \n"
"            {\n"
"            color: rgba(0,0,0,1);\n"
"            background-color: rgba(255,255,255,1);\n"
"            border-radius:20px;\n"
"            }\n"
"        QPushButton:hover\n"
"            {\n"
"            background-color:rgba(206,200,200,0.5); \n"
"            }\n"
"        QPushButton:pressed \n"
"            {\n"
"            background-color: rgba(206,200,200,1)\n"
"            }")
        self.sql_setting.setCheckable(False)
        self.sql_setting.setChecked(False)
        API.setCentralWidget(self.centralwidget)

        self.retranslateUi(API)

        QMetaObject.connectSlotsByName(API)
    # setupUi

    def retranslateUi(self, API):
        API.setWindowTitle(QCoreApplication.translate("API", u"MainWindow", None))
        self.dong_1.setText(QCoreApplication.translate("API", u"BINH CH\u1ee6NG TH\u00d4NG TIN LI\u00caN L\u1ea0C", None))
        self.dong_2.setText(QCoreApplication.translate("API", u"H\u1ec6 TH\u1ed0NG GI\u00c1M S\u00c1T, C\u1ea2NH B\u00c1O T\u1eea XA TR\u1ea0M TH\u00d4NG TIN", None))
        self.anh_bc.setText("")
        self.dong_5.setText(QCoreApplication.translate("API", u"M\u1eadt kh\u1ea9u:  ", None))
        self.taikhoan.setText("")
        self.taikhoan.setPlaceholderText(QCoreApplication.translate("API", u"Username", None))
        self.login_button.setText(QCoreApplication.translate("API", u"\u0110\u0103ng nh\u1eadp", None))
        self.checkBox.setText(QCoreApplication.translate("API", u"Nh\u1edb th\u00f4ng tin \u0111\u0103ng nh\u1eadp", None))
        self.dong_4.setText(QCoreApplication.translate("API", u"T\u00e0i kho\u1ea3n:  ", None))
        self.taikhoan1_2.setText("")
        self.taikhoan1_2.setPlaceholderText(QCoreApplication.translate("API", u"Passwords", None))
        self.dong_3.setText(QCoreApplication.translate("API", u"Th\u00f4ng tin \u0111\u0103ng nh\u1eadp                                  ", None))
        self.sql_setting.setText(QCoreApplication.translate("API", u"~", None))
    # retranslateUi

