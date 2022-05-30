'''
Date: 2022-05-30 13:27:52
LastEditors: HeXu
LastEditTime: 2022-05-30 13:33:55
FilePath: /3D-PointCloud-PyQt/absolute_position.py
'''
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        labl1 = QLabel("Labl1", self)
        labl1.move(15, 10)
        
        labl1 = QLabel("Labl1", self)
        labl1.move(15, 50)
        
        labl1 = QLabel("Labl1", self)
        labl1.move(15, 100)
        
        labl1 = QLabel("Labl1", self)
        labl1.move(15, 200)
        
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("hexu")
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())