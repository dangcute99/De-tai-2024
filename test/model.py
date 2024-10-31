# model.py
import os
import json


class UserModel:
    def __init__(self):
        self.login_config_file_path = 'login_config.json'
        self.create_config_file()

    def create_config_file(self):
        if not os.path.exists(self.login_config_file_path):
            with open(self.login_config_file_path, 'w') as config_file:
                json.dump({"username": "", "password": "",
                          "checkbox": "0"}, config_file)

    def check_login(self, username, password):
        # Thay đổi logic kiểm tra thông tin đăng nhập ở đây
        # Ví dụ đơn giản:
        return username == "admin" and password == "password"
