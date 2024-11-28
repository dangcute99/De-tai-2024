
import mysql.connector
from mysql.connector import Error
from datetime import datetime


class DatabaseConnection:
    def __init__(self, host, username, password):
        self.host = host
        self.user = username
        self.password = password
        self.connection = None

    def check_connection(self):
        try:
            # Tạo kết nối đến MySQL server mà không chỉ định cơ sở dữ liệu
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                status = "Connected to MySQL server"
                return True
            else:
                return False
                # print(status)
        except Error as e:
            status = f"Error: {e}"
            # print(status)
            self.connection = None

    def create_database(self, database_name):
        """Tạo cơ sở dữ liệu nếu chưa tồn tại."""
        if self.connection is None:
            raise Exception("No connection to MySQL server")
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
            # print(f"Database '{database_name}' created successfully.")
        except Error as e:
            print(f"Error while creating database: {e}")
        finally:
            cursor.close()
            # self.connection.close()

    import mysql.connector

    def execute_query(self, query, database):
        """Thực hiện một truy vấn SQL."""
        connec = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=database
        )
        cursor = None  # Khởi tạo biến cursor
        try:
            cursor = connec.cursor()
            cursor.execute(query)

            # Kiểm tra loại truy vấn
            if query.strip().lower().startswith("select"):
                result = cursor.fetchall()  # Đọc kết quả
                return result  # Trả về kết quả

            else:
                connec.commit()  # Chỉ commit nếu không phải là SELECT
                # print("Query executed successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor is not None:  # Chỉ đóng cursor nếu nó đã được gán giá trị
                cursor.close()
            if connec.is_connected():  # Đảm bảo kết nối được đóng
                connec.close()

    def close_connection(self):
        """Đóng kết nối với cơ sở dữ liệu."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Kết nối đã được đóng")

    def insert_value(self, database, table, column, value):
        """Thêm mới một giá trị vào cột chỉ định và tự động thêm timestamp."""
        query = f"""
        INSERT INTO {table} ({column}, timestamp)
        VALUES (%s, %s)
        """
        connec = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=database
        )
        cursor = None
        try:
            cursor = connec.cursor()
            current_time = datetime.now()
            cursor.execute(query, (value, current_time))
            connec.commit()
            print(f"Giá trị '{value}' đã được thêm mới vào cột {
                  column} trong bảng {table}")
        except Error as e:
            print(f"Lỗi: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            connec.close()

    # def insert_multiple_values(self, database, table, data):
    #     """
    #     Thêm nhiều giá trị vào bảng cùng một lúc.

    #     :param database: Tên cơ sở dữ liệu
    #     :param table: Tên bảng
    #     :param data: Dictionary chứa dữ liệu cần chèn
    #     """
    #     timestamp = datetime.now()

    #     columns = ["timestamp"]
    #     values = [timestamp]
    #     placeholders = ["%s"]

    #     for column, value in data.items():
    #         if isinstance(value, dict):
    #             columns.append(column)
    #             values.append(value['value'])
    #             placeholders.append("%s")

    #             if column in ['temperature', 'humidity']:
    #                 columns.append(f"{column}_low")
    #                 columns.append(f"{column}_high")
    #                 values.append(value.get('low', None))
    #                 values.append(value.get('high', None))
    #                 placeholders.extend(["%s"] * 2)
    #             elif column in ['dc1_voltage', 'dc2_voltage']:
    #                 columns.append(f"{column}_low_1")
    #                 columns.append(f"{column}_low_2")
    #                 columns.append(f"{column}_high")
    #                 values.append(value.get('low_1', None))
    #                 values.append(value.get('low_2', None))
    #                 values.append(value.get('high', None))
    #                 placeholders.extend(["%s"] * 3)
    #         else:
    #             columns.append(column)
    #             values.append(value)
    #             placeholders.append("%s")

    #     columns_str = ", ".join(columns)
    #     placeholders_str = ", ".join(placeholders)

    #     query = f"""
    #     INSERT INTO {table} ({columns_str})
    #     VALUES ({placeholders_str})
    #     """

    #     connec = mysql.connector.connect(
    #         host=self.host,
    #         user=self.user,
    #         password=self.password,
    #         database=database
    #     )
    #     cursor = None
    #     try:
    #         cursor = connec.cursor()
    #         cursor.execute(query, values)
    #         connec.commit()
    #         print(f"Đã thêm mới {len(data)} giá trị vào bảng {table}")
    #     except Error as e:
    #         print(f"Lỗi: {e}")
    #     finally:
    #         if cursor is not None:
    #             cursor.close()
    #         connec.close()

    def insert_multiple_values(self, database, table, data):
        """
        Thêm nhiều giá trị vào bảng cùng một lúc.

        :param database: Tên cơ sở dữ liệu
        :param table: Tên bảng
        :param data: Dictionary chứa dữ liệu cần chèn, dạng {"username": "da", "password": ""}
        """
        # Lấy thời gian hiện tại cho cột timestamp
        timestamp = datetime.now()

        # Khởi tạo danh sách cột và giá trị
        columns = ["timestamp"]
        values = [timestamp]
        placeholders = ["%s"]

        # Thêm các cột và giá trị từ data
        for column, value in data.items():
            columns.append(column)
            values.append(value)
            placeholders.append("%s")

        # Chuẩn bị câu truy vấn
        columns_str = ", ".join(columns)
        placeholders_str = ", ".join(placeholders)

        query = f"""
        INSERT INTO {table} ({columns_str})
        VALUES ({placeholders_str})
        """

        # Thực hiện kết nối với cơ sở dữ liệu và chèn dữ liệu
        connec = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=database
        )
        cursor = None
        try:
            cursor = connec.cursor()
            cursor.execute(query, values)
            connec.commit()
            print(f"Đã thêm mới một bản ghi vào bảng {table}")
        except Error as e:
            print(f"Lỗi: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            connec.close()

    def get_cell_value_by_id(self, database, table, column, id):
        query = f"""
        SELECT {column}
        FROM {table}
        WHERE id = %s
        """
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=database
        )
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            result = cursor.fetchone()
            if result is not None:
                if result[0] is None:
                    print(f"Giá trị của ô (id={id}, cột={column}) là NULL")
                    return None
                else:
                    return result[0]
            else:
                print(f"Không tìm thấy dữ liệu cho id={id}")
                return None
        except Error as e:
            print(f"Lỗi: {e}")
            return None
        finally:
            if cursor is not None:
                cursor.close()
            connection.close()

    def get_x_notnull(self, database, table, column, x=20):
        # Kiểm tra xem cột có tồn tại không
        valid_columns = self.get_valid_columns(database, table)
        if column not in valid_columns:
            print(f"Lỗi: Cột '{column}' không tồn tại trong bảng '{table}'")
            return None

        query = f"""
        SELECT id, `{column}`, timestamp
        FROM `{table}`
        WHERE `{column}` IS NOT NULL
        ORDER BY timestamp DESC
        LIMIT %s
        """

        connec = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=database
        )
        cursor = None
        try:
            cursor = connec.cursor(dictionary=True)
            cursor.execute(query, (x,))
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Lỗi SQL: {e}")
            return None
        finally:
            if cursor is not None:
                cursor.close()
            connec.close()

    def get_valid_columns(self, database, table):
        query = f"""
        SHOW COLUMNS FROM {table}
        """
        connec = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=database
        )
        cursor = None
        try:
            cursor = connec.cursor()
            cursor.execute(query)
            columns = [row[0] for row in cursor.fetchall()]
            return columns
        except Error as e:
            print(f"Lỗi: {e}")
            return None
        finally:
            if cursor is not None:
                cursor.close()
            connec.close()

    def update_row(self, database, table, id, data):
        """
        Cập nhật dữ liệu của một hàng trong bảng dựa trên ID.

        :param database: Tên cơ sở dữ liệu
        :param table: Tên bảng
        :param id: ID của hàng cần cập nhật
        :param data: Dictionary chứa các cột và giá trị cần cập nhật
        :return: True nếu cập nhật thành công, False nếu có lỗi
        """
        set_clauses = []
        values = []
        for key, value in data.items():
            if isinstance(value, dict):
                # Xử lý trường hợp giá trị là một dictionary
                for sub_key, sub_value in value.items():
                    if sub_key == 'value':
                        set_clauses.append(f"`{key}` = %s")
                        values.append(sub_value)
                    else:
                        set_clauses.append(f"`{key}_{sub_key}` = %s")
                        values.append(sub_value)
            else:
                set_clauses.append(f"`{key}` = %s")
                values.append(value)

        set_clause = ", ".join(set_clauses)
        query = f"""
        UPDATE `{table}`
        SET {set_clause}
        WHERE id = %s
        """

        values.append(id)

        connec = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=database
        )
        cursor = None
        try:
            cursor = connec.cursor()
            cursor.execute(query, values)
            connec.commit()
            if cursor.rowcount > 0:
                print(f"Đã cập nhật hàng có ID {id} trong bảng {table}")
                return True
            else:
                print(f"Không tìm thấy hàng có ID {id} trong bảng {
                      table} hoặc không có thay đổi")
                return False
        except Error as e:
            print(f"Lỗi khi cập nhật hàng: {e}")
            return False
        finally:
            if cursor is not None:
                cursor.close()
            connec.close()

    def check_in4(self, database, table, username, password):
        """
        Kiểm tra xem username và password có đúng không.

        :param database: Tên cơ sở dữ liệu
        :param table: Tên bảng chứa thông tin đăng nhập
        :param username: Tên đăng nhập cần kiểm tra
        :param password: Mật khẩu cần kiểm tra
        :return: True nếu thông tin đăng nhập đúng, False nếu sai
        """
        query = f"""
        SELECT * FROM `{table}`
        WHERE username = %s AND passwords = %s
        """

        connec = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=database
        )
        cursor = None
        try:
            cursor = connec.cursor(dictionary=True)
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            if result:
                print("Đăng nhập thành công")
                return True
            else:
                print("Tên đăng nhập hoặc mật khẩu không đúng")
                return False
        except Error as e:
            print(f"Lỗi khi kiểm tra thông tin đăng nhập: {e}")
            return False
        finally:
            if cursor is not None:
                cursor.close()
            connec.close()

# Ví dụ sử dụng
# conn = create_connection()
# if conn:
#     create_database(conn, 'your_database')  # Cung cấp tên cơ sở dữ liệu ở đây
#     close_connection(conn)
