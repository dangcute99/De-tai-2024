from PyQt6 import QtCore, QtGui, QtWidgets
from model import Model
from view import View
import os
import json


class Controller():
    def __init__(self, main_window):  # , main_window
        super().__init__()
        self.sql_login_window = None
        self.login_config_file_path = 'login_config.json'
        self.sql_config_file_path = 'sql_config.json'
        self.my_view = View()
        # Thiết lập UI cho View với đối tượng main_window
        self.my_view.ui.setupUi(main_window)
        self.my_view.ui.connect_login_button(self.handle_login)
        self.my_view.ui.connect_sql_setting_button(self.on_sql_setting_clicked)
        self.create_config_file()
        # self.load_login_data()
        self.my_view.ui.connect_load_login_info(self.load_login_in4())

    def handle_login(self):
        self.save_checkbox()
        in_4 = self.load_sql_login_in4()
        print(in_4)
        self.my_model = Model(in_4)
        if (self.my_model.check_connection()):
            self.my_view.ui.return_sql_status(True)
        else:
            self.my_view.ui.return_sql_status(False)

    def check_sql_connection(self):
        self.my_model.check_sql_connection()

    def save_checkbox(self):
        self.checkbox_status = self.my_view.ui.check_checkbox_status()
        data = self.my_view.ui.ruturn_login_in4()
        with open(self.login_config_file_path, 'r') as file:
            login_data = json.load(file)
        if (self.checkbox_status):
            # print("true")
            login_data["username"] = data["username"]
            login_data["password"] = data["password"]
            login_data["checkbox"] = 1
        else:
            login_data["checkbox"] = 0
            # print("false")
        with open(self.login_config_file_path, 'w') as config_file:
            json.dump(login_data, config_file)

    def load_login_in4(self):
        try:
            with open(self.login_config_file_path, 'r') as file:
                # Đọc và chuyển đổi nội dung tệp JSON thành dictionary
                login_data = json.load(file)
                return login_data
        except FileNotFoundError:
            print("Tệp cấu hình không tìm thấy.")
            return None
        except json.JSONDecodeError:
            print("Lỗi khi phân tích cú pháp JSON.")
            return None

    def sql_enter_button(self):
        sql_login_data = self.my_view.sql_login.get_sql_data()
        with open(self.sql_config_file_path, 'w') as config_file:
            json.dump(sql_login_data, config_file)
        self.sql_login_window.close()

    def on_sql_setting_clicked(self):
        # Kiểm tra xem cửa sổ SQL login đã mở chưa
        if self.sql_login_window is None or not self.sql_login_window.isVisible():
            self.sql_login_window = QtWidgets.QMainWindow()
            ui_sql_login = self.my_view.sql_login
            ui_sql_login.setupUi(self.sql_login_window)
            self.sql_login_window.show()
            self.my_view.sql_login.connect_enter_button(
                self.sql_enter_button)
        else:
            self.sql_login_window.close()  # Đóng cửa sổ nếu nó đã mở
        self.my_view.sql_login.load_sql_data(self.load_sql_login_in4())

    def load_sql_login_in4(self):
        with open(self.sql_config_file_path, 'r') as file:
            # Đọc và chuyển đổi nội dung tệp JSON thành dictionary
            sql_login_data = json.load(file)
            return sql_login_data

    def create_config_file(self):
        if not os.path.exists(self.login_config_file_path):
            with open(self.login_config_file_path, 'w') as config_file:
                json.dump({"username": "", "password": "",
                          "checkbox": "0"}, config_file)
        if not os.path.exists(self.sql_config_file_path):
            with open(self.sql_config_file_path, 'w') as config_file:
                json.dump({"host": "localhost", "username": "123",
                          "password": "992002"}, config_file)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    API = QtWidgets.QMainWindow()  # Tạo một đối tượng QMainWindow
    ct = Controller(API)  # Khởi tạo Controller và truyền QMainWindow vào

    API.show()  # Gọi show() trên QMainWindow

    sys.exit(app.exec())
