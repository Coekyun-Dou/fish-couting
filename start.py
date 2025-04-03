import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from main.login import Login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    # login.setObjectName("MainWindow")
    # login.setStyleSheet("#MainWindow{border-image:url(img/icon/background.jpg)}") 设置背景
    login.setWindowIcon(QIcon("img/imageonline-co-pngtoicoimage.ico"))
    login.show()
    sys.exit(app.exec_())
