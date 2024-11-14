import sys
import json
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Nạp giao diện từ file .ui đã tạo trong Qt Designer
        uic.loadUi(
            r"C:\Users\ASUS\OneDrive\My Computer\ui\MVC BUILD\main.ui", self)

        # Gọi hàm load style từ JSON
        self.load_json_style(
            r"C:\Users\ASUS\OneDrive\My Computer\ui\MVC BUILD\style.json")

    def load_json_style(self, json_file):
        """Nạp kiểu từ file JSON và áp dụng vào các widget tương ứng"""
        try:
            with open(json_file, "r") as file:
                styles = json.load(file)

            for widget_name, style_props in styles.items():
                widget = getattr(self, widget_name, None)
                if widget:
                    style_sheet = "; ".join(
                        [f"{key}: {value}" for key, value in style_props.items()])
                    widget.setStyleSheet(style_sheet)
                else:
                    print(f"Không tìm thấy widget: {widget_name}")
        except Exception as e:
            print(f"Lỗi khi nạp JSON style: {e}")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
