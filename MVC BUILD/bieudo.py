import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class TemperatureChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Biểu đồ nhiệt độ")
        self.setGeometry(100, 100, 800, 600)

        # Dữ liệu nhiệt độ
        self.temperature_data = [15, 20, 25, 30, 35, 28, 22, 18, 15, 10, 5, 20]
        self.months = list(range(1, 13))

        # Tạo widget trung tâm
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Tạo biểu đồ matplotlib
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.plot_chart()

    def plot_chart(self):
        self.ax.clear()

        # Phân loại điểm theo nhiệt độ và vẽ đường thẳng dọc
        for month, temp in zip(self.months, self.temperature_data):
            if temp > 20:
                color = 'red'  # Trên 20 độ
            elif temp == 20:
                color = 'yellow'  # Bằng 20 độ
            else:
                color = 'blue'  # Dưới 20 độ

            # Vẽ từng điểm với kích thước lớn hơn
            self.ax.scatter(month, temp, color=color, s=150, label=f"{
                            temp}°C" if month == 1 else None)

            # Vẽ đường thẳng dọc từ điểm đến trục x, màu xám nhạt, nét nhỏ
            self.ax.plot([month, month], [0, temp],
                         color='lightgray', linestyle='-', linewidth=0.5)

            # Hiển thị giá trị nhiệt độ trên điểm với kích thước font chữ lớn hơn
            self.ax.text(
                month, temp + 1,
                f"{temp}°C",
                fontsize=12,  # Thay đổi kích thước font ở đây
                ha='center',
                color=color
            )

        # Vẽ đường nối với độ dày lớn hơn
        self.ax.plot(
            self.months,
            self.temperature_data,
            color='black',
            linestyle='--',
            linewidth=2,  # Độ dày của đường
            label="Đường nhiệt độ"
        )

        # Vẽ đường ngang tại mức nhiệt độ 20°C
        self.ax.axhline(y=20, color='green', linestyle='-',
                        linewidth=1, label="Mức 20°C")

        # Thiết lập tiêu đề và nhãn
        # Thay đổi kích thước tiêu đề
        self.ax.set_title("Biểu đồ nhiệt độ theo tháng", fontsize=14)
        # Thay đổi kích thước nhãn trục x
        self.ax.set_xlabel("Tháng", fontsize=12)
        # Thay đổi kích thước nhãn trục y
        self.ax.set_ylabel("Nhiệt độ (°C)", fontsize=12)
        self.ax.legend(loc='upper left')

        # Tắt đường lưới
        self.ax.grid(False)

        # Tạo annotation (tooltip động)
        self.annot = self.ax.annotate(
            "", xy=(0, 0), xytext=(10, 10),
            textcoords="offset points",
            bbox=dict(boxstyle="round", fc="w"),
            arrowprops=dict(arrowstyle="->")
        )
        self.annot.set_visible(False)

        # Kết nối sự kiện hover
        self.canvas.mpl_connect("motion_notify_event", self.on_hover)

        self.canvas.draw()

    def on_hover(self, event):
        if event.inaxes == self.ax and event.xdata is not None and event.ydata is not None:
            for i, temp in enumerate(self.temperature_data):
                x, y = self.months[i], temp
                if abs(event.xdata - x) <= 0.25 and abs(event.ydata - y) <= 2:
                    self.annot.xy = (x, y)
                    self.annot.set_text(f"Tháng: {x}, Nhiệt độ: {y}°C")
                    self.annot.set_visible(True)
                    self.canvas.draw_idle()
                    return
            self.annot.set_visible(False)
            self.canvas.draw_idle()


def main():
    app = QApplication(sys.argv)
    window = TemperatureChartWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
