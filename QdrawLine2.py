## Ex 4-1. 절대적 배치.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont, QPainter, QPen
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.setFont(QFont("맑은고딕", 20))
        label1.setStyleSheet("color: black;"
                             "border-style: solid;"
                             "border-width: 2px;"
                             "border-color: black;"
                             "border-radius: 3px")
        label1.setFixedSize(100, 100)
        label1.move(100, 100)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)

        self.setWindowTitle('Absolute Positioning')
        #self.setGeometry(300, 300, 700, 600)
        self.setFixedSize(700, 600)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_line(qp)
        qp.end()

    def draw_line(self, qp):
        qp.setPen(QPen(Qt.red, 20))
        qp.drawLine(31, 235, 130, 235)
        qp.setPen(QPen(Qt.gray, 20))
        qp.drawLine(31, 265, 50, 265)
        qp.setPen(QPen(Qt.blue, 20))
        qp.drawLine(31, 295, 100, 295)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())