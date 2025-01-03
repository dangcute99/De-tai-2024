from PyQt6.QtCore import QSize
from PyQt6 import QtCore
import sys
import os
import json
from PyQt6 import QtWidgets, uic, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QSizePolicy
import matplotlib.dates as mdates
from PyQt6.QtCore import QTimer, QDateTime


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Nạp giao diện từ file .ui đã tạo trong Qt Designer
        ui_path = resource_path("ui designer/main.ui")
        uic.loadUi(ui_path, self)

        # Gọi hàm load style từ JSON
        json_path = resource_path("MVC BUILD/style.json")
        self.load_json_style(json_path)
        self.stackedWidget.setCurrentWidget(self.page_1)
        self.setting_ui()

        self.temp_chart_bit = False
        self.humi_chart_bit = False
        self.dc_chart_bit = False
        # tạo nút HDSD động
        self.in4_button = self.create_draggable_button(
            "", "Hướng dẫn sử dụng!", self)
        self.in4_button.move(1350, 750)

        # Tạo QTimer để cập nhật thời gian
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Cập nhật mỗi 1000ms (1 giây)
        # Hiển thị thời gian ngay khi khởi động
        self.update_time()

    def setting_ui(self):
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setSingleStep(0.5)
        self.doubleSpinBox.setSuffix(" %")
        ################################################################
        self.doubleSpinBox_7.setDecimals(1)
        self.doubleSpinBox_7.setSingleStep(0.5)
        self.doubleSpinBox_7.setSuffix(" %")
        ################################################################
        self.doubleSpinBox_2.setDecimals(1)
        self.doubleSpinBox_2.setSingleStep(0.5)
        self.doubleSpinBox_2.setSuffix(" %")
        ################################################################
        self.doubleSpinBox_6.setDecimals(1)
        self.doubleSpinBox_6.setSingleStep(0.5)
        self.doubleSpinBox_6.setSuffix(" %")
        ################################################################
        ################################################################
        self.doubleSpinBox_3.setDecimals(1)
        self.doubleSpinBox_3.setSingleStep(0.5)
        self.doubleSpinBox_3.setSuffix(" V")
        ################################################################
        self.doubleSpinBox_4.setDecimals(1)
        self.doubleSpinBox_4.setSingleStep(0.5)
        self.doubleSpinBox_4.setSuffix(" V")
        ################################################################
        self.doubleSpinBox_5.setDecimals(1)
        self.doubleSpinBox_5.setSingleStep(0.5)
        self.doubleSpinBox_5.setSuffix(" V")
        ################################################################
        self.doubleSpinBox_8.setDecimals(0)
        self.doubleSpinBox_8.setSuffix("°C")
        ################################################################
        # self.checkBox.setStyleSheet("  QCheckBox {\n"
        #                             "        color: rgb(0,0,0);  \n"
        #                             "    }\n"
        #                             "    QCheckBox::indicator {\n"
        #                             "        width: 12px;\n"
        #                             "        height: 12px;\n"
        #                             "        border-radius:6px;\n"
        #                             "    }\n"
        #                             "    QCheckBox::indicator:unchecked {\n"
        #                             "        background-color: white;  \n"
        #                             "        border: 1px solid black;\n"
        #                             "    }\n"
        #                             "    QCheckBox::indicator:checked {\n"
        #                             "        background-color: blue;\n"
        #                             "        border: 1px solid black;\n"
        #                             "    }")

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

    # def load_json_style(self, json_file):
    #     try:
    #         with open(json_file, "r") as file:
    #             styles = json.load(file)

    #         for widget_name, style_props in styles.items():
    #             widget = self.findChild(QtWidgets.QWidget, widget_name)
    #             if widget:
    #                 style_sheet = ""
    #                 font = QtGui.QFont()  # Tạo một QFont để áp dụng các thuộc tính font

    #                 for key, value in style_props.items():
    #                     if isinstance(value, dict):
    #                         # Xử lý các thuộc tính lồng nhau
    #                         if key == "maximum-size":
    #                             widget.setMaximumSize(
    #                                 QSize(value["width"], value["height"]))
    #                         elif key == "minimum-size":
    #                             widget.setMinimumSize(
    #                                 QSize(value["width"], value["height"]))
    #                         elif key == "font":
    #                             # Kiểm tra và thiết lập các thuộc tính font như size, family, weight
    #                             if "size" in value:
    #                                 font.setPointSize(value["size"])
    #                             if "family" in value:
    #                                 font.setFamily(value["family"])
    #                             if "weight" in value:
    #                                 if value["weight"].lower() == "bold":
    #                                     font.setBold(True)
    #                                 else:
    #                                     font.setBold(False)
    #                             widget.setFont(font)  # Áp dụng font cho widget
    #                     else:
    #                         # Áp dụng các thuộc tính CSS khác vào style_sheet
    #                         style_sheet += f"{key}: {value}; "

    #                 # Áp dụng style sheet cho widget
    #                 widget.setStyleSheet(style_sheet)

    #             else:
    #                 print(f"Widget not found: {widget_name}")

    #     except Exception as e:
    #         print(f"Error loading JSON style: {e}")
    def load_json_style(self, json_file):
        """
        Load và áp dụng style từ file JSON cho các widget
        json_file: đường dẫn đến file JSON chứa style
        """
        try:
            # Đọc file JSON
            with open(json_file, "r", encoding='utf-8') as file:
                styles = json.load(file)

            # Xử lý style cho từng widget
            for widget_name, style_props in styles.items():
                # Tìm widget theo tên
                widget = self.findChild(QtWidgets.QWidget, widget_name)
                if not widget:
                    print(f"Widget không tìm thấy: {widget_name}")
                    continue

                # Xử lý các thuộc tính cơ bản của widget (font, size)
                font = QtGui.QFont()
                has_font = False

                full_style = ""
                for prop, value in style_props.items():
                    if isinstance(value, dict):
                        # Xử lý font
                        if prop == "font":
                            if "family" in value:
                                font.setFamily(value["family"])
                            if "size" in value:
                                font.setPointSize(value["size"])
                            if "weight" in value:
                                if value["weight"].lower() == "bold":
                                    font.setBold(True)
                                elif value["weight"].lower() == "normal":
                                    font.setBold(False)
                            if "italic" in value:
                                font.setItalic(value["italic"])
                            has_font = True

                        # Xử lý size
                        elif prop == "size":
                            if "fixed" in value:
                                if "width" in value["fixed"] and "height" in value["fixed"]:
                                    widget.setFixedSize(
                                        value["fixed"]["width"], value["fixed"]["height"])
                            if "minimum" in value:
                                if "width" in value["minimum"] and "height" in value["minimum"]:
                                    widget.setMinimumSize(
                                        value["minimum"]["width"], value["minimum"]["height"])
                            if "maximum" in value:
                                if "width" in value["maximum"] and "height" in value["maximum"]:
                                    widget.setMaximumSize(
                                        value["maximum"]["width"], value["maximum"]["height"])

                        # Xử lý style
                        elif prop == "style":
                            # Duyệt qua từng widget type trong style
                            for widget_type, widget_style in value.items():
                                style_str = ""
                                states_style = {}
                                sub_controls = {}

                                # Xử lý từng thuộc tính style
                                for key, val in widget_style.items():
                                    if isinstance(val, dict):
                                        # Xử lý các trạng thái đặc biệt
                                        if key in ["hover", "pressed", "checked", "unchecked", "selected", "focus"]:
                                            states_str = ""
                                            for k, v in val.items():
                                                states_str += f"{k}: {v};\n"
                                            states_style[key] = states_str

                                        # Xử lý các sub-controls
                                        elif key in ["indicator", "handle", "add-line", "sub-line", "up-arrow", "down-arrow"]:
                                            sub_str = ""
                                            for k, v in val.items():
                                                sub_str += f"{k}: {v};\n"
                                            sub_controls[key] = sub_str

                                        # Xử lý các thuộc tính lồng nhau khác
                                        else:
                                            nested_str = ""
                                            for k, v in val.items():
                                                nested_str += f"{k}: {v};\n"
                                            style_str += f"{key} {{\n{nested_str}}}\n"
                                    else:
                                        style_str += f"{key}: {val};\n"

                                # Tạo style string hoàn chỉnh
                                full_style += f"{widget_type} {{\n{style_str}}}\n"

                                # Thêm các trạng thái
                                for state, state_style in states_style.items():
                                    full_style += f"{widget_type}:{
                                        state} {{\n{state_style}}}\n"

                                # Thêm các sub-controls
                                for control, control_style in sub_controls.items():
                                    full_style += f"{widget_type}::{
                                        control} {{\n{control_style}}}\n"

                # Áp dụng font nếu có
                if has_font:
                    widget.setFont(font)

                # Áp dụng style sheet
                if full_style:
                    widget.setStyleSheet(full_style)

        except Exception as e:
            print(f"Lỗi khi load JSON style: {e}")

    def update_time(self):
        # Lấy thời gian hiện tại
        current_time = QDateTime.currentDateTime()

        # Tạo chuỗi thời gian (giờ:phút:giây)
        time_str = current_time.toString("HH:mm:ss")

        # Tạo chuỗi ngày tháng năm
        date_str = current_time.toString("dd/MM/yyyy")

        # Cập nhật nội dung cho QLabel (thời gian ở trên, ngày tháng ở dưới)
        self.time_label.setText(f"{time_str}\n{date_str}")

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

    def ve_bieu_do_nhiet_do(self, data_points, data_points_2, temp_1, temp_2):
        if not self.temp_chart_bit:  # Kiểm tra cờ
            self.stackedWidget.setCurrentWidget(self.page_2)
            self.plot_temperature_chart_in_widget(
                data_points, data_points_2, temp_1, temp_2)
            self.temp_chart_bit = True  # Đặt cờ thành True sau khi vẽ
        else:
            print("Biểu đồ nhiet do đã được vẽ trước đó, không cần vẽ lại.")

    def ve_bieu_do_do_am(self, data_points, data_points_2, humi_1, humi_2):
        if not self.humi_chart_bit:  # Kiểm tra cờ
            self.stackedWidget.setCurrentWidget(self.page_2)
            self.plot_humidity_chart_in_widget(
                data_points, data_points_2, humi_1, humi_2)
            self.humi_chart_bit = True  # Đặt cờ thành True sau khi vẽ
        else:
            print("Biểu đồ độ ẩm đã được vẽ trước đó, không cần vẽ lại.")

    def ve_bieu_do_dc(self, data_points, data_points_2, dc_1, dc_2, dc_3):
        if not self.dc_chart_bit:  # Kiểm tra cờ
            self.stackedWidget.setCurrentWidget(self.page_2)
            self.plot_voltage_chart_in_widget(
                data_points, data_points_2, dc_1, dc_2, dc_3)
            self.dc_chart_bit = True  # Đặt cờ thành True sau khi vẽ
        else:
            print("Biểu đồ điện áp DC đã được vẽ trước đó, không cần vẽ lại.")

    def plot_temperature_chart_in_widget(self, data_points, data_points_2, temp_1, temp_2):
        """
        Vẽ biểu đồ nhiệt độ với tooltip thông minh tự động điều chỉnh vị trí
        """
        parent_widget = self.temp_chart
        figure, ax = plt.subplots(figsize=(12, 6))

        # Tách ngày giờ và nhiệt độ từ hai tập dữ liệu
        dates_1, temperatures_1 = zip(*data_points)
        dates_2, temperatures_2 = zip(*data_points_2)

        # Vẽ đường nhiệt độ chính (đường 1)
        ax.plot(dates_1, temperatures_1, color='#0088FF',
                linestyle='-', linewidth=1, label="Đường nhiệt độ 1")

        # Vẽ đường nhiệt độ thứ hai (đường 2)
        ax.plot(dates_2, temperatures_2, color='#FF6347',
                linestyle='-', linewidth=1, label="Đường nhiệt độ 2")

        # Vẽ các điểm dữ liệu và đường kẻ dọc cho đường 1
        for date, temp in data_points:
            color = 'red' if temp > temp_2 or temp < temp_1 else '#00FF00'
            ax.scatter(date, temp, color=color, s=50)
            ax.plot([date, date], [0, temp], color='gray',
                    linestyle='-', linewidth=0.5, alpha=0.3)

        # Vẽ các điểm dữ liệu và đường kẻ dọc cho đường 2
        for date, temp in data_points_2:
            color = 'red' if temp > temp_2 or temp < temp_1 else '#00FF00'
            ax.scatter(date, temp, color=color, s=50)
            ax.plot([date, date], [0, temp], color='gray',
                    linestyle='--', linewidth=0.5, alpha=0.3)

        # Vẽ các đường ngưỡng
        ax.axhline(y=temp_1, color='#35ff00', linestyle='--',
                   linewidth=1, label=f"Ngưỡng {temp_1}°C")
        ax.axhline(y=temp_2, color='#f600ff', linestyle='-.',
                   linewidth=1, label=f"Ngưỡng {temp_2}°C")

        # Định dạng trục thời gian
        time_format = mdates.DateFormatter("%H:%M")
        ax.xaxis.set_major_formatter(time_format)
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())

        # Thiết lập nhãn trục và tiêu đề
        ax.set_xlabel("Thời gian", fontsize=10)
        ax.xaxis.set_label_coords(0.95, -0.05)
        ax.set_ylabel("Nhiệt độ (°C)", fontsize=10)
        ax.yaxis.set_label_coords(-0.03, 0.9)
        figure.text(0.5, 0.1, "Biểu đồ nhiệt độ", fontsize=14,
                    ha='center', fontweight='bold')
        ax.legend(loc='best')
        ax.grid(False)

        # Tối ưu layout
        plt.tight_layout()
        figure.autofmt_xdate()

        # Tạo canvas và thêm vào widget
        canvas = FigureCanvas(figure)
        layout = parent_widget.layout()
        if not layout:
            layout = QtWidgets.QVBoxLayout(parent_widget)
            parent_widget.setLayout(layout)
        layout.addWidget(canvas)

        # Tạo annotation cho tooltip
        annot = ax.annotate(
            "",
            xy=(0, 0),
            xytext=(0, 0),
            textcoords="offset points",
            bbox=dict(
                boxstyle="round4,pad=0.5",
                fc="white",
                ec="gray",
                alpha=0.9,
                mutation_scale=0.8
            ),
            arrowprops=dict(
                arrowstyle="-|>",
                connectionstyle="arc3,rad=0.2",
                color='gray'
            )
        )
        annot.set_visible(False)

        def get_smart_offset(date, temp, ax_bbox):
            """
            Tính toán offset thông minh cho tooltip dựa trên vị trí của điểm và kích thước của đồ thị
            """
            x_rel = (mdates.date2num(date) - ax.get_xlim()
                     [0]) / (ax.get_xlim()[1] - ax.get_xlim()[0])
            y_rel = (temp - ax.get_ylim()[0]) / \
                (ax.get_ylim()[1] - ax.get_ylim()[0])

            # Offset mặc định
            x_offset = 10
            y_offset = 10

            # Điều chỉnh theo vị trí tương đối
            if x_rel > 0.8:  # Gần mép phải
                x_offset = -80
            elif x_rel < 0.2:  # Gần mép trái
                x_offset = 20

            if y_rel > 0.8:  # Gần mép trên
                y_offset = -40
            elif y_rel < 0.2:  # Gần mép dưới
                y_offset = 20

            return x_offset, y_offset

        def on_hover(event):
            if event.inaxes == ax:
                hit = False
                for idx, (date, temp) in enumerate(data_points + data_points_2):
                    # Kiểm tra điểm thuộc đường 1 hay đường 2
                    is_first_dataset = idx < len(data_points)
                    dataset_label = "Đường 1" if is_first_dataset else "Đường 2"

                    # Tăng độ nhạy của vùng hover
                    if abs(event.xdata - mdates.date2num(date)) <= 0.001 and abs(event.ydata - temp) <= 1:
                        hit = True
                        # Lấy offset thông minh
                        x_offset, y_offset = get_smart_offset(
                            date, temp, ax.bbox)

                        # Cập nhật vị trí và thuộc tính của tooltip
                        annot.xy = (mdates.date2num(date), temp)
                        annot.set_position((x_offset, y_offset))

                        # Định dạng nội dung tooltip
                        tooltip_text = (
                            f"{dataset_label}\n"
                            f"Ngày: {date.strftime('%d/%m/%Y')}\n"
                            f"Thời gian: {date.strftime('%H:%M')}\n"
                            f"Nhiệt độ: {temp}°C"
                        )
                        if temp > temp_2:
                            tooltip_text += "\n⚠️ Nhiệt độ cao"
                        elif temp < temp_1:
                            tooltip_text += "\n⚠️ Nhiệt độ thấp"

                        annot.set_text(tooltip_text)

                        # Đổi màu tooltip theo trạng thái nhiệt độ
                        if temp > temp_2 or temp < temp_1:
                            annot.get_bbox_patch().set(fc="#F01F1F")
                        else:
                            annot.get_bbox_patch().set(fc="#00FF00")

                        annot.set_visible(True)
                        canvas.draw_idle()
                        break

                if not hit and annot.get_visible():
                    annot.set_visible(False)
                    canvas.draw_idle()

        canvas.mpl_connect("motion_notify_event", on_hover)
        canvas.setSizePolicy(QSizePolicy.Policy.Expanding,
                             QSizePolicy.Policy.Expanding)

    def create_draggable_button(self, name, tooltips, parent=None):
        button = QtWidgets.QPushButton(name, parent)
        button.setFixedSize(30, 30)
        button.setStyleSheet("""
            QPushButton {
                background-color: rgba(0,246,255,1);
                border-radius: 15px;
                color: black;
                             font-family: dripicons-v2;
                             font-size: 30px;
            }
            QPushButton:hover {
                background-color: skyblue;
            }
        """)

        button._drag_active = False
        button._drag_start_position = None

        # Hiển thị tooltip khi chuột vào nút
        def enterEvent(event):
            QtWidgets.QToolTip.showText(
                button.mapToGlobal(QtCore.QPoint(
                    button.width() // 2, button.height() // 2)),
                tooltips
            )
            super(QtWidgets.QPushButton, button).enterEvent(event)

        def leaveEvent(event):
            QtWidgets.QToolTip.hideText()
            super(QtWidgets.QPushButton, button).leaveEvent(event)

        # Xử lý sự kiện bắt đầu kéo
        def mousePressEvent(event):
            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                button._drag_active = True
                button._drag_start_position = event.pos()
            super(QtWidgets.QPushButton, button).mousePressEvent(event)

        # Di chuyển nút khi kéo
        def mouseMoveEvent(event):
            if button._drag_active and event.buttons() == QtCore.Qt.MouseButton.LeftButton:
                global_mouse_pos = event.globalPosition().toPoint()
                new_pos = button.parent().mapFromGlobal(
                    global_mouse_pos - button._drag_start_position)

                # Giới hạn vị trí nút trong vùng cha
                parent_rect = button.parent().rect()
                new_pos.setX(
                    max(0, min(new_pos.x(), parent_rect.width() - button.width())))
                new_pos.setY(
                    max(0, min(new_pos.y(), parent_rect.height() - button.height())))

                button.move(new_pos)
            super(QtWidgets.QPushButton, button).mouseMoveEvent(event)

        # Kết thúc kéo
        def mouseReleaseEvent(event):
            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                button._drag_active = False
            super(QtWidgets.QPushButton, button).mouseReleaseEvent(event)
        # Xử lý sự kiện nhấn đúp chuột

        def mouseDoubleClickEvent(event):
            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                # print("Nhấn đúp chuột!")

                # Lấy chỉ số hiện tại
                current_index = self.stackedWidget.currentIndex()

                # Lưu chỉ số trước đó nếu chưa lưu
                if not hasattr(button, "_previous_index"):
                    button._previous_index = current_index

                # Chuyển đổi trạng thái
                if current_index != 2:
                    # Lưu trạng thái trước khi chuyển
                    button._previous_index = current_index
                    self.stackedWidget.setCurrentIndex(2)
                else:
                    # Quay lại trạng thái trước đó
                    self.stackedWidget.setCurrentIndex(button._previous_index)

            # Gọi sự kiện mặc định
            super(QtWidgets.QPushButton, button).mouseDoubleClickEvent(event)

        # Gán các phương thức vào button
        button.enterEvent = enterEvent
        button.leaveEvent = leaveEvent
        button.mousePressEvent = mousePressEvent
        button.mouseMoveEvent = mouseMoveEvent
        button.mouseReleaseEvent = mouseReleaseEvent
        button.mouseDoubleClickEvent = mouseDoubleClickEvent

        return button

    def plot_humidity_chart_in_widget(self, data_points, data_points_2, humidity_1, humidity_2):
        """
        Vẽ biểu đồ độ ẩm với tooltip thông minh tự động điều chỉnh vị trí
        """
        parent_widget = self.humi_chart
        figure, ax = plt.subplots(figsize=(12, 6))

        # Tách ngày giờ và độ ẩm từ hai tập dữ liệu
        dates_1, humidity_1_values = zip(*data_points)
        dates_2, humidity_2_values = zip(*data_points_2)

        # Vẽ đường độ ẩm chính (đường 1)
        ax.plot(dates_1, humidity_1_values, color='#0088FF',
                linestyle='-', linewidth=1, label="Đường độ ẩm 1")

        # Vẽ đường độ ẩm thứ hai (đường 2)
        ax.plot(dates_2, humidity_2_values, color='#FF6347',
                linestyle='-', linewidth=1, label="Đường độ ẩm 2")

        # Vẽ các điểm dữ liệu và đường kẻ dọc cho đường 1
        for date, humidity in data_points:
            color = 'red' if humidity > humidity_2 or humidity < humidity_1 else '#00FF00'
            ax.scatter(date, humidity, color=color, s=50)
            ax.plot([date, date], [0, humidity], color='gray',
                    linestyle='-', linewidth=0.5, alpha=0.3)

        # Vẽ các điểm dữ liệu và đường kẻ dọc cho đường 2
        for date, humidity in data_points_2:
            color = 'red' if humidity > humidity_2 or humidity < humidity_1 else '#00FF00'
            ax.scatter(date, humidity, color=color, s=50)
            ax.plot([date, date], [0, humidity], color='gray',
                    linestyle='--', linewidth=0.5, alpha=0.3)

        # Vẽ các đường ngưỡng
        ax.axhline(y=humidity_1, color='#35ff00', linestyle='--',
                   linewidth=1, label=f"Ngưỡng {humidity_1}%")
        ax.axhline(y=humidity_2, color='#f600ff', linestyle='-.',
                   linewidth=1, label=f"Ngưỡng {humidity_2}%")

        # Định dạng trục thời gian
        time_format = mdates.DateFormatter("%H:%M")
        ax.xaxis.set_major_formatter(time_format)
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())

        # Thiết lập nhãn trục và tiêu đề
        ax.set_xlabel("Thời gian", fontsize=10)
        ax.xaxis.set_label_coords(0.95, -0.05)
        ax.set_ylabel("Độ ẩm (%)", fontsize=10)
        ax.yaxis.set_label_coords(-0.03, 0.9)
        figure.text(0.5, 0.1, "Biểu đồ độ ẩm", fontsize=14,
                    ha='center', fontweight='bold')
        ax.legend(loc='best')
        ax.grid(False)

        # Tối ưu layout
        plt.tight_layout()
        figure.autofmt_xdate()

        # Tạo canvas và thêm vào widget
        canvas = FigureCanvas(figure)
        layout = parent_widget.layout()
        if not layout:
            layout = QtWidgets.QVBoxLayout(parent_widget)
            parent_widget.setLayout(layout)
        layout.addWidget(canvas)

        # Tạo annotation cho tooltip
        annot = ax.annotate(
            "",
            xy=(0, 0),
            xytext=(0, 0),
            textcoords="offset points",
            bbox=dict(
                boxstyle="round4,pad=0.5",
                fc="white",
                ec="gray",
                alpha=0.9,
                mutation_scale=0.8
            ),
            arrowprops=dict(
                arrowstyle="-|>",
                connectionstyle="arc3,rad=0.2",
                color='gray'
            )
        )
        annot.set_visible(False)

        def get_smart_offset(date, humidity, ax_bbox):
            """
            Tính toán offset thông minh cho tooltip dựa trên vị trí của điểm và kích thước của đồ thị
            """
            x_rel = (mdates.date2num(date) - ax.get_xlim()
                     [0]) / (ax.get_xlim()[1] - ax.get_xlim()[0])
            y_rel = (humidity - ax.get_ylim()[0]) / \
                (ax.get_ylim()[1] - ax.get_ylim()[0])

            # Offset mặc định
            x_offset = 10
            y_offset = 10

            # Điều chỉnh theo vị trí tương đối
            if x_rel > 0.8:  # Gần mép phải
                x_offset = -80
            elif x_rel < 0.2:  # Gần mép trái
                x_offset = 20

            if y_rel > 0.8:  # Gần mép trên
                y_offset = -40
            elif y_rel < 0.2:  # Gần mép dưới
                y_offset = 20

            return x_offset, y_offset

        def on_hover(event):
            if event.inaxes == ax:
                hit = False
                for idx, (date, humidity) in enumerate(data_points + data_points_2):
                    # Kiểm tra điểm thuộc đường 1 hay đường 2
                    is_first_dataset = idx < len(data_points)
                    dataset_label = "Đường 1" if is_first_dataset else "Đường 2"

                    # Tăng độ nhạy của vùng hover
                    if abs(event.xdata - mdates.date2num(date)) <= 0.001 and abs(event.ydata - humidity) <= 1:
                        hit = True
                        # Lấy offset thông minh
                        x_offset, y_offset = get_smart_offset(
                            date, humidity, ax.bbox)

                        # Cập nhật vị trí và thuộc tính của tooltip
                        annot.xy = (mdates.date2num(date), humidity)
                        annot.set_position((x_offset, y_offset))

                        # Định dạng nội dung tooltip
                        tooltip_text = (
                            f"{dataset_label}\n"
                            f"Ngày: {date.strftime('%d/%m/%Y')}\n"
                            f"Thời gian: {date.strftime('%H:%M')}\n"
                            f"Độ ẩm: {humidity}%"
                        )
                        if humidity > humidity_2:
                            tooltip_text += "\n⚠️ Độ ẩm cao"
                        elif humidity < humidity_1:
                            tooltip_text += "\n⚠️ Độ ẩm thấp"

                        annot.set_text(tooltip_text)

                        # Đổi màu tooltip theo trạng thái độ ẩm
                        if humidity > humidity_2 or humidity < humidity_1:
                            annot.get_bbox_patch().set(fc="#F01F1F")
                        else:
                            annot.get_bbox_patch().set(fc="#00FF00")

                        annot.set_visible(True)
                        canvas.draw_idle()
                        break

                if not hit and annot.get_visible():
                    annot.set_visible(False)
                    canvas.draw_idle()

        canvas.mpl_connect("motion_notify_event", on_hover)
        canvas.setSizePolicy(QSizePolicy.Policy.Expanding,
                             QSizePolicy.Policy.Expanding)

    def plot_voltage_chart_in_widget(self, data_points, data_points_2, dc_1, dc_2, dc_3):
        """
        Vẽ biểu đồ điện áp DC với tooltip thông minh tự động điều chỉnh vị trí và 3 ngưỡng so sánh.
        """
        parent_widget = self.dc_chart  # Widget nơi biểu đồ sẽ hiển thị
        figure, (ax1, ax2) = plt.subplots(
            2, 1, figsize=(12, 12))  # Tạo 2 subplot

        def plot_voltage(ax, data, label, line_color):
            """Hàm vẽ biểu đồ điện áp"""
            dates, voltages = zip(*data)
            ax.plot(dates, voltages, color=line_color,
                    linestyle='-', linewidth=1, label=label)

            # Vẽ các điểm dữ liệu và đường kẻ dọc
            for date, voltage in data:
                color = get_color_based_on_voltage(voltage, dc_1, dc_2, dc_3)
                ax.scatter(date, voltage, color=color, s=50)
                ax.plot([date, date], [0, voltage], color='gray',
                        linestyle='-', linewidth=0.5, alpha=0.3)

            # Vẽ các đường ngưỡng
            ax.axhline(y=dc_1, color='#00FF00', linestyle='-.',
                       linewidth=1, label=f"Ngưỡng {dc_1}V")
            ax.axhline(y=dc_2, color='#FFA500', linestyle=':',
                       linewidth=1, label=f"Ngưỡng {dc_2}V")
            ax.axhline(y=dc_3, color='#FF0000', linestyle='--',
                       linewidth=1, label=f"Ngưỡng {dc_3}V")

            # Thiết lập nhãn trục và tiêu đề
            ax.set_ylabel("Điện áp (V)", fontsize=10)
            ax.yaxis.set_label_coords(-0.03, 0.85)
            ax.set_xlabel("Thời gian", fontsize=10)
            # # Di chuyển nhãn ra ngoài (phía bên phải)
            ax.xaxis.set_label_coords(0.95, -0.1)
            ax.legend(loc='best')
            ax.grid(False)

        def get_color_based_on_voltage(voltage, dc_1, dc_2, dc_3):
            if voltage > dc_3:
                return "#F01F1F"  # Màu đỏ
            elif voltage > dc_2:
                return "#FFA500"  # Màu cam
            elif voltage > dc_1:
                return "#00FF00"  # Màu xanh lá
            else:
                return "#F01F1F"  # Màu đỏ

        # Vẽ biểu đồ đầu tiên (DC1)
        plot_voltage(ax1, data_points, "Điện áp DC1", "#0088FF")
        # Định dạng trục x cho ax1
        ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
        ax1.xaxis.set_major_locator(mdates.AutoDateLocator())
        ax1.tick_params(axis="x")
        # Đặt tiêu đề cho từng subplot

        # ax1.set_xlabel("Thời gian", fontsize=12, labelpad=10)
        # # Di chuyển nhãn ra ngoài (phía bên phải)
        # ax1.xaxis.set_label_coords(1.05, -0.05)

        # Vẽ biểu đồ thứ hai (DC2)
        plot_voltage(ax2, data_points_2, "Điện áp DC2", "#FF6347")
        # Định dạng trục x cho ax2
        ax2.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
        ax2.xaxis.set_major_locator(mdates.AutoDateLocator())
        ax2.tick_params(axis="x")
        # ax2.set_xlabel("Thời gian", fontsize=12, labelpad=10)
        # # Di chuyển nhãn ra ngoài (phía bên phải)
        # ax2.xaxis.set_label_coords(1.05, -0.05)

        # Đặt tiêu đề dưới các biểu đồ
        figure.text(0.5, 0.52, "Điện áp DC1", fontsize=14,
                    ha='center', fontweight='bold')
        figure.text(0.5, 0.02, "Điện áp DC2", fontsize=14,
                    ha='center', fontweight='bold')
        # Tối ưu layout cho cả 2 biểu đồ
        plt.tight_layout()
        # Điều chỉnh khoảng cách giữa các biểu đồ
        plt.subplots_adjust(hspace=0.25, bottom=0.1)

        # Tạo canvas và thêm vào widget
        canvas = FigureCanvas(figure)
        layout = parent_widget.layout()
        if not layout:
            layout = QtWidgets.QVBoxLayout(parent_widget)
            parent_widget.setLayout(layout)
        layout.addWidget(canvas)

        # Tạo annotation cho tooltip của biểu đồ 1
        annot1 = ax1.annotate(
            "",
            xy=(0, 0),
            xytext=(0, 0),
            textcoords="offset points",
            bbox=dict(boxstyle="round4,pad=0.5",
                      fc="white", ec="gray", alpha=0.9),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=0.2", color='gray')
        )
        annot1.set_visible(False)

        # Tạo annotation cho tooltip của biểu đồ 2
        annot2 = ax2.annotate(
            "",
            xy=(0, 0),
            xytext=(0, 0),
            textcoords="offset points",
            bbox=dict(boxstyle="round4,pad=0.5",
                      fc="white", ec="gray", alpha=0.9),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=0.2", color='gray')
        )
        annot2.set_visible(False)

        def get_smart_offset(date, voltage, ax_bbox):
            """Tính toán offset thông minh cho tooltip"""
            x_rel = (mdates.date2num(date) - ax1.get_xlim()
                     [0]) / (ax1.get_xlim()[1] - ax1.get_xlim()[0])
            y_rel = (voltage - ax1.get_ylim()[0]) / \
                (ax1.get_ylim()[1] - ax1.get_ylim()[0])

            x_offset = -100 if x_rel > 0.8 else 20 if x_rel < 0.2 else 10
            y_offset = -40 if y_rel > 0.8 else 20 if y_rel < 0.2 else 10

            return x_offset, y_offset

        def on_hover(event):
            """Xử lý sự kiện hover để hiển thị tooltip trên cả hai biểu đồ"""
            hit = False

            # Kiểm tra biểu đồ thứ nhất (ax1)
            if event.inaxes == ax1:
                for date, voltage in data_points:
                    if abs(event.xdata - mdates.date2num(date)) <= 0.001 and abs(event.ydata - voltage) <= 1:
                        hit = True
                        x_offset, y_offset = get_smart_offset(
                            date, voltage, ax1.bbox)
                        annot1.xy = (mdates.date2num(date), voltage)
                        annot1.set_position((x_offset, y_offset))
                        tooltip_text = (
                            f"Ngày: {date.strftime('%d/%m/%Y')}\n"
                            f"Thời gian: {date.strftime('%H:%M')}\n"
                            f"Điện áp: {voltage}V"
                        )
                        tooltip_text += (
                            "\n⚠️ Quá điện áp" if voltage > dc_3 else
                            "\n⚠️ Điện áp cao (Ngưỡng trung)" if voltage > dc_2 else
                            "\nĐiện áp vừa phải" if voltage > dc_1 else
                            "\n⚠️ Điện áp thấp"
                        )
                        annot1.set_text(tooltip_text)
                        annot1.get_bbox_patch().set(fc=get_color_based_on_voltage(voltage, dc_1, dc_2, dc_3))
                        annot1.set_visible(True)
                        canvas.draw_idle()
                        break
                if not hit and annot1.get_visible():
                    annot1.set_visible(False)
                    canvas.draw_idle()

            # Kiểm tra biểu đồ thứ hai (ax2)
            elif event.inaxes == ax2:
                for date, voltage in data_points_2:
                    if abs(event.xdata - mdates.date2num(date)) <= 0.001 and abs(event.ydata - voltage) <= 1:
                        hit = True
                        x_offset, y_offset = get_smart_offset(
                            date, voltage, ax2.bbox)
                        annot2.xy = (mdates.date2num(date), voltage)
                        annot2.set_position((x_offset, y_offset))
                        tooltip_text = (
                            f"Ngày: {date.strftime('%d/%m/%Y')}\n"
                            f"Thời gian: {date.strftime('%H:%M')}\n"
                            f"Điện áp: {voltage}V"
                        )
                        tooltip_text += (
                            "\n⚠️ Quá điện áp" if voltage > dc_3 else
                            "\n⚠️ Điện áp cao (Ngưỡng trung)" if voltage > dc_2 else
                            "\nĐiện áp vừa phải" if voltage > dc_1 else
                            "\n⚠️ Điện áp thấp"
                        )
                        annot2.set_text(tooltip_text)
                        annot2.get_bbox_patch().set(fc=get_color_based_on_voltage(voltage, dc_1, dc_2, dc_3))
                        annot2.set_visible(True)
                        canvas.draw_idle()
                        break
                if not hit and annot2.get_visible():
                    annot2.set_visible(False)
                    canvas.draw_idle()

        canvas.mpl_connect("motion_notify_event", on_hover)
        canvas.setSizePolicy(QSizePolicy.Policy.Expanding,
                             QSizePolicy.Policy.Expanding)
