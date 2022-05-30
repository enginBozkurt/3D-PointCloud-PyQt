'''
Date: 2022-05-29 14:10:02
LastEditors: HeXu
LastEditTime: 2022-05-29 14:34:32
FilePath: /3D-PointCloud-PyQt/checkable_menu.py
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("this is a statusbar")
        
        menubar = self.menuBar()# 定义菜单栏
        menubar.setNativeMenuBar(False)
        viewMenu1 = menubar.addMenu('菜单一')# 添加两个首选项
        viewMenu2 = menubar.addMenu('菜单二')
        
        viewStatAct = QAction('view statusbar', self, checkable = True)#设置一个按钮
        viewStatAct.setStatusTip('view statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)# 绑定按钮动作
        
        viewMenu1.addAction(viewStatAct)
        
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("hexu8")
        self.show()
    def toggleMenu(self, status):
        if status :
            self.statusbar.show()
        else :
            self.statusbar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())