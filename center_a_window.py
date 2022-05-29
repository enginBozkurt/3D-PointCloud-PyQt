'''
Date: 2022-05-29 10:29:39
LastEditors: HeXu
LastEditTime: 2022-05-29 11:11:38
FilePath: /3D-PointCloud-PyQt/center_a_window.py
'''
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication #QDesktopWidget提供了用户的桌面信息，包括屏幕的大小。

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("hexu4")
        self.resize(250, 150)
        self.center()
        self.show()
        
    def center(self):
        qr = self.frameGeometry()# 获得主窗口所在的框架
        cp = QDesktopWidget().availableGeometry().center()# 获得显示器的中点
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        
