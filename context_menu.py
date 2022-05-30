'''
Date: 2022-05-29 14:35:09
LastEditors: HeXu
LastEditTime: 2022-05-29 14:52:55
FilePath: /3D-PointCloud-PyQt/context_menu.py
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMenu, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("hexu")
        self.show()
        
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        newAct = cmenu.addAction("new")# 三个选项
        openAct = cmenu.addAction("open")
        quitAct = cmenu.addAction("quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))# 显示组建中的相对坐标转为绝对坐标
        if action == quitAct:
            qApp.quit()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())