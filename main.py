import sys
from math import sin, cos, pi
from random import randint

from PyQt6.QtCore import QPointF, QRectF, Qt
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.drawf)
        self.setMouseTracking(True)
        self.qp = QPainter()
        self.flag = False
        self.status = None

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        coord1 = randint(100, 400)
        coord2 = randint(100, 400)
        R = randint(20, 100)
        self.qp.drawEllipse(QPointF(coord1, coord2), R, R)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())