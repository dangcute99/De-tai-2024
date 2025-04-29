from datetime import datetime
import json
from db_connection import DatabaseConnection
import sys
import socket
import threading
tram1_ip = "192.168.0.1"
###########################################################################################
# Tạo bảng measurements và faults
create_table_measurements_query = """
CREATE TABLE IF NOT EXISTS measurements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    temperature FLOAT,
    temperature_low FLOAT,
    temperature_high FLOAT,
    humidity FLOAT,
    humidity_low FLOAT,
    humidity_high FLOAT,
    dc1_voltage FLOAT,
    dc1_voltage_low_1 FLOAT,
    dc1_voltage_low_2 FLOAT,
    dc1_voltage_high FLOAT,
    dc2_voltage FLOAT,
    dc2_voltage_low_1 FLOAT,
    dc2_voltage_low_2 FLOAT,
    dc2_voltage_high FLOAT,
    ac_voltage FLOAT,
    fault_status VARCHAR(255)
);
"""
create_table_faults_query = """CREATE TABLE IF NOT EXISTS faults (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    fault_type VARCHAR(255),
    measurement_id INT,
    FOREIGN KEY (measurement_id) REFERENCES measurements(id)
);
"""
create_table_login_in4_query = """CREATE TABLE IF NOT EXISTS login_in4 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    username VARCHAR(255),
    passwords VARCHAR(255)
);
"""
create_table_temp1_value_query = """CREATE TABLE IF NOT EXISTS temp1_value (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    temp1 FLOAT,
    temp_min FLOAT,
    temp_max FLOAT,
    alert_type VARCHAR(255)
);
"""
create_table_temp2_value_query = """CREATE TABLE IF NOT EXISTS temp2_value (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    temp2 FLOAT,
    temp_min FLOAT,
    temp_max FLOAT,
    alert_type VARCHAR(255)
);
"""
create_table_humi1_value_query = """CREATE TABLE IF NOT EXISTS humi1_value (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    humi1 FLOAT,
    humi_min FLOAT,
    humi_max FLOAT,
    alert_type VARCHAR(255)
);
"""
create_table_humi2_value_query = """CREATE TABLE IF NOT EXISTS humi2_value (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    humi2 FLOAT,
    humi_min FLOAT,
    humi_max FLOAT,
    alert_type VARCHAR(255)
);
"""
create_table_dc1_value_query = """CREATE TABLE IF NOT EXISTS dc1_value (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    dc1 FLOAT,
    dc_low_1 FLOAT,
    dc_low_2 FLOAT,
    dc_high FLOAT,
    alert_type VARCHAR(255)
);
"""
create_table_dc2_value_query = """CREATE TABLE IF NOT EXISTS dc2_value (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    dc2 FLOAT,
    dc_low_1 FLOAT,
    dc_low_2 FLOAT,
    dc_high FLOAT,
    alert_type VARCHAR(255)
);
"""
create_table_ac1_value_query = """CREATE TABLE IF NOT EXISTS ac_value (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    ac FLOAT,
    alert_type VARCHAR(255)
);
"""
create_table_ac2_value_query = """CREATE TABLE IF NOT EXISTS ac2_value (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    ac2 FLOAT,
    alert_type VARCHAR(255)
);
"""
create_table_temp_threshold_query = """CREATE TABLE IF NOT EXISTS threshold_temp (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    temp_min    FLOAT,
    temp_max FLOAT
);
"""
create_table_humi_threshold_query = """CREATE TABLE IF NOT EXISTS threshold_humi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    humi_min FLOAT,
    humi_max FLOAT
);
"""
create_table_dc_threshold_query = """CREATE TABLE IF NOT EXISTS threshold_dc (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    dc_low_1 FLOAT,
    dc_low_2 FLOAT,
    dc_high FLOAT
);
"""


