import socket
import threading


def receive_data(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"🔵 Server đang lắng nghe trên {host}:{port}...")

    try:
        while True:
            connection, client_address = server_socket.accept()
            print(f"🟢 Đã kết nối với {client_address}")

            try:
                while True:
                    data = connection.recv(1024)
                    if not data:
                        print(f"🔴 Client {client_address} đã ngắt kết nối.")
                        break

                    message = data.decode()
                    print(f"📩 Nhận từ {client_address}: {message}")

                    # Phản hồi lại đúng nội dung nhận được
                    # connection.sendall(data)
                    connection.sendall("nguyendangdeptrai".encode())

            except ConnectionResetError:
                print(f"⚠️ Kết nối với {client_address} bị reset đột ngột.")

            except ConnectionAbortedError:
                print(f"⚠️ Kết nối với {client_address} bị đóng đột ngột.")

            finally:
                connection.close()

    except KeyboardInterrupt:
        print("\n⚠️ Server dừng lại do người dùng.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    HOST = "192.168.0.99"
    PORT = 2380

    # Chạy server trong một luồng riêng
    server_thread = threading.Thread(
        target=receive_data, args=(HOST, PORT), daemon=True)
    server_thread.start()

    # Đợi server khởi động
    import time
    time.sleep(2)
