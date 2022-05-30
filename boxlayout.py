'''
Date: 2022-05-30 13:35:32
LastEditors: HeXu
LastEditTime: 2022-05-30 16:50:59
FilePath: /3D-PointCloud-PyQt/boxlayout.py
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        okButton = QPushButton("OK", self)
        cancelButton = QPushButton("cancel", self)
        
        hBox = QHBoxLayout()# 一个水平布局
        hBox.addStretch(1)
        hBox.addWidget(okButton)
        hBox.addWidget(cancelButton)
        
        vBox = QVBoxLayout()# 一个垂直布局
        vBox.addStretch(1)
        vBox.addLayout(hBox)
        
        self.setLayout(vBox)
        
        self.setGeometry(300, 300,300, 300)
        self.setWindowTitle("hexu")
        self.show()
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        
        