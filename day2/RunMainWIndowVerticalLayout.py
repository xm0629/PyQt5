# -*- coding :  utf-8 -*-
# @Data      :  2019-9-15
# @Author    :  Ming Xu
# @Email     :  920972751@qq.com
# @File      :  RunMainWIndowVerticalLayout.py
# Desctiption:  垂直控件设置


import sys

import MainWIndowVerticalLayout

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWIndowVerticalLayout.Ui_MainWindow()
    # 向主窗口添加控件
    ui.setupUi(mainWindow)
    # 显示主窗口
    mainWindow.show()
    sys.exit(app.exec_())
