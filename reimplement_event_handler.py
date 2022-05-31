'''
Date: 2022-05-31 09:24:26
LastEditors: HeXu
LastEditTime: 2022-05-31 09:31:52
FilePath: /3D-PointCloud-PyQt/reimplement_event_handler.py
'''
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__();
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("hexu")
        self.show()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        