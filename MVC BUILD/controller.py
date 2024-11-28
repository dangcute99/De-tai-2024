from PyQt6 import QtCore, QtGui, QtWidgets
from model import Model
from view import View
import os
import json
from datetime import datetime

tentram = ["Phòng 302", "Trạm BĐKT", "Trạm 3", "Trạm 4", "Trạm 5", "Trạm 6", "Trạm 7", "Trạm 8",
           "Trạm 9", "Trạm 10", "Trạm 11", "Trạm 12", "Trạm 13", "Trạm 14", "Trạm 15", "Trạm 16"]


class Controller():
    def __init__(self, open_window):  # , main_window
        super().__init__()
        self.sql_login_window = None
        self.open_window = open_window
        self.login_config_file_path = 'login_config.json'
        self.sql_config_file_path = 'sql_config.json'
        self.my_view = View()
        # Thiết lập UI cho View với đối tượng main_window
        self.my_view.ui.setupUi(open_window)
        self.my_view.ui.connect_login_button(self.handle_login)
        self.my_view.ui.connect_sql_setting_button(self.on_sql_setting_clicked)
        self.create_config_file()
        # self.load_login_data()
        self.my_view.ui.connect_load_login_info(self.load_login_in4())

        self.data_points = [
            (datetime(2024, 11, 1, 14, 30), 22),
            (datetime(2024, 11, 1, 14, 35), 12),
            (datetime(2024, 11, 1, 14, 37), 83),
            (datetime(2024, 11, 1, 14, 42), 50),
            (datetime(2024, 11, 1, 15, 45), 28),
            (datetime(2024, 11, 1, 15, 50), 26),
            (datetime(2024, 11, 1, 15, 56), 24),
            (datetime(2024, 11, 1, 16, 5), 62),
            (datetime(2024, 11, 1, 16, 10), 20),
            (datetime(2024, 11, 1, 16, 15), 12),
            (datetime(2024, 11, 1, 16, 20), 8),
            (datetime(2024, 11, 1, 16, 30), 35),
            (datetime(2024, 11, 1, 18, 40), 82),

        ]
        self.data_points_2 = [
            (datetime(2024, 11, 1, 11, 30), 22),
            (datetime(2024, 11, 1, 12, 35), 12),
            (datetime(2024, 11, 1, 13, 37), 25),
            (datetime(2024, 11, 1, 13, 42), 50),
            (datetime(2024, 11, 1, 13, 45), 28),
            (datetime(2024, 11, 1, 14, 50), 26),
            (datetime(2024, 11, 1, 14, 56), 24),
            (datetime(2024, 11, 1, 15, 5), 58),
            (datetime(2024, 11, 1, 16, 10), 20),
            (datetime(2024, 11, 1, 16, 15), 12),
            (datetime(2024, 11, 1, 16, 20), 50),
            (datetime(2024, 11, 1, 16, 30), 35),
            (datetime(2024, 11, 1, 17, 40), 90),

        ]
        self.temp_1 = 19
        self.temp_2 = 30
        self.humi_1 = 50
        self.humi_2 = 70
        self.dc_1 = 40
        self.dc_2 = 55
        self.dc_3 = 70
################################################################
# link với login

    def handle_login(self):
        self.save_checkbox()
        login_data = self.my_view.ui.return_login_in4()
        in_4 = self.load_sql_login_in4()
        self.my_model = Model(in_4)
        if not (self.my_model.check_connection()):
            self.my_view.ui.return_sql_status(False)
        else:
            if self.my_model.return_user_exists(login_data):
                print("Đăng nhập thành công")
                if self.sql_login_window and self.sql_login_window.isVisible():
                    self.sql_login_window.close()
                self.open_window.close()  # Close the main window
                self.open_main_window()

            else:
                self.my_view.ui.return_login_status(False)

        # return login_data
        # self.my_view.ui.return_login_status(True)

    def check_sql_connection(self):
        self.my_model.check_sql_connection()

    def save_checkbox(self):
        self.checkbox_status = self.my_view.ui.check_checkbox_status()
        data = self.my_view.ui.return_login_in4()
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
        return login_data

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
########################################################################
# link với sql_setting

    def load_sql_login_in4(self):
        with open(self.sql_config_file_path, 'r') as file:
            # Đọc và chuyển đổi nội dung tệp JSON thành dictionary
            sql_login_data = json.load(file)
            return sql_login_data
