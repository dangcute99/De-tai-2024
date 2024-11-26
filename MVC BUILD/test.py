from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QPoint, QEvent


def create_draggable_button(parent=None):
    # Tạo đối tượng nút bấm kéo
    button = QPushButton("Drag me", parent)

    # Cấu hình font tooltip toàn cục
    QToolTip.setFont(QFont('Arial', 10))

    # Cấu hình nút
    button.setFixedSize(100, 100)
    button.setStyleSheet("""
        QPushButton {
            background-color: lightblue;
            border: 2px solid black;
            border-radius: 50px;
            color: black;
        }
        QPushButton:hover {
            background-color: skyblue;
        }
    """)

    # Bật theo dõi chuột
    button.setMouseTracking(True)

    # Thuộc tính kéo
    button._drag_active = False
    button._drag_start_position = None

    # Xử lý sự kiện tooltip khi chuột vào nút
    def event(event):
        if event.type() == QEvent.Type.ToolTip:
            QToolTip.showText(
                button.mapToGlobal(event.pos()),
                "HDSD: Kéo nút hoặc nhấn đúp chuột!"
            )
            return True
        return super(QPushButton, button).event(event)

    # Hiển thị tooltip khi chuột vào nút
    def enterEvent(event):
        QToolTip.showText(
            button.mapToGlobal(QPoint(0, 0)),
            "HDSD: Kéo nút hoặc nhấn đúp chuột!"
        )
        # print("Chuột đã vào nút")
        super(QPushButton, button).enterEvent(event)

    # Bắt đầu kéo
    def mousePressEvent(event):
        if event.button() == Qt.MouseButton.LeftButton:
            button._drag_active = True
            # Lưu vị trí bắt đầu kéo
            button._drag_start_position = event.globalPosition().toPoint() - button.pos()
            # print("Bắt đầu kéo")
        super(QPushButton, button).mousePressEvent(event)

    # Di chuyển nút khi kéo
    def mouseMoveEvent(event):
        if button._drag_active and event.buttons() == Qt.MouseButton.LeftButton:
            # Di chuyển nút
            new_pos = event.globalPosition().toPoint() - button._drag_start_position
            button.move(new_pos)
            # print(f"Đang kéo đến vị trí: {new_pos}")
        super(QPushButton, button).mouseMoveEvent(event)

    # Kết thúc kéo
    def mouseReleaseEvent(event):
        if event.button() == Qt.MouseButton.LeftButton:
            button._drag_active = False
            # print("Kết thúc kéo")
        super(QPushButton, button).mouseReleaseEvent(event)

    # Nhấn đúp chuột
    def mouseDoubleClickEvent(event):
        if event.button() == Qt.MouseButton.LeftButton:
            print("Nhấn đúp!")
        super(QPushButton, button).mouseDoubleClickEvent(event)

    # Gán các phương thức vào button
    button.event = event
    button.enterEvent = enterEvent
    button.mousePressEvent = mousePressEvent
    button.mouseMoveEvent = mouseMoveEvent
    button.mouseReleaseEvent = mouseReleaseEvent
    button.mouseDoubleClickEvent = mouseDoubleClickEvent

    return button


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Draggable Button Test")
        self.setGeometry(100, 100, 600, 400)

        # Gọi hàm tạo nút kéo
        self.button = create_draggable_button(self)
        self.button.move(250, 150)  # Đặt vị trí ban đầu của nút


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
