from PyQt6.QtCore import QSize
import sys
import json
from PyQt6 import QtWidgets, uic, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Nạp giao diện từ file .ui đã tạo trong Qt Designer
        uic.loadUi(
            r"C:\Users\ASUS\OneDrive\My Computer\ui\ui designer\main.ui", self)

        # Gọi hàm load style từ JSON
        self.load_json_style(
            r"C:\Users\ASUS\OneDrive\My Computer\ui\MVC BUILD\style.json")
        self.stackedWidget.setCurrentWidget(self.page_1)
        # self.label.setPointSize(10)
        # Lấy tổng số trang
        # total_pages = self.stackedWidget.count()

        # # Lấy chỉ số của trang hiện tại
        # current_page = self.stackedWidget.currentIndex()
        # print(f"Current page: {current_page}")
        # print(f"Total pages: {total_pages}")
        # current_widget = self.stackedWidget.currentWidget()
        # print(f"Trang hiện tại là: {current_widget.objectName()}")
        # # Chuyển đến trang "page2"
        # self.stackedWidget.setCurrentWidget(self.page_2)
    def set_tentram(self, tentram):
        # Thiết lập tên cho các trạm
        for i in range(1, 17):  # Dùng 1 đến 16 vì có 16 trạm
            tram = getattr(self, f"tram_{i}", None)
            if tram and hasattr(tram, "setText"):
                tram.setText(tentram[i - 1])
                # tram.setEnabled(False)
                # tram.setDisabled(True)
                tram.setStyleSheet(
                    "color: black;font:bold; background: transparent; border: none;")

    def load_json_style(self, json_file):
        try:
            with open(json_file, "r") as file:
                styles = json.load(file)

            for widget_name, style_props in styles.items():
                widget = self.findChild(QtWidgets.QWidget, widget_name)
                if widget:
                    style_sheet = ""
                    font = QtGui.QFont()  # Tạo một QFont để áp dụng các thuộc tính font

                    for key, value in style_props.items():
                        if isinstance(value, dict):
                            # Xử lý các thuộc tính lồng nhau
                            if key == "maximum-size":
                                widget.setMaximumSize(
                                    QSize(value["width"], value["height"]))
                            elif key == "minimum-size":
                                widget.setMinimumSize(
                                    QSize(value["width"], value["height"]))
                            elif key == "font":
                                # Kiểm tra và thiết lập các thuộc tính font như size, family, weight
                                if "size" in value:
                                    font.setPointSize(value["size"])
                                if "family" in value:
                                    font.setFamily(value["family"])
                                if "weight" in value:
                                    if value["weight"].lower() == "bold":
                                        font.setBold(True)
                                    else:
                                        font.setBold(False)
                                widget.setFont(font)  # Áp dụng font cho widget
                        else:
                            # Áp dụng các thuộc tính CSS khác vào style_sheet
                            style_sheet += f"{key}: {value}; "

                    # Áp dụng style sheet cho widget
                    widget.setStyleSheet(style_sheet)

                else:
                    print(f"Widget not found: {widget_name}")

        except Exception as e:
            print(f"Error loading JSON style: {e}")

    def connect_anh_tram_1_button(self, slot):
        self.anhtram_1.clicked.connect(slot)

    def connect_anh_tram_2_button(self, slot):
        self.anhtram_2.clicked.connect(slot)

    def connect_anh_tram_3_button(self, slot):
        self.anhtram_3.clicked.connect(slot)

    def connect_anh_tram_4_button(self, slot):
        self.anhtram_4.clicked.connect(slot)

    def connect_anh_tram_5_button(self, slot):
        self.anhtram_5.clicked.connect(slot)

    def connect_home_button(self, slot):
        self.home_button.clicked.connect(slot)

    def connect_mute_button(self, slot):
        self.mute_button.clicked.connect(slot)

    def connect_in4_button(self, slot):
        self.in4_button.clicked.connect(slot)

    def connect_setting_button(self, slot):
        self.setting_button.clicked.connect(slot)

    def connect_temp_button(self, slot):
        self.temp_button.clicked.connect(slot)

    def connect_humi_button(self, slot):
        self.humi_button.clicked.connect(slot)

    def connect_error_button(self, slot):
        self.error_button.clicked.connect(slot)

    def connect_dc_button(self, slot):
        self.dc_button.clicked.connect(slot)

    def connect_chung_tram_button(self, slot):
        self.chung_tram.clicked.connect(slot)

    def switch_page(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def switch_ten_tram(self, name):
        self.ten_tram.setText(name)
        self.chung_tram.setText(name)

    # def plot_temp_value(self, value):

        # # @staticmethod
        # def main(self):
        #     app = QtWidgets.QApplication(sys.argv)
        #     window = MainWindow()
        #     window.show()
        #     sys.exit(app.exec())

        # # Gọi phương thức main từ bên ngoài lớp
        # if __name__ == "__main__":
        #     MainWindow.main()
