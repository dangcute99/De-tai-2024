from PyQt6 import QtCore, QtGui, QtWidgets
from login import Ui_API  # Đảm bảo bạn đã import Ui_API từ file api.py
from SQL_setting import Ui_SQL_login
from main import MainWindow
import json  # Thêm import json


class View():
    def __init__(self):
        import sys
        # app = QtWidgets.QApplication(sys.argv)
        # API = QtWidgets.QMainWindow()
        self.ui = Ui_API()
        # self.ui.setupUi(API)
        self.sql_login = Ui_SQL_login()
        self.main = MainWindow()

    # def load_data(self):
    #      return self.config
