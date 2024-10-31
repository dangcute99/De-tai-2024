# controller.py
from model import UserModel
from view import UserView
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
import sys


class UserController:
    def __init__(self):
        self.model = UserModel()
        self.view = UserView()
        self.view.connect_login_button(self.handle_login)

    def handle_login(self):
        print("Login button clicked")  # Dòng này sẽ in ra khi nút được nhấn
        username, password = self.view.get_login_info()
        self.view.clear_error()

        if self.model.check_login(username, password):
            self.view.display_success_message("Login successful!")
            self.switch_to_second_widget()
        else:
            self.view.display_error_message("Login failed!")

    def switch_to_second_widget(self):
        self.view.hide()  # Ẩn widget hiện tại
        self.second_widget = SecondWidget()  # Tạo widget mới
        self.second_widget.show()  # Hiển thị widget thứ hai


class SecondWidget(QWidget):  # Widget thứ hai
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")  # Tiêu đề cho widget mới
        layout = QVBoxLayout()
        label = QLabel("Welcome to the Dashboard!")  # Thông báo chào mừng
        layout.addWidget(label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = UserController().view
    main_window.show()
    sys.exit(app.exec())
