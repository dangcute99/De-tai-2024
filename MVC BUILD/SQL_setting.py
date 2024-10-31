from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFontDatabase
from PyQt6.QtCore import Qt, QPoint
import json
import os


def load_custom_font():
    try:
        font_path = os.path.abspath(
            "C:\\Users\\ASUS\\OneDrive\\My Computer\\ui\\MVC BUILD\\font\\dripicons-v2.ttf")
        print(f"Đường dẫn font: {font_path}")
        print(f"File tồn tại: {os.path.exists(font_path)}")

        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print(f"Không thể tải font. ID: {font_id}")
            return None
        else:
            font_families = QFontDatabase.applicationFontFamilies(font_id)
            if font_families:
                print(f"Font đã được tải: {font_families[0]}")
                return font_families[0]
        return None
    except Exception as e:
        print(f"Lỗi khi tải font: {str(e)}")
        return None


class Ui_SQL_login(object):
    def setupUi(self, SQL_login):
        # Kết nối sự kiện keyPressEvent cho SQL_login để lắng nghe phím bấm
        SQL_login.keyPressEvent = self.keyPressEvent
        SQL_login.setObjectName("SQL_login")
        SQL_login.resize(400, 415)
        SQL_login.setWindowFlags(
            Qt.WindowType.FramelessWindowHint)
        SQL_login.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(parent=SQL_login)

        # Thêm thuộc tính để lưu vị trí chuột
        self.oldPos = self.centralwidget.pos()

        # Kết nối sự kiện chuột với các phương thức xử lý
        self.centralwidget.mousePressEvent = self.mousePressEvent
        self.centralwidget.mouseMoveEvent = self.mouseMoveEvent

        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 30, 400, 380))
        self.frame.setStyleSheet("border-radius:30;\n"
                                 "background-color:rgba(75,188,255,1)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.dong_6 = QtWidgets.QLabel(parent=self.frame)
        self.dong_6.setGeometry(QtCore.QRect(20, 60, 361, 31))
        self.dong_6.setMaximumSize(QtCore.QSize(16777215, 48))
        self.dong_6.setSizeIncrement(QtCore.QSize(20, 20))
        self.dong_6.setBaseSize(QtCore.QSize(20, 40))
        font = QtGui.QFont()
        font.setFamily("Times")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dong_6.setFont(font)
        self.dong_6.setStyleSheet("color: rgb(0, 0, 0)")
        self.dong_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dong_6.setObjectName("dong_6")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.verticalLayoutWidget.setGeometry(
            QtCore.QRect(50, 110, 302, 210))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dong_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.dong_4.setMinimumSize(QtCore.QSize(90, 0))
        self.dong_4.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dong_4.setFont(font)
        self.dong_4.setStyleSheet("color:white\n"
                                  "")
        self.dong_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                 QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dong_4.setObjectName("dong_4")
        self.verticalLayout_2.addWidget(self.dong_4)
        self.taikhoan = QtWidgets.QLineEdit(
            parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.taikhoan.sizePolicy().hasHeightForWidth())
        self.taikhoan.setSizePolicy(sizePolicy)
        self.taikhoan.setMinimumSize(QtCore.QSize(300, 30))
        self.taikhoan.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.taikhoan.setFont(font)
        self.taikhoan.setAcceptDrops(True)
        self.taikhoan.setStyleSheet("color:rgba(0,0,0,1);\n"
                                    "background-color:white;\n"
                                    "border-radius:10px;\n"
                                    "border: 1px inset rgba(75,188,255,1);\n"
                                    "")
        self.taikhoan.setObjectName("taikhoan")
        self.verticalLayout_2.addWidget(self.taikhoan)
        self.dong_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.dong_7.setMinimumSize(QtCore.QSize(90, 0))
        self.dong_7.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dong_7.setFont(font)
        self.dong_7.setStyleSheet("color:white\n"
                                  "")
        self.dong_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                 QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dong_7.setObjectName("dong_7")
        self.verticalLayout_2.addWidget(self.dong_7)
        self.taikhoan_2 = QtWidgets.QLineEdit(
            parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.taikhoan_2.sizePolicy().hasHeightForWidth())
        self.taikhoan_2.setSizePolicy(sizePolicy)
        self.taikhoan_2.setMinimumSize(QtCore.QSize(300, 30))
        self.taikhoan_2.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.taikhoan_2.setFont(font)
        self.taikhoan_2.setAcceptDrops(True)
        self.taikhoan_2.setStyleSheet("color:rgba(0,0,0,1);\n"
                                      "background-color:white;\n"
                                      "border-radius:10px;\n"
                                      "border: 1px inset rgba(75,188,255,1);\n"
                                      "")
        self.taikhoan_2.setObjectName("taikhoan_2")
        self.verticalLayout_2.addWidget(self.taikhoan_2)
        self.dong_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.dong_5.setMinimumSize(QtCore.QSize(90, 0))
        self.dong_5.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dong_5.setFont(font)
        self.dong_5.setStyleSheet("color:white\n"
                                  "")
        self.dong_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                 QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dong_5.setObjectName("dong_5")
        self.verticalLayout_2.addWidget(self.dong_5)
        self.taikhoan1_2 = QtWidgets.QLineEdit(
            parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.taikhoan1_2.sizePolicy().hasHeightForWidth())
        self.taikhoan1_2.setSizePolicy(sizePolicy)
        self.taikhoan1_2.setMinimumSize(QtCore.QSize(300, 30))
        self.taikhoan1_2.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.taikhoan1_2.setFont(font)
        self.taikhoan1_2.setAcceptDrops(True)
        self.taikhoan1_2.setStyleSheet("color:rgba(0,0,0,1);\n"
                                       "background-color:white;\n"
                                       "border-radius:10px;\n"
                                       "border: 1px inset rgba(75,188,255,0.5);\n"
                                       "")
        self.taikhoan1_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.taikhoan1_2.setObjectName("taikhoan1_2")
        self.verticalLayout_2.addWidget(self.taikhoan1_2)
        self.login_button = QtWidgets.QPushButton(parent=self.frame)
        self.login_button.setGeometry(QtCore.QRect(50, 340, 300, 31))
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
                                        "        border-radius: 15px; \n"
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

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 80, 80))
        custom_font_name = load_custom_font()
        font = QtGui.QFont(custom_font_name, 20)
        self.label.setFont(font)

        self.label.setStyleSheet("border-radius:40;\n"
                                 "\n"
                                 "background-color:rgba(255,0,0,1)")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        SQL_login.setCentralWidget(self.centralwidget)

        self.retranslateUi(SQL_login)
        QtCore.QMetaObject.connectSlotsByName(SQL_login)

    def retranslateUi(self, SQL_login):
        _translate = QtCore.QCoreApplication.translate
        SQL_login.setWindowTitle(_translate("SQL_login", "MainWindow"))
        self.dong_6.setText(_translate(
            "SQL_login", "Thông tin tài khoản MySQL"))
        self.dong_4.setText(_translate("SQL_login", "Host"))
        self.taikhoan.setPlaceholderText(
            _translate("SQL_login", "Hostname"))
        self.dong_7.setText(_translate("SQL_login", "Username"))
        self.taikhoan_2.setPlaceholderText(
            _translate("SQL_login", "Username"))
        self.dong_5.setText(_translate("SQL_login", "Passwords"))
        self.taikhoan1_2.setPlaceholderText(
            self.login_button.setText(_translate("SQL_login", "Xác nhận")))
        self.label.setText(_translate("SQL_login", ""))

    # Thêm các phương thức xử lý sự kiện chuột

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
        self.centralwidget.window().move(self.centralwidget.window().x() + delta.x(),
                                         self.centralwidget.window().y() + delta.y())
        self.oldPos = event.globalPosition().toPoint()

    def load_sql_data(self, sql_data):
        self.taikhoan.setText(sql_data.get("host", ""))
        self.taikhoan_2.setText(sql_data.get("username", ""))
        self.taikhoan1_2.setText(sql_data.get("password", ""))

    def get_sql_data(self):
        data = {
            "host": self.taikhoan.text(),
            "username": self.taikhoan_2.text(),
            "password": self.taikhoan1_2.text()
        }
        return data
    # Trong file SQL_setting.py

    # def connect_enter_button(self, slot):
    #     if slot is None:
    #         print("Slot is None!")
    #     else:
    #         self.login_button.clicked.connect(slot)

    # def keyPressEvent(self, event):  # Thêm phương thức này
    #     if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
    #         self.close_connect_enter_button(slot)  # Gọi hàm close_window
    def connect_enter_button(self, slot):
        self.enter_button_slot = slot
        self.login_button.clicked.connect(slot)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            if hasattr(self, 'enter_button_slot'):
                self.enter_button_slot()
