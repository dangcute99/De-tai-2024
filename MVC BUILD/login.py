
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
import json


class Ui_API(object):
    def setupUi(self, API):
        API.keyPressEvent = self.keyPressEvent
        API.setObjectName("API")
        API.setFixedSize(800, 376)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(API.sizePolicy().hasHeightForWidth())
        API.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(6)
        API.setFont(font)
        API.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        API.setContextMenuPolicy(
            QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        API.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        API.setStyleSheet("background-color:rgb(255, 255, 255)")
        API.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        API.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=API)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(
            parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(
            QtCore.QRect(160, 10, 691, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dong_1 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times")
        font.setPointSize(18)
        # font.setBold(True)
        font.setItalic(False)
        font.setWeight(95)
        self.dong_1.setFont(font)
        self.dong_1.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.dong_1.setStyleSheet(" color: rgb(45, 38, 255)")
        self.dong_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dong_1.setObjectName("dong_1")
        self.verticalLayout.addWidget(self.dong_1)
        self.dong_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.dong_2.setFont(font)
        self.dong_2.setStyleSheet(" color: rgb(255, 64, 16)")
        self.dong_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dong_2.setObjectName("dong_2")
        self.verticalLayout.addWidget(self.dong_2)
        self.dong_2_1 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.dong_2_1.setFont(font)
        self.dong_2_1.setStyleSheet(" color: rgb(255, 64, 16)")
        self.dong_2_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dong_2_1.setObjectName("dong_2_1")
        self.verticalLayout.addWidget(self.dong_2_1)
        self.anh_bc = QtWidgets.QLabel(parent=self.centralwidget)
        self.anh_bc.setGeometry(QtCore.QRect(5, 5, 190, 190))
        self.anh_bc.setText("")
        self.anh_bc.setPixmap(QtGui.QPixmap(
            "C:\\Users\\ASUS\\OneDrive\\My Computer\\ui\\MVC BUILD\\picture\\anh1.png"))
        self.anh_bc.setScaledContents(True)
        self.anh_bc.setObjectName("anh_bc")
        self.gridLayoutWidget = QtWidgets.QWidget(
            parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 90, 691, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.dong_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dong_5.setFont(font)
        self.dong_5.setStyleSheet(
            "color: rgb(0, 0, 0); ")

        self.dong_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                 QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dong_5.setObjectName("dong_5")
        self.gridLayout.addWidget(self.dong_5, 6, 3, 1, 1)
        self.taikhoan = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.taikhoan.sizePolicy().hasHeightForWidth())
        self.taikhoan.setSizePolicy(sizePolicy)
        self.taikhoan.setMinimumSize(QtCore.QSize(300, 25))
        self.taikhoan.setMaximumSize(QtCore.QSize(300, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.taikhoan.setFont(font)
        self.taikhoan.setAcceptDrops(True)
        self.taikhoan.setStyleSheet("color: rgb(0, 0, 0);")
        self.taikhoan.setText("")
        self.taikhoan.setObjectName("taikhoan")
        self.gridLayout.addWidget(self.taikhoan, 5, 2, 1, 1)
        self.taikhoan1_2 = QtWidgets.QLineEdit(
            parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.taikhoan1_2.sizePolicy().hasHeightForWidth())
        self.taikhoan1_2.setSizePolicy(sizePolicy)
        self.taikhoan1_2.setMinimumSize(QtCore.QSize(300, 25))
        self.taikhoan1_2.setMaximumSize(QtCore.QSize(300, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.taikhoan1_2.setFont(font)
        self.taikhoan1_2.setAcceptDrops(True)
        self.taikhoan1_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.taikhoan1_2.setText("")
        self.taikhoan1_2.setObjectName("taikhoan1_2")
        # self.taikhoan1_2.returnPressed.connect(self.on_login_clicked)
        self.login_button = QtWidgets.QPushButton(
            parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_button.setFont(font)
        self.login_button.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.login_button.setLayoutDirection(
            QtCore.Qt.LayoutDirection.RightToLeft)
        self.login_button.setStyleSheet("QPushButton {\n"
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
        self.login_button.setObjectName("login_button")
        # Thêm dòng này để kết nối nút đăng nhập với hàm xử lý
        self.gridLayout.addWidget(self.login_button, 8, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.checkBox.setStyleSheet("  QCheckBox {\n"
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
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 7, 2, 1, 1)
        # Truy cập trạng thái widgets
        # self.checkBox.toggled.connect(self.remember_in4)
        self.dong_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dong_4.setFont(font)
        self.dong_4.setStyleSheet(
            "color: rgb(0, 0, 0); ")

        self.dong_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                 QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dong_4.setObjectName("dong_4")
        self.gridLayout.addWidget(self.dong_4, 5, 3, 1, 1)
        self.gridLayout.addWidget(self.taikhoan1_2, 6, 2, 1, 1)
        self.dong_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.dong_3.setMaximumSize(QtCore.QSize(16777215, 48))
        self.dong_3.setSizeIncrement(QtCore.QSize(20, 20))
        self.dong_3.setBaseSize(QtCore.QSize(20, 40))
        font = QtGui.QFont()
        font.setFamily("Times")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dong_3.setFont(font)
        self.dong_3.setStyleSheet("color: rgb(0, 0, 0); ")
        self.dong_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dong_3.setObjectName("dong_3")
        self.gridLayout.addWidget(self.dong_3, 4, 1, 1, 2)
        self.sql_setting = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sql_setting.setGeometry(QtCore.QRect(10, 330, 41, 41))
        font = QtGui.QFont()
        font.setFamily("dripicons-v2")
        font.setPointSize(16)
        self.sql_setting.setFont(font)
        self.sql_setting.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.sql_setting.setContextMenuPolicy(
            QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.sql_setting.setStyleSheet("QPushButton \n"
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
        self.sql_setting.setObjectName("sql_setting")
        # Thay đổi dòng này
        API.setCentralWidget(self.centralwidget)

        self.retranslateUi(API)
        QtCore.QMetaObject.connectSlotsByName(API)

    def retranslateUi(self, API):
        _translate = QtCore.QCoreApplication.translate
        API.setWindowTitle(_translate(
            "API", "Đăng nhập"))
        self.dong_1.setText(_translate(
            "API", "HỌC VIỆN KỸ THUẬT QUÂN SỰ"))
        self.dong_2.setText(_translate(
            "API", "HỆ THỐNG GIÁM SÁT, CẢNH BÁO VÀ ĐIỀU KHIỂN TỪ XA CHO"))
        self.dong_2_1.setText(_translate(
            "API", "TRẠM THÔNG TIN KỸ THUẬT SỐ"))
        self.dong_5.setText(_translate("API", "Mật khẩu:  "))
        self.taikhoan.setPlaceholderText(_translate("API", "Username"))
        self.login_button.setText(_translate("API", "Đăng nhập"))
        self.checkBox.setText(_translate("API", "Nhớ thông tin đăng nhập"))
        self.dong_4.setText(_translate("API", "Tài khoản:  "))
        self.taikhoan1_2.setPlaceholderText(_translate("API", "Passwords"))
        self.dong_3.setText(_translate(
            "API", "Thông tin đăng nhập                                  "))
        self.sql_setting.setText(_translate("API", "~"))
        # self.load_login_info()  # Tải thông tin khi khởi động

        # self.load_data()
    def connect_login_button(self, slot):
        self.enter_button_slot = slot
        self.login_button.clicked.connect(slot)  # Kết nối nút với slot

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            if hasattr(self, 'enter_button_slot'):
                self.enter_button_slot()

    def return_login_in4(self):
        data = {
            "username": self.taikhoan.text(),
            "password": self.taikhoan1_2.text()
        }
        return data

    def check_checkbox_status(self):
        if self.checkBox.isChecked():
            return True
        else:
            return False

    def connect_sql_setting_button(self, slot):
        self.sql_setting.clicked.connect(slot)

    def connect_load_login_info(self, login_data):
        # Kiểm tra giá trị của checkbox
        if login_data.get("checkbox") == 1:
            self.taikhoan.setText(login_data.get("username", ""))
            self.taikhoan1_2.setText(login_data.get("password", ""))
            self.checkBox.setChecked(True)  # Đánh dấu checkbox
        else:
            print("Checkbox is not checked (0). No username returned.")
            self.checkBox.setChecked(False)  # Bỏ đánh dấu checkbox

    def return_sql_status(self, status):
        if not status:
            QtWidgets.QMessageBox.critical(
                None, "Lỗi kết nối", "Kiểm trai lại tài khoản MySQL"
            )

    def return_login_status(self, status):
        if not status:
            QtWidgets.QMessageBox.critical(
                None, "Lỗi kết nối", "Kiểm trai lại thông tin đăng nhập"
            )
