'''
Date: 2022-05-30 17:19:02
LastEditors: HeXu
LastEditTime: 2022-05-30 21:31:41
FilePath: /3D-PointCloud-PyQt/QGridLayout_manager.py
'''
import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QTextEdit, QLineEdit, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        title = QLabel("title")
        author = QLabel("author")
        review = QLabel("review")
        
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        
        grid = QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        
        self.setLayout(grid)
        
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("hxu1")
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())