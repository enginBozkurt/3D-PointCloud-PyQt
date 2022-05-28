'''
Date: 2022-05-28 21:05:41
LastEditors: HeXu
LastEditTime: 2022-05-28 22:09:46
FilePath: /3D-PointCloud-PyQt/helloworld.py
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv) # 创建应用对象, sys.argv 是一组命令行的参数列表, 通过参数进行脚本控制

    w = QWidget()# 用户界面的基本控件,提供了基本的应用构造器,默认下是没有父级的

    w.resize(250, 150)# 调整大小,单位是像素
    
    w.move(300, 300)# 修改位置,原点为左上角

    w.setWindowTitle('Simple')

    w.show()

    sys.exit(app.exec_()) # 进入了应用的主循环中
