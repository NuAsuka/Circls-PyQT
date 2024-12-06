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

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, diameter in self.circles:
            pen = QPen(QColor('Yellow'), 2)
            painter.setPen(pen)
            painter.drawEllipse(x, y, diameter, diameter)

    def draw_circle(self):
        width = self.width()
        height = self.height()
        diameter = random.randint(10, 50)
        x = random.randint(0, width - diameter)
        y = random.randint(0, height - diameter)
        self.circles.append((x, y, diameter))
        self.update()  # update


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
