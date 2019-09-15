# -*- coding :  utf-8 -*-
# @Data      :  2019-9-15
# @Author    :  Ming Xu
# @Email     :  920972751@qq.com
# @File      :  RunMainWindowCallLayout.py
# Desctiption:  ui 的设置文件


import sys

import RunMainWindowLayout

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = RunMainWindowLayout.Ui_MainWindow()
    # 向主窗口添加控件
    ui.setupUi(mainWindow)
    # 显示主窗口
    mainWindow.show()
    sys.exit(app.exec_())

