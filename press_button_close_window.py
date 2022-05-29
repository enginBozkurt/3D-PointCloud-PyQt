'''
Date: 2022-05-28 22:39:53
LastEditors: HeXu
LastEditTime: 2022-05-29 10:11:11
FilePath: /3D-PointCloud-PyQt/press_button_close_window.py
'''
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 100)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("hexu3")
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
 