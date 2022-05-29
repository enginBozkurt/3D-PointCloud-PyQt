'''
Date: 2022-05-28 22:23:22
LastEditors: HeXu
LastEditTime: 2022-05-28 22:37:55
FilePath: /3D-PointCloud-PyQt/a_tooltip_on_ a_window_and_a_button.py
'''
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))# 设置了一个提示框
        self.setToolTip("This is a <b> QWidget </b> widget")# 设置提示框的字体内容,可以富文本
        
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("hexu2")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
