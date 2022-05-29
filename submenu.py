'''
Date: 2022-05-29 13:59:21
LastEditors: HeXu
LastEditTime: 2022-05-29 14:08:44
FilePath: /3D-PointCloud-PyQt/submenu.py
'''
import sys
from tkinter import E
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QMenu

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        menuBar = self.menuBar()# 初始化一个菜单栏
        menuBar.setNativeMenuBar(False)# MacOS需要加上
        
        fileMenu = menuBar.addMenu('菜单')# 菜单栏上添加一个菜单
        
        imMenu = QMenu('Import', self)# 初始化一个下拉选项
        imAct = QAction('Import Mail', self)# 添加一个选项
        imMenu.addAction(imAct)
        
        newAct = QAction('New', self)# 添加一个选项
        
        fileMenu.addAction(newAct)
        fileMenu.addMenu(imMenu)
        
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("hexu7")
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
    