class Model:
    def __init__(self, db_config):
        self.db = DatabaseConnection(**db_config)
        if self.check_connection():
            self.create_table_in4_if_not_exists()
            print("Đã tạo tt cơ bản")

    def check_connection(self):
        return self.db.check_connection()

    def create_table_in4_if_not_exists(self):
        self.db.create_database('data')
        self.db.execute_query(create_table_login_in4_query, 'data')
        self.db.execute_query(create_table_temp1_value_query, 'data')
        self.db.execute_query(create_table_temp2_value_query, 'data')
        self.db.execute_query(create_table_humi1_value_query, 'data')
        self.db.execute_query(create_table_humi2_value_query, 'data')
        self.db.execute_query(create_table_dc1_value_query, 'data')
        self.db.execute_query(create_table_dc2_value_query, 'data')
        self.db.execute_query(create_table_ac1_value_query, 'data')
        self.db.execute_query(create_table_ac2_value_query, 'data')
        self.db.execute_query(create_table_temp_threshold_query, 'data')
        self.db.execute_query(create_table_humi_threshold_query, 'data')
        self.db.execute_query(create_table_dc_threshold_query, 'data')
        default_users_data = {'username': 'admin', 'passwords': '123456'}
        if not (self.user_exists('login_in4', default_users_data)):
            self.insert_multiple_values(
                'data', 'login_in4', default_users_data)
            print("Đã tạo user mặc định")
        else:
            print("User mặc định đã tồn tại")

    def return_user_exists(self, users_data_1):
        return self.user_exists('login_in4', users_data_1)

    def user_exists(self, table, users_data):
        # Lấy giá trị username và passwords từ dictionary users_data
        username = users_data.get('username')
        password = users_data.get('passwords')
        # print(username, password)
        # Truy vấn kiểm tra xem người dùng có tồn tại trong bảng login_in4 không
        query = f"SELECT COUNT(*) FROM {table} WHERE username = '{
            username}' AND passwords = '{password}'"
        # print(query)
        # Gọi execute_query để kiểm tra sự tồn tại của username và password
        result = self.db.execute_query(query, 'data')
        print(result)

        # Kiểm tra kết quả của truy vấn
        if result and result[0][0] > 0:
            print("Người dùng tồn tại")
            return True  # Người dùng tồn tại
        else:
            print("Người dùng không tồn tại")
            return False  # Người dùng không tồn tại

    def check_login(self, username, password, database):
        """Kiểm tra thông tin đăng nhập"""
        query = f"""
        SELECT * FROM users
        WHERE username = '{username}'
        AND password = '{password}'
        """
        result = self.execute_query(query, database)

        if result:
            return True  # Đăng nhập thành công
        return False    # Đăng nhập thất bại

    def get_x_values_latest(self, database, table, column_name, x=1):
        latest_data = self.db.get_x_notnull(
            database, table, column_name, x=x)
        if latest_data:
            # Chuyển đổi datetime thành chuỗi để có thể serialize
            json_data = []
            for row in latest_data:
                json_row = {
                    'id': row['id'],
                    'timestamp': row['timestamp'].isoformat(),
                    column_name: row[column_name]
                }
                json_data.append(json_row)
            return json.dumps(json_data, ensure_ascii=False)
        return json.dumps([])  # Trả về một mảng rỗng nếu không có dữ liệu

    def get_x_firgue_data(self, database, table, column_name, x=1):
        # Lấy JSON string từ hàm trước
        json_str = self.get_x_values_latest(database, table, column_name, x)
        json_data = json.loads(json_str)

        data_points = []
        for row in json_data:
            timestamp = datetime.fromisoformat(row['timestamp'])
            value = row[column_name]
            data_points.append((timestamp, value))

        return data_points

    # data = {
    #     'humidity': {'value': 52, 'low': 20.0, 'high': 30.0},
    #     # 'humidity': {'value': 60.0, 'low': 40.0, 'high': 80.0},
    #     # 'dc1_voltage': {'value': 12.0, 'low_1': 11.0, 'low_2': 11.5, 'high': 13.0},
    #     # 'ac_voltage': 220.0,
    #     # 'fault_status': 'Normal'
    # }

    # # Thêm nhiều giá trị cùng một lúc
    # db.insert_multiple_values('data', 'measurements', data)

    def insert_multiple_values(self, database, table, data):
        self.db.insert_multiple_values(database, table, data)

    def get_cell_value_by_id(self, database, table, column_name, id):
        return self.db.get_cell_value_by_id(database, table, column_name, id)

    def delete_row(self, database, table, id_row):
        return self.db.delete_row(database, table, id_row)

    def update_row(self, database, table, id_row, data):
        return self.db.update_row(database, table, id_row, data)

    def check_in4(self, database, table, username, password):
        return self.db.check_in4(database, table, username, password)

    def close_connection(self):
        self.db.close_connection()

    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        except Exception:
            ip = "127.0.0.1"
        finally:
            s.close()
        return ip

    def start_server(self):
        """Khởi động server trong luồng nền"""
        host = self.get_local_ip()
        port = 2380
        print(f"🌐 Server chạy tại: {host}:{port}")

        server_thread = threading.Thread(
            target=self.receive_data, args=(host, port), daemon=True)
        server_thread.start()

    def get_lan_value(self, expected_ip, expected_sensor, message):
        """
        Tách dữ liệu từ message có dạng: '192.168.0.1,aht temperature, 30.4'
        Nếu IP đầu tiên trong message trùng expected_ip thì in ra kết quả.
        """
        parts = [part.strip() for part in message.split(',')]

        if len(parts) == 3:
            ip = parts[0]
            sensor_type = parts[1]
            value = parts[2]
            # print(message)
            if ip == expected_ip:
                if sensor_type == expected_sensor:
                    # print(f"📊 Value: {value}")
                    # Chuyển đổi giá trị thành số thực
                    return value
                else:
                    # print(f"🌐 Sensor không đúng: {sensor_type}")
                    return False
            # Nếu IP không đúng, không in gì cả
            else:
                print(f"🌐 IP không đúng: {ip}")

    def get_2_lan_value(self, expected_ip, expected_sensor, message):
        """
        Tách dữ liệu từ message có dạng: '192.168.0.1,aht temperature, 30.4'
        Nếu IP đầu tiên trong message trùng expected_ip thì in ra kết quả.
        """
        parts = [part.strip() for part in message.split(',')]

        if len(parts) == 4:
            ip = parts[0]
            sensor_type = parts[1]
            value1 = parts[2]
            value2 = parts[3]

            if ip == expected_ip:
                if sensor_type == expected_sensor:
                    # print(f"📊 Value1: {value1}")
                    # print(f"📊 Value2: {value2}")
                    data = {'value1': value1, 'value2': value2}
                    # Chuyển đổi giá trị thành số thực
                    return data
                else:
                    print(f"🌐 Sensor không đúng: {sensor_type}")
                    return False
            # Nếu IP không đúng, không in gì cả
            else:
                print(f"🌐 IP không đúng: {ip}")

    def get_3_lan_value(self, expected_ip, expected_sensor, message):
        """
        Tách dữ liệu từ message có dạng: '192.168.0.1,aht temperature, 30.4'
        Nếu IP đầu tiên trong message trùng expected_ip thì in ra kết quả.
        """
        parts = [part.strip() for part in message.split(',')]

        if len(parts) == 5:
            ip = parts[0]
            sensor_type = parts[1]
            value1 = parts[2]
            value2 = parts[3]
            value3 = parts[4]

            if ip == expected_ip:
                if sensor_type == expected_sensor:
                    # print(f"📊 Value1: {value1}")
                    # print(f"📊 Value2: {value2}")
                    # print(f"📊 Value3: {value3}")
                    data = {'value1': value1,
                            'value2': value2, 'value3': value3}
                    # Chuyển đổi giá trị thành số thực
                    return data
                else:
                    print(f"🌐 Sensor không đúng: {sensor_type}")
                    return False
            # Nếu IP không đúng, không in gì cả
            else:
                print(f"🌐 IP không đúng: {ip}")

    def get_threshold_data_from_device(self, expected_ip, message):

        # lay du lieu nguong nhiet do
        if self.get_2_lan_value(expected_ip, "temp threshold", message):
            temp_threshold = self.get_2_lan_value(
                expected_ip, "temp threshold", message)
            temp_min = temp_threshold['value1']
            temp_max = temp_threshold['value2']
            self.insert_multiple_values(
                'data', 'threshold_temp', {'temp_min': temp_min, 'temp_max': temp_max})
            print("📩 Nhận từ trạm 1 đúng ngưỡng nhiệt độ")
        # lay du lieu nguong do am
        if self.get_2_lan_value(expected_ip, "humi threshold", message):
            humi_threshold = self.get_2_lan_value(
                expected_ip, "humi threshold", message)
            humi_min = humi_threshold['value1']
            humi_max = humi_threshold['value2']
            self.insert_multiple_values(
                'data', 'threshold_humi', {'humi_min': humi_min, 'humi_max': humi_max})
            print("📩 Nhận từ trạm  1 đúng ngưỡng độ ẩm")
        # lay du lieu nguong dien ap
        if self.get_3_lan_value(expected_ip, "dc threshold", message):
            dc_threshold = self.get_3_lan_value(
                expected_ip, "dc threshold", message)
            dc_low_1 = dc_threshold['value1']
            dc_low_2 = dc_threshold['value2']
            dc_high = dc_threshold['value3']
            self.insert_multiple_values(
                'data', 'threshold_dc', {'dc_low_1': dc_low_1, 'dc_low_2': dc_low_2, 'dc_high': dc_high})
            print("📩 Nhận từ trạm 1 đúng ngưỡng điện áp")

    def get_sensor_data_from_device(self, expected_ip, message):
        ########################################################
        # lay du lieu nhiet do tu cam bien 1
        if self.get_lan_value(expected_ip, "aht temp", message):
            aht_temp_value = float(self.get_lan_value(
                expected_ip, "aht temp", message))
            temp_min = json.loads(self.get_x_values_latest(
                'data', 'threshold_temp', 'temp_min'))
            temp_min_value = float(temp_min[0]['temp_min'])
            temp_max = json.loads(self.get_x_values_latest(
                'data', 'threshold_temp', 'temp_max'))
            temp_max_value = float(temp_max[0]['temp_max'])

            if aht_temp_value < temp_min_value:
                alert_type = "Nhiet do thap"
            elif aht_temp_value > temp_max_value:
                alert_type = "Nhiet do cao"
            else:
                alert_type = "Nhiet do binh thuong"

            data = {'temp1': aht_temp_value, 'temp_min': temp_min_value,
                    'temp_max': temp_max_value, 'alert_type': alert_type}
            # print(data)
            self.insert_multiple_values(
                'data', 'temp1_value', data)
            print("📩 Nhận từ cleint đúng temp 1 value")
        # else:
        #     print("📩 Nhận từ cleint sai temp 1 value")
        ####################################################
        # lay du lieu do am tu cam bien 1
        if self.get_lan_value(expected_ip, "aht humi", message):
            aht_humi_value = float(self.get_lan_value(
                expected_ip, "aht humi", message))
            humi_min = json.loads(self.get_x_values_latest(
                'data', 'threshold_humi', 'humi_min'))
            humi_min_value = float(humi_min[0]['humi_min'])
            humi_max = json.loads(self.get_x_values_latest(
                'data', 'threshold_humi', 'humi_max'))
            humi_max_value = float(humi_max[0]['humi_max'])
            if aht_humi_value < humi_min_value:
                alert_type = "Do am thap"
            elif aht_humi_value > humi_max_value:
                alert_type = "Do am cao"
            else:
                alert_type = "Do am binh thuong"
            data = {'humi1': aht_humi_value, 'humi_min': humi_min_value,
                    'humi_max': humi_max_value, 'alert_type': alert_type}
            # print(data)
            self.insert_multiple_values(
                'data', 'humi1_value', data)
            print("📩 Nhận từ cleint đúng humi 1 value")
        # else:
            # print("📩 Nhận từ cleint sai humi 1 value")
            #################################################
            # lay du lieu nhiet do tu cam bien 2
        if self.get_lan_value(expected_ip, "bme temp", message):
            bme_temp_value = float(self.get_lan_value(
                expected_ip, "bme temp", message))
            temp_min = json.loads(self.get_x_values_latest(
                'data', 'threshold_temp', 'temp_min'))
            temp_min_value = float(temp_min[0]['temp_min'])
            temp_max = json.loads(self.get_x_values_latest(
                'data', 'threshold_temp', 'temp_max'))
            temp_max_value = float(temp_max[0]['temp_max'])

            if bme_temp_value < temp_min_value:
                alert_type = "Nhiet do thap"
            elif bme_temp_value > temp_max_value:
                alert_type = "Nhiet do cao"
            else:
                alert_type = "Nhiet do binh thuong"

            data = {'temp2': bme_temp_value, 'temp_min': temp_min_value,
                    'temp_max': temp_max_value, 'alert_type': alert_type}
            # print(data)
            self.insert_multiple_values(
                'data', 'temp2_value', data)
            print("📩 Nhận từ cleint đúng temp 2 value")
        # else:
        #     print("📩 Nhận từ cleint sai temp 2 value")
        #################################################
        # lay du lieu do am tu cam bien 2
        if self.get_lan_value(expected_ip, "bme humi", message):
            bme_humi_value = float(self.get_lan_value(
                expected_ip, "bme humi", message))
            humi_min = json.loads(self.get_x_values_latest(
                'data', 'threshold_humi', 'humi_min'))
            humi_min_value = float(humi_min[0]['humi_min'])
            humi_max = json.loads(self.get_x_values_latest(
                'data', 'threshold_humi', 'humi_max'))
            humi_max_value = float(humi_max[0]['humi_max'])
            if bme_humi_value < humi_min_value:
                alert_type = "Do am thap"
            elif bme_humi_value > humi_max_value:
                alert_type = "Do am cao"
            else:
                alert_type = "Do am binh thuong"
            data = {'humi2': bme_humi_value, 'humi_min': humi_min_value,
                    'humi_max': humi_max_value, 'alert_type': alert_type}
            # print(data)
            self.insert_multiple_values(
                'data', 'humi2_value', data)
            print("📩 Nhận từ cleint đúng humi 2 value")
        # else:
        #     print("📩 Nhận từ cleint sai humi 2 value")
        #################################################
        # lay du lieu dien ap tu cam bien 1
        if self.get_lan_value(expected_ip, "dc1_voltage", message):
            dc1_voltage = float(self.get_lan_value(
                expected_ip, "dc1_voltage", message))
            print(dc1_voltage)
            dc_low_1 = json.loads(self.get_x_values_latest(
                'data', 'threshold_dc', 'dc_low_1'))
            dc_low_1_value = float(dc_low_1[0]['dc_low_1'])
            dc_low_2 = json.loads(self.get_x_values_latest(
                'data', 'threshold_dc', 'dc_low_2'))
            dc_low_2_value = float(dc_low_2[0]['dc_low_2'])
            dc_high = json.loads(self.get_x_values_latest(
                'data', 'threshold_dc', 'dc_high'))
            dc_high_value = float(dc_high[0]['dc_high'])
            if dc1_voltage < dc_low_1_value:
                alert_type = "Canh bao dien ap thap"
            elif dc1_voltage > dc_high_value:
                alert_type = "Canh bao dien ao cao"
            elif dc1_voltage <= dc_low_2_value and dc1_voltage >= dc_low_1_value:
                alert_type = "Canh bao muc 1"
            else:
                alert_type = "Dien ap binh thuong"
            data = {'dc1': dc1_voltage, 'dc_low_1': dc_low_1_value,
                    'dc_low_2': dc_low_2_value, 'dc_high': dc_high_value, 'alert_type': alert_type}
            self.insert_multiple_values(
                'data', 'dc1_value', data)
            print("📩 Nhận từ cleint đúng dc1 value")
        #################################################
        # lay du lieu dien ap tu cam bien 2
        if self.get_lan_value(expected_ip, "dc2_voltage", message):
            dc2_voltage = float(self.get_lan_value(
                expected_ip, "dc2_voltage", message))
            dc_low_1 = json.loads(self.get_x_values_latest(
                'data', 'threshold_dc', 'dc_low_1'))
            dc_low_1_value = float(dc_low_1[0]['dc_low_1'])
            dc_low_2 = json.loads(self.get_x_values_latest(
                'data', 'threshold_dc', 'dc_low_2'))
            dc_low_2_value = float(dc_low_2[0]['dc_low_2'])
            dc_high = json.loads(self.get_x_values_latest(
                'data', 'threshold_dc', 'dc_high'))
            dc_high_value = float(dc_high[0]['dc_high'])
            if dc2_voltage < dc_low_1_value:
                alert_type = "Canh bao dien ap thap"
            elif dc2_voltage > dc_high_value:
                alert_type = "Canh bao dien ao cao"
            elif dc2_voltage <= dc_low_2_value and dc2_voltage >= dc_low_1_value:
                alert_type = "Canh bao muc 2"
            else:
                alert_type = "Dien ap binh thuong"
            data = {'dc2': dc2_voltage, 'dc_low_1': dc_low_1_value,
                    'dc_low_2': dc_low_2_value, 'dc_high': dc_high_value, 'alert_type': alert_type}
            self.insert_multiple_values(
                'data', 'dc2_value', data)
            print("📩 Nhận từ cleint đúng dc2 value")

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
                # print(f"🟢 Kết nối từ {client_address}")

                try:
                    while True:
                        data = connection.recv(1024)

                        if not data:
                            # print(f"🔴 {client_address} đã ngắt kết nối.")
                            break

                        message = data.decode()
                        self.get_threshold_data_from_device(tram1_ip, message)
                        self.get_sensor_data_from_device(tram1_ip, message)
                        # if dc_low_1 and dc_low_2 and dc_high:
                        #     self.insert_multiple_values(
                        #         'data', 'dc_threshold', {'dc_low_1': dc_low_1, 'dc_low_2': dc_low_2, 'dc_high': dc_high})
                        #     print("📩 Nhận từ cleint đúng")
                        #
                        # print(f"📩 Nhận từ {client_address}: {message}")

                        # Phản hồi lại đúng nội dung nhận được
                        # connection.sendall(data)
                        # connection.sendall("nguyendangdeptrai".encode())
                        connection.sendall(message.encode())

                except ConnectionResetError:
                    print(f"⚠️ Lỗi kết nối với {client_address}")
                finally:
                    connection.close()
        finally:
            server_socket.close()
            print("🔴 Server đã ngừng lắng nghe.")


# def create_default_user(self, database):

# ###########################################################################################
# ###########################################################################################

# db = DatabaseConnection(**db_in4.db_config)
# column_to_check = 'humidity'  # Hoặc bất kỳ cột nào bạn muốn kiểm tra
# latest_data = db.get_x_notnull(
#     'data', 'measurements', column_to_check, x=30)

# # In kết quả
# if latest_data:
#     for row in latest_data:
#         print(f"ID: {row['id']}, Thời gian: {row['timestamp']}, {
#               column_to_check}: {row[column_to_check]}")
# else:
#     print("Không tìm thấy dữ liệu hoặc có lỗi xảy ra.")

# db.close_connection()
# ###########################################################################################
# db_config = {'host': 'localhost', 'username': 'root', 'password': '992002'}
# model = Model(db_config)
# model.user_exists(
#     'login_in4', {'username': 'admin', 'passwords': '1234567'})
