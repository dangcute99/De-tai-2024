from PyQt6.QtWidgets import QApplication, QMainWindow, QToolButton, QVBoxLayout, QWidget, QHBoxLayout, QCheckBox
from PyQt6.QtGui import QIcon


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QToolButton Example with Status CheckBox")

        # Tạo một widget chính
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Tạo layout
        layout = QVBoxLayout(central_widget)

        # Tạo một layout ngang cho nút và trạng thái
        h_layout = QHBoxLayout()

        # Tạo QToolButton
        self.tool_button = QToolButton()
        self.tool_button.setIcon(
            QIcon(r"C:\Users\ASUS\OneDrive\My Computer\ui\MVC BUILD\picture\anh1.png"))
        self.tool_button.setText('Click Me')
        self.tool_button.setCheckable(True)

        # Kết nối sự kiện
        self.tool_button.clicked.connect(self.on_button_clicked)

        # Tạo QCheckBox để hiển thị trạng thái
        self.status_check_box = QCheckBox("Status: Off")
        # Không cho phép người dùng thay đổi trạng thái
        self.status_check_box.setEnabled(False)

        # Thêm nút và trạng thái vào layout ngang
        h_layout.addWidget(self.tool_button)
        h_layout.addWidget(self.status_check_box)

        # Thêm layout ngang vào layout chính
        layout.addLayout(h_layout)

    def on_button_clicked(self):
        # Thay đổi trạng thái khi nút được nhấn
        if self.tool_button.isChecked():
            self.status_check_box.setText("Status: On")
            self.status_check_box.setChecked(True)
        else:
            self.status_check_box.setText("Status: Off")
            self.status_check_box.setChecked(False)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
