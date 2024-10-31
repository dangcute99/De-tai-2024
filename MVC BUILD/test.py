from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_API(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("API")
        self.setFixedSize(800, 376)
        self.setStyleSheet("background-color:rgb(255, 255, 255)")

        # Thiết lập layout và các label
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.setCentralWidget(self.centralwidget)

        self.verticalLayoutWidget = QtWidgets.QWidget(
            parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 10, 691, 80))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        # Tạo Label tiêu đề
        self.dong_1 = QtWidgets.QLabel(
            "HỌC VIỆN KỸ THUẬT QUÂN SỰ", parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times")
        font.setPointSize(18)
        self.dong_1.setFont(font)
        self.dong_1.setStyleSheet("color: rgb(45, 38, 255)")
        self.dong_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.dong_1)

        # Tạo ô nhập tài khoản
        self.taikhoan = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.taikhoan.setGeometry(QtCore.QRect(200, 100, 300, 25))
        self.taikhoan.setPlaceholderText("Username")

        # Tạo ô nhập mật khẩu
        self.taikhoan1_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.taikhoan1_2.setGeometry(QtCore.QRect(200, 150, 300, 25))
        self.taikhoan1_2.setPlaceholderText("Password")

        # Tạo nút đăng nhập
        self.login_button = QtWidgets.QPushButton(
            "Đăng nhập", parent=self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(200, 200, 100, 30))

        # Tạo checkbox
        self.checkBox = QtWidgets.QCheckBox(
            "Nhớ thông tin đăng nhập", parent=self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(200, 250, 200, 25))

        # Thiết lập tiêu đề
        self.setWindowTitle("Đăng nhập")
