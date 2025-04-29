from model import Model
import sys
sys.path.append(r'c:\Users\ASUS\OneDrive\My Computer\ui\MVC BUILD')


db_config = {'host': 'localhost', 'username': 'root', 'password': '992002'}
model = Model(db_config)

# model.get_lan_value("192.168.0.1", "aht temp", "192.168.0.1,aht temperature, 30.4")
# model.get_lan_value("192.168.0.1", "humi", "192.168.0.1,humi, 50")
# model.get_lan_value("192.168.0.1", "dc", "192.168.0.1,dc, 12")

model.start_server()
model.get_threshold_data_from_device(
    "192.168.0.1", "192.168.0.1,temp threshold, 30.4,40.4")
model.get_sensor_data_from_device(
    "192.168.0.1", "192.168.0.1,aht temperature, 30.4")
