import sys
import random
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QRect


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle("Circles")
        self.pushButton1.clicked.connect(self.draw_circle)
        self.circles = []

    def random_color_hsv(self):
        h = random.randint(0, 360)
        s = random.randint(0, 255)
        v = random.randint(128, 255)
        return QColor.fromHsv(h, s, v)

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, diameter, color in self.circles:
            pen = QPen(color, 2)
            painter.setPen(pen)
            painter.drawEllipse(x, y, diameter, diameter)

    def draw_circle(self):
        width = self.width()
        height = self.height()
        diameter = random.randint(10, 50)
        x = random.randint(0, width - diameter)
        y = random.randint(0, height - diameter)
        color = self.random_color_hsv()
        self.circles.append((x, y, diameter, color))
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
