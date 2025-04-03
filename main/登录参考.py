from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QMainWindow, QWidget, QMessageBox
import pymysql



class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(629, 491)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(130, 260, 71, 41))
        self.label.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(True)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(130, 320, 71, 41))
        self.label_2.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setMouseTracking(True)
        self.label_2.setTabletTracking(True)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 380, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.userName = QtWidgets.QLineEdit(Form)
        self.userName.setGeometry(QtCore.QRect(220, 260, 271, 41))
        self.userName.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.userName.setObjectName("lineEdit")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(220, 320, 271, 41))
        self.password.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 380, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 521, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(240, 30, 191, 121))
        pixmap = QPixmap('icon/conan1.png')
        pixmap = pixmap.scaled(self.label_4.width(), self.label_4.height(), Qt.KeepAspectRatio)
        self.label_4.setPixmap(pixmap)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.showdialog)  # type: ignore
        self.pushButton_2.clicked.connect(self.userName.clear)  # type: ignore
        self.pushButton_2.clicked.connect(self.password.clear)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "海上风电叶片缺陷检测系统"))
        self.label.setText(_translate("Form", "账号："))
        self.label_2.setText(_translate("Form", "密码："))
        self.pushButton.setText(_translate("Form", "登录"))
        self.userName.setText(_translate("Form", "请输入账号"))
        self.password.setText(_translate("Form", "请输入密码"))
        self.pushButton_2.setText(_translate("Form", "清空"))
        self.label_3.setText(_translate("Form", "AI应用创新团队海上风电叶片检测系统"))

    def showdialog(self):
        dlg = QDialog()
        dlg.setWindowTitle("Succeed")
        dlg.setWindowModality(Qt.ApplicationModal)
        icon =(QIcon("img/imageonline-co-pngtoicoimage.ico")) # 替换为您实际的图标文件路径
        dlg.setWindowIcon(icon)
        # 添加文本信息
        label = QLabel(dlg)
        label.setText("登录成功！")
        label.move(50, 50)

        # 添加确定按钮
        button = QPushButton('确定', dlg)
        button.move(50, 80)
        button.clicked.connect(self.showMainSystem)
        button.clicked.connect(dlg.close)
        dlg.exec_()

    def login_button(self):
        Login_User = self.userName.text()
        Login_Passwd = self.password.text()
        if Login_User == 0 or Login_Passwd == '':
            QMessageBox.information(self, "error", "输入错误")
        else:
            conn = pymysql.connect(
                host='192.168.10.3',  # 连接主机, 默认127.0.0.1
                user='root',  # 用户名
                passwd='123456',  # 密码
                port=3306,  # 端口，默认为3306
                db='hsfdSystem',  # 数据库名称
                charset='utf8'  # 字符编码
            )
            # 生成游标对象 cursor
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM `hsfdsystem`.`usertable` WHERE `user`='{Login_User}'")
            data = cursor.fetchone()
            if data is None:
                QMessageBox.information(self, "user is not exist", "用户名不存在")
            else:
                if data[1] == Login_Passwd:
                    self.showdialog()
                    self.close()
                else:
                    QMessageBox.information(self, "password error", "密码错误")
            cursor.close()  # 关闭游标
            conn.close()  # 关闭连接

    def showMainSystem(self):
        # 做好其他窗口后先import进来后就简单调用就ok了
        from main_win.win import MainWindow
        self.w1 = MainWindow()
        self.w1.show()
