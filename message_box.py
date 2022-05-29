'''
Date: 2022-05-29 10:11:37
LastEditors: HeXu
LastEditTime: 2022-05-29 10:29:13
FilePath: /3D-PointCloud-PyQt/message_box.py
'''

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()
        
    def InitUI(self):
        self.setGeometry(300, 300, 200 , 200)
        self.setWindowTitle("hexu4")
        self.show()
        
    def closeEvent(self, event):# 关闭QWidget,会产生一个QCloseEvent,并且会闯入到closeEvent的event参数中
        reply = QMessageBox.question(self, 'message', "r u quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())