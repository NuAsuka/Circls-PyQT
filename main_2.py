import sys
import random
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QRect


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circles")
        self.button = QPushButton("Draw Circle", self)
        self.button.clicked.connect(self.draw_circle)
        self.circles = []
        self.button.setGeometry(10, 10, 100, 30)
        self.setGeometry(0, 0, 500, 500)

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


import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QRect


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Circles")
        self.button = QPushButton("Draw Circle", self)
        self.button.clicked.connect(self.draw_circle)
        self.button.setGeometry(10, 10, 100, 30)

        self.circles = []  # Список для хранения данных о кругах

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing) # Сглаживание

        for x, y, diameter in self.circles:
            pen = QPen(QColor("yellow"), 2) # Толщина линии
            painter.setPen(pen)
            painter.drawEllipse(x, y, diameter, diameter)

    def draw_circle(self):
        width = self.width()
        height = self.height()
        diameter = random.randint(10, 50)  # Диаметр от 10 до 50 пикселей
        x = random.randint(0, width - diameter)
        y = random.randint(0, height - diameter)
        self.circles.append((x, y, diameter))
        self.update() # Перерисовываем форму


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
