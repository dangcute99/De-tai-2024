import sys
from PyQt6.QtWidgets import QApplication
from test import Ui_API


class MainApp(Ui_API):
    def __init__(self):
        super().__init__()
        self.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.taikhoan.text()
        password = self.taikhoan1_2.text()
        remember = self.checkBox.isChecked()

        print(f"Username: {username}, Password: {
              password}, Remember: {remember}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
