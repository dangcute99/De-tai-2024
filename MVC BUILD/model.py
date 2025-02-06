from datetime import datetime
import json
from db_connection import DatabaseConnection
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
db_config = {'host': 'localhost', 'username': 'root', 'password': '992002'}
model = Model(db_config)
model.user_exists(
    'login_in4', {'username': 'admin', 'passwords': '1234567'})
