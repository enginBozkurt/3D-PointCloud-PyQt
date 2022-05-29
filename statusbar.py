'''
Date: 2022-05-29 11:15:47
LastEditors: HeXu
LastEditTime: 2022-05-29 11:22:30
FilePath: /3D-PointCloud-PyQt/statusbar.py
'''
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar().showMessage("HELLO")
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Hexu5")
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())