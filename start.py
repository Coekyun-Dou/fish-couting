import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from main.login import Login
from main.innerface import MainWindow  # 导入第一个 UI

import res_rc



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # login_window = Login()
    login_window = MainWindow()

    # login.setObjectName("MainWindow")
    # login.setStyleSheet("#MainWindow{border-image:url(img/icon/fish.jpg)}") #设置背景
    # login.setWindowIcon(QIcon("img/imageonline-co-pngtoicoimage.ico"))
    # ui = Login()  # Ui_Form 是由 Qt Designer 转换成的类名
    # ui.setupUi(login_window)  # 在主窗口中设置 UI
    login_window.show()
    sys.exit(app.exec_())


