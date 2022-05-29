'''
Date: 2022-05-28 22:12:32
LastEditors: HeXu
LastEditTime: 2022-05-28 22:22:08
FilePath: /3D-PointCloud-PyQt/icon_in_the_title_bar.py
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget): #面向对象的编程,继承QWidget
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('hexu')
        self.setWindowIcon(QIcon('icon.png'))
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    


