'''
Date: 2022-05-29 11:23:35
LastEditors: HeXu
LastEditTime: 2022-05-29 13:58:04
FilePath: /3D-PointCloud-PyQt/menu.py
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 定义一个菜单栏按钮
        exitAct = QAction(QIcon("icon.png"), "&退出", self)# 设置icon和按钮文本
        exitAct.setShortcut('Ctrl+Q') #设置快捷键
        exitAct.setStatusTip("Exit application")# 状态栏设置描述
        exitAct.triggered.connect(qApp.quit)# 设置触发动作
        
        self.statusBar()# 创建一个菜单栏
        
        menuBar = self.menuBar()# 创建一个菜单栏
        menuBar.setNativeMenuBar(False)# MacOS需要加上
        fileMenu = menuBar.addMenu('&File')#加一个下拉菜单
        fileMenu.addAction(exitAct)# 菜单中添加按钮
        
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle("hexu6")
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        
    