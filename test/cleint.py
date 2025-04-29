import sys
import socket
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QLabel, QGridLayout
)


def get_local_ip():
    """Lấy IP nội bộ của máy hiện tại"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


class TcpClientGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TCP Client - Gửi Dữ Liệu")
        self.setGeometry(300, 300, 800, 600)

        main_layout = QVBoxLayout()

        # IP Server
        self.ip_label = QLabel("Nhập IP Server:")
        self.ip_input = QLineEdit()
        self.ip_input.setText(get_local_ip())
        main_layout.addWidget(self.ip_label)
        main_layout.addWidget(self.ip_input)

        # IP Client
        self.client_ip_label = QLabel(
            "Nhập IP Client (mặc định là 192.168.0.1):")
        self.client_ip_input = QLineEdit()
        self.client_ip_input.setText("192.168.0.1")
        main_layout.addWidget(self.client_ip_label)
        main_layout.addWidget(self.client_ip_input)

        # Layout chia 2 cột
        two_column_layout = QHBoxLayout()

        self.input_fields = []
        self.send_buttons = []

        default_data = [
            "192.168.0.1,aht temp,20",
            "192.168.0.1,aht humi,40",
            "192.168.0.1,bme temp,30",
            "192.168.0.1,bme humi,50",
            "192.168.0.1,dc1_voltage,12",
            "192.168.0.1,dc2_voltage,24",
            "192.168.0.1,dc1_voltage,24",
            "192.168.0.1,ac1,ON",
            "192.168.0.1,ac2,OFF",
            "192.168.0.1,temp threshold,20,25",
            "192.168.0.1,humi threshold,40,60",
            "192.168.0.1,dc threshold,46,47,53.5",



        ]

        column1 = QVBoxLayout()
        column2 = QVBoxLayout()

        for i in range(12):
            label = QLabel(f"Dòng {i+1}:")
            input_field = QLineEdit()
            input_field.setText(default_data[i])
            send_button = QPushButton(f"Gửi Dữ Liệu Dòng {i+1}")
            send_button.clicked.connect(
                lambda _, idx=i: self.send_data_line(idx))

            self.input_fields.append(input_field)
            self.send_buttons.append(send_button)

            vbox = QVBoxLayout()
            vbox.addWidget(label)
            vbox.addWidget(input_field)
            vbox.addWidget(send_button)

            if i < 6:
                column1.addLayout(vbox)
            else:
                column2.addLayout(vbox)

        two_column_layout.addLayout(column1)
        two_column_layout.addLayout(column2)

        main_layout.addLayout(two_column_layout)

        # Nhãn phản hồi
        self.response_label = QLabel("")
        main_layout.addWidget(self.response_label)

        # Nút gửi tất cả
        self.send_all_button = QPushButton("🚀 Gửi Tất Cả Dữ Liệu")
        self.send_all_button.clicked.connect(self.send_all_data)
        main_layout.addWidget(self.send_all_button)

        self.setLayout(main_layout)

    def send_data(self, message):
        host = self.ip_input.text().strip()
        port = 2380

        if not message:
            self.response_label.setText("⚠️ Vui lòng nhập dữ liệu.")
            return

        try:
            with socket.create_connection((host, port), timeout=5) as client_socket:
                client_socket.sendall(message.encode())
                response = client_socket.recv(1024).decode()
                self.response_label.setText(f"✅ Server phản hồi: {response}")
        except Exception as e:
            self.response_label.setText(f"❌ Lỗi kết nối: {e}")

    def send_data_line(self, index):
        message = self.input_fields[index].text().strip()
        self.send_data(message)

    def send_all_data(self):
        for field in self.input_fields:
            message = field.text().strip()
            if message:
                self.send_data(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TcpClientGUI()
    window.show()
    sys.exit(app.exec())
