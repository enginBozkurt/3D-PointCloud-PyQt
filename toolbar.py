'''
Date: 2022-05-29 14:53:01
LastEditors: HeXu
LastEditTime: 2022-05-29 15:07:17
FilePath: /3D-PointCloud-PyQt/toolbar.py
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QMenu, QApplication, qApp, QApplication, QAction
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        exitAct = QAction(QIcon("icon.png"), '退出', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)
        
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("hexu")
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())