import sys
import socket
import threading
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import pyqtSignal, QObject


# Lớp để tạo tín hiệu cập nhật GUI từ thread khác
class Communicator(QObject):
    update_label = pyqtSignal(str)


def get_local_ip():
    """Lấy IP nội bộ của máy đang chạy"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


class ServerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TCP Server - Hiển thị dữ liệu nhận")
        self.setGeometry(300, 300, 500, 200)

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Dữ liệu nhận sẽ hiển thị tại đây:")
        self.layout.addWidget(self.info_label)

        self.data_label = QLabel("(Chưa có dữ liệu)")
        self.data_label.setStyleSheet("font-size: 20px; color: blue;")
        self.layout.addWidget(self.data_label)

        self.setLayout(self.layout)

        # Tạo đối tượng signal để truyền dữ liệu giữa luồng
        self.comm = Communicator()
        self.comm.update_label.connect(self.update_display)

        # Khởi động server
        self.start_server()

    def update_display(self, message):
        """Cập nhật nội dung dữ liệu lên giao diện"""
        self.data_label.setText(message)

    def start_server(self):
        """Khởi động server trong luồng nền"""
        host = get_local_ip()
        port = 2380
        print(f"🌐 Server chạy tại: {host}:{port}")

        server_thread = threading.Thread(
            target=self.receive_data, args=(host, port), daemon=True)
        server_thread.start()

    def receive_data(self, host, port):
        """Lắng nghe và nhận dữ liệu TCP"""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"🔵 Server đang lắng nghe trên {host}:{port}...")

        try:
            while True:
                connection, client_address = server_socket.accept()
                print(f"🟢 Kết nối từ {client_address}")

                try:
                    while True:
                        data = connection.recv(1024)
                        if not data:
                            print(f"🔴 {client_address} đã ngắt kết nối.")
                            break

                        message = data.decode()
                        print(f"📩 Nhận từ {client_address}: {message}")

                        # Gửi phản hồi lại client (nếu cần)
                        connection.sendall("nguyendangdeptrai".encode())

                        # Cập nhật giao diện
                        self.comm.update_label.emit(
                            f"Từ {client_address}: {message}")

                except (ConnectionResetError, ConnectionAbortedError):
                    print(f"⚠️ Lỗi kết nối với {client_address}")
                finally:
                    connection.close()
        finally:
            server_socket.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerGUI()
    window.show()
    sys.exit(app.exec())
