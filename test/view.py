# view.py
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class UserView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.error_label = QLabel()  # Thêm label để hiển thị thông báo lỗi

        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.error_label)

        self.setLayout(self.layout)

    def connect_login_button(self, slot):
        self.login_button.clicked.connect(slot)  # Kết nối nút với slot

    def get_login_info(self):
        # Trả về thông tin đăng nhập
        return self.username_input.text(), self.password_input.text()

    def clear_error(self):
        self.error_label.setText("")  # Xóa thông báo lỗi

    def display_error_message(self, message):
        self.error_label.setText(message)  # Hiển thị thông báo lỗi

    def display_success_message(self, message):
        # Có thể sử dụng cùng label để hiển thị thành công
        self.error_label.setText(message)
