from model import Model

db_config = {'host': 'localhost', 'username': 'root', 'password': '992002'}
model = Model(db_config)

#######################################
# test server
# model.start_server()
# model.receive_data("172.20.10.10", 2380)
######################################
# test figure
data = model.get_x_firgue_data('data', 'temp1_value', 'temp1', 2)
print(data)
