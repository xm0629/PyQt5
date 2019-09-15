# -*- coding :  utf-8 -*-
# @Data      :  2019-9-15
# @Author    :  Ming Xu
# @Email     :  920972751@qq.com
# @File      :  first.py
# Desctiption:  第一个　PyQt5 程序

import sys

from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == "__main__":
    # 创建　QApplication 类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口尺寸
    w.resize(400, 200)
    # 移动窗口
    w.move(300, 300)
    # 设置窗口标题
    w.setWindowTitle("第一个基于 PyQt5 的桌面应用")
    # 显示窗口
    w.show()

    # 进入程序的主循环, 并通过 exit 函数确保主循环安全结束
    sys.exit(app.exec_())