#######################################################################

    def create_config_file(self):
        if not os.path.exists(self.login_config_file_path):
            with open(self.login_config_file_path, 'w') as config_file:
                json.dump({"username": "", "password": "",
                          "checkbox": "0"}, config_file)
        if not os.path.exists(self.sql_config_file_path):
            with open(self.sql_config_file_path, 'w') as config_file:
                json.dump({"host": "localhost", "username": "123",
                          "password": "992002"}, config_file)
################################################################
# link với main_window

    def open_main_window(self):
        self.my_view.main.show()
        self.my_view.main.set_tentram(tentram)
        ################################################################
        self.my_view.main.connect_anh_tram_1_button(self.anh_tram_1_button)
        self.my_view.main.connect_anh_tram_2_button(self.anh_tram_2_button)
        self.my_view.main.connect_anh_tram_3_button(self.anh_tram_3_button)
        self.my_view.main.connect_anh_tram_4_button(self.anh_tram_4_button)
        self.my_view.main.connect_anh_tram_5_button(self.anh_tram_5_button)
        ################################################################
        self.my_view.main.connect_home_button(self.home_button)
        ########################################################################
        self.my_view.main.connect_temp_button(self.temp_button)
        self.my_view.main.connect_humi_button(self.humi_button)
        self.my_view.main.connect_dc_button(self.dc_button)
        self.my_view.main.connect_error_button(self.error_button)
        self.my_view.main.connect_chung_tram_button(self.chung_tram_button)

    ################################################################
    def anh_tram_1_button(self):
        if not self.my_view.main.tram.isVisible():
            self.my_view.main.tram.setVisible(True)
        self.my_view.main.switch_page(1)
        self.my_view.main.switch_ten_tram(tentram[0])
        self.my_view.main.hienthi.setCurrentIndex(0)

    def anh_tram_2_button(self):
        if not self.my_view.main.tram.isVisible():
            self.my_view.main.tram.setVisible(True)
        self.my_view.main.switch_page(1)
        self.my_view.main.switch_ten_tram(tentram[1])
        self.my_view.main.hienthi.setCurrentIndex(0)

    def anh_tram_3_button(self):
        print("anh tram 3")
        self.my_view.main.switch_page(1)
        self.my_view.main.switch_ten_tram(tentram[2])
        self.my_view.main.hienthi.setCurrentIndex(0)

    def anh_tram_4_button(self):
        print("anh tram 4")
        self.my_view.main.switch_page(1)
        self.my_view.main.switch_ten_tram(tentram[3])
        self.my_view.main.hienthi.setCurrentIndex(0)

    def anh_tram_5_button(self):
        print("anh tram 5")
        self.my_view.main.switch_page(1)
        self.my_view.main.switch_ten_tram(tentram[4])
        self.my_view.main.hienthi.setCurrentIndex(0)
    ################################################################

    def home_button(self):
        self.my_view.main.switch_page(0)

    def in4_button(self):
        # Kiểm tra trạng thái hiện tại của widget và đảo ngược nó
        if self.my_view.main.tram.isVisible():
            self.my_view.main.tram.setVisible(
                False)  # Ẩn widget nếu đang hiển thị
            self.my_view.main.hienthi.setCurrentIndex(5)
        else:
            self.my_view.main.tram.setVisible(
                True)   # Hiển thị widget nếu đang ẩn
    ################################################################

    def temp_button(self):
        self.my_view.main.hienthi.setCurrentIndex(1)
        self.my_view.main.ve_bieu_do_nhiet_do(
            self.data_points, self.data_points_2, self.temp_1, self.temp_2)

    def humi_button(self):
        self.my_view.main.hienthi.setCurrentIndex(2)
        self.my_view.main.ve_bieu_do_do_am(
            self.data_points_2, self.data_points, self.humi_1, self.humi_2)

    def dc_button(self):
        self.my_view.main.hienthi.setCurrentIndex(3)
        self.my_view.main.ve_bieu_do_dc(
            self.data_points, self.data_points_2, self.dc_1, self.dc_2, self.dc_3)

    def error_button(self):
        self.my_view.main.hienthi.setCurrentIndex(4)

    def chung_tram_button(self):
        self.my_view.main.hienthi.setCurrentIndex(0)
################################################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    API = QtWidgets.QMainWindow()  # Tạo một đối tượng QMainWindow
    ct = Controller(API)  # Khởi tạo Controller và truyền QMainWindow vào

    API.show()  # Gọi show() trên QMainWindow

    sys.exit(app.exec())
