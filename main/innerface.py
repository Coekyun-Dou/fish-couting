import threading
import mss
import traceback
#pyqt5库的引用
from PyQt5.QtCore import QResource, Qt, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMenu, QAction, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import Qt, QPoint, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap, QPainter, QIcon, QPalette, QBrush
#图像处理和深度学习相关的导入
import sys
import json
import numpy as np
import torch
import os
import time
import cv2
from bokeh.server.tornado import psutil
from mypy.checker import defaultdict
from torch.cpu import synchronize
from ultralytics import YOLO

#Web引擎相关的导入
from MouseLabel import Label_click_Mouse
from test.captureScreen import boxScreen
from utils.augmentations import letterbox
from utils.datasets import LoadImages, LoadWebcam, LoadStreams
from utils.CustomMessageBox import MessageBox
from utils.general import non_max_suppression, scale_coords
from utils.plots import colors, Annotator
from utils.torch_utils import select_device
from dialog.rtsp_win import Window

QResource.registerResource("apprcc.qrc")
class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1081, 713)
        mainWindow.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icon/图片1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("#mainWindow{border:none;}")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_18 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_18.setStyleSheet("#groupBox_18{\n"
"    border-image: url(:/icons/icons/fish.jpg);\n"
"border: 0px solid #42adff;\n"
"border-radius:5px;}")
        self.groupBox_18.setTitle("")
        self.groupBox_18.setObjectName("groupBox_18")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_18)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_18)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 45))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 45))
        self.groupBox.setStyleSheet("#groupBox{\n"
"background-color: rgba(75, 75, 75, 200);\n"
"border: 0px solid #42adff;\n"
"border-left: 0px solid rgba(29, 83, 185, 255);\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-bottom: 1px solid rgba(200, 200, 200,100);\n"
";\n"
"border-radius:0px;}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setMinimumSize(QtCore.QSize(40, 40))
        self.label_7.setMaximumSize(QtCore.QSize(40, 40))
        self.label_7.setStyleSheet("image: url(:/img/icon/conan.png);\n"
"image: url(:/images/icons/logonew.png)")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 24px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.minButton = QtWidgets.QPushButton(self.groupBox)
        self.minButton.setMinimumSize(QtCore.QSize(50, 28))
        self.minButton.setMaximumSize(QtCore.QSize(50, 28))
        self.minButton.setStyleSheet("QPushButton {\n"
"\n"
"    image: url(:/icons/icons/最小化.png);\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.minButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/icon/最小化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minButton.setIcon(icon1)
        self.minButton.setObjectName("minButton")
        self.horizontalLayout_5.addWidget(self.minButton)
        self.maxButton = QtWidgets.QPushButton(self.groupBox)
        self.maxButton.setMinimumSize(QtCore.QSize(50, 28))
        self.maxButton.setMaximumSize(QtCore.QSize(50, 28))
        self.maxButton.setStyleSheet("QPushButton {\n"
"    image: url(:/icons/icons/最大化.png);\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.maxButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/icon/正方形.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/img/icon/还原.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap(":/img/icon/还原.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.maxButton.setIcon(icon2)
        self.maxButton.setCheckable(True)
        self.maxButton.setObjectName("maxButton")
        self.horizontalLayout_5.addWidget(self.maxButton)
        self.closeButton = QtWidgets.QPushButton(self.groupBox)
        self.closeButton.setMinimumSize(QtCore.QSize(50, 28))
        self.closeButton.setMaximumSize(QtCore.QSize(50, 28))
        self.closeButton.setStyleSheet("QPushButton {\n"
"    image: url(:/icons/icons/关闭.png);\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.closeButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/icon/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_5.addWidget(self.closeButton)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_18)
        self.groupBox_8.setMinimumSize(QtCore.QSize(320, 0))
        self.groupBox_8.setMaximumSize(QtCore.QSize(320, 16777215))
        self.groupBox_8.setStyleSheet("#groupBox_8{\n"
"background-color: rgba(75, 75, 75, 200);\n"
"border: 0px solid #42adff;\n"
"border-radius:0px;}\n"
"")
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(11)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 42))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 42))
        self.groupBox_2.setStyleSheet("#groupBox_2{\n"
"border: 0px solid #42adff;\n"
"border-bottom: 1px solid rgba(200, 200, 200,100);\n"
"border-radius:0px;}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_35.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 22px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"\n"
"}\n"
"")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_35.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(37, 39, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem1)
        self.verticalLayout_8.addWidget(self.groupBox_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, -1, 11, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_8)
        self.label_3.setMinimumSize(QtCore.QSize(0, 28))
        self.label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 28))
        self.comboBox.setStyleSheet("QComboBox QAbstractItemView {\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"background:rgba(200, 200, 200,150);\n"
"selection-background-color: rgba(200, 200, 200,50);\n"
"color: rgb(218, 218, 218);\n"
"outline:none;\n"
"border:none;}\n"
"QComboBox{\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"color: rgb(218, 218, 218);\n"
"border-width:0px;\n"
"border-color:white;\n"
"border-style:solid;\n"
"background-color: rgba(200, 200, 200,0);}\n"
"\n"
"QComboBox::drop-down {\n"
"margin-top:8;\n"
"height:20;\n"
"background:rgba(255,255,255,0);\n"
"    border-image: url(:/icons/icons/下拉_白色.png);\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(11, -1, 0, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_8)
        self.label_10.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_10.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_5.setStyleSheet("#groupBox_5{\n"
"background-color: rgba(48,148,243,0);\n"
"border: 0px solid #42adff;\n"
"border-left: 0px solid #d9d9d9;\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-radius:0px;}")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.fileButton = QtWidgets.QPushButton(self.groupBox_5)
        self.fileButton.setMinimumSize(QtCore.QSize(55, 28))
        self.fileButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.fileButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"    image: url(:/icons/icons/打开.png);\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(200, 200, 200,0);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        self.fileButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/icon/打开.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileButton.setIcon(icon4)
        self.fileButton.setObjectName("fileButton")
        self.horizontalLayout_8.addWidget(self.fileButton)
        self.cameraButton = QtWidgets.QPushButton(self.groupBox_5)
        self.cameraButton.setMinimumSize(QtCore.QSize(55, 28))
        self.cameraButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.cameraButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"    image: url(:/icons/icons/摄像头开.png);\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(48,148,243,0);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        self.cameraButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/icon/摄像头开.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cameraButton.setIcon(icon5)
        self.cameraButton.setObjectName("cameraButton")
        self.horizontalLayout_8.addWidget(self.cameraButton)
        self.rtspButton = QtWidgets.QPushButton(self.groupBox_5)
        self.rtspButton.setMinimumSize(QtCore.QSize(55, 28))
        self.rtspButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.rtspButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"    image: url(:/icons/icons/实时视频流解析.png);\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(48,148,243,0);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        self.rtspButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/icon/实时视频流解析.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rtspButton.setIcon(icon6)
        self.rtspButton.setObjectName("rtspButton")
        self.horizontalLayout_8.addWidget(self.rtspButton)
        self.horizontalLayout_11.addWidget(self.groupBox_5)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_11)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_8)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.iouSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.iouSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.iouSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.iouSpinBox.setStyleSheet("QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"    image: url(:/icons/icons/箭头_列表展开.png);\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"    image: url(:/icons/icons/箭头_列表收起.png);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"")
        self.iouSpinBox.setMaximum(1.0)
        self.iouSpinBox.setSingleStep(0.01)
        self.iouSpinBox.setProperty("value", 0.45)
        self.iouSpinBox.setObjectName("iouSpinBox")
        self.horizontalLayout_4.addWidget(self.iouSpinBox)
        self.iouSlider = QtWidgets.QSlider(self.groupBox_8)
        self.iouSlider.setStyleSheet("QSlider{\n"
"border-color: #bcbcbc;\n"
"color:#d9d9d9;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"     border: 1px solid #999999;\n"
"     height: 3px;\n"
"    margin: 0px 0;\n"
"     left: 5px; right: 5px;\n"
" }\n"
"QSlider::handle:horizontal {\n"
"     border: 0px ;\n"
"     border-image: url(:/img/icon/圆.png);\n"
"     width:15px;\n"
"     margin: -7px -7px -7px -7px;\n"
"}\n"
"QSlider::add-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9);\n"
"\n"
"}\n"
"QSlider::sub-page:horizontal{\n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);\n"
"}")
        self.iouSlider.setMaximum(100)
        self.iouSlider.setProperty("value", 45)
        self.iouSlider.setOrientation(QtCore.Qt.Horizontal)
        self.iouSlider.setObjectName("iouSlider")
        self.horizontalLayout_4.addWidget(self.iouSlider)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_8)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.confSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.confSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.confSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.confSpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.confSpinBox.setStyleSheet("QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"    image: url(:/icons/icons/箭头_列表收起.png);\n"
"    image: url(:/icons/icons/箭头_列表展开.png);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"    image: url(:/icons/icons/箭头_列表收起.png);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"")
        self.confSpinBox.setMaximum(1.0)
        self.confSpinBox.setSingleStep(0.01)
        self.confSpinBox.setProperty("value", 0.25)
        self.confSpinBox.setObjectName("confSpinBox")
        self.horizontalLayout_3.addWidget(self.confSpinBox)
        self.confSlider = QtWidgets.QSlider(self.groupBox_8)
        self.confSlider.setStyleSheet("QSlider{\n"
"border-color: #bcbcbc;\n"
"color:#d9d9d9;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"     border: 1px solid #999999;\n"
"     height: 3px;\n"
"    margin: 0px 0;\n"
"     left: 5px; right: 5px;\n"
" }\n"
"QSlider::handle:horizontal {\n"
"     border: 0px ;\n"
"     border-image: url(:/img/icon/圆.png);\n"
"     width:15px;\n"
"     margin: -7px -7px -7px -7px;\n"
"}\n"
"QSlider::add-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9);\n"
"\n"
"}\n"
"QSlider::sub-page:horizontal{\n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);\n"
"}")
        self.confSlider.setMaximum(100)
        self.confSlider.setProperty("value", 25)
        self.confSlider.setOrientation(QtCore.Qt.Horizontal)
        self.confSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.confSlider.setObjectName("confSlider")
        self.horizontalLayout_3.addWidget(self.confSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_8 = QtWidgets.QLabel(self.groupBox_8)
        self.label_8.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_8.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_14.addWidget(self.label_8)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_8)
        self.checkBox.setStyleSheet("\n"
"QCheckBox\n"
"{font-size: 16px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QCheckBox::indicator {\n"
"    image: url(:/icons/icons/button-on.png);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"\n"
"}\n"
"")
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_14.addWidget(self.checkBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.rateSpinBox = QtWidgets.QSpinBox(self.groupBox_8)
        self.rateSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.rateSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.rateSpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.rateSpinBox.setStyleSheet("QSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"\n"
"    image: url(:/icons/icons/箭头_列表展开.png);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"\n"
"QSpinBox::up-button{\n"
"    image: url(:/icons/icons/箭头_列表收起.png);\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"QSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"")
        self.rateSpinBox.setMinimum(1)
        self.rateSpinBox.setMaximum(20)
        self.rateSpinBox.setSingleStep(1)
        self.rateSpinBox.setProperty("value", 1)
        self.rateSpinBox.setObjectName("rateSpinBox")
        self.horizontalLayout_13.addWidget(self.rateSpinBox)
        self.rateSlider = QtWidgets.QSlider(self.groupBox_8)
        self.rateSlider.setStyleSheet("QSlider{\n"
"border-color: #bcbcbc;\n"
"color:#d9d9d9;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"     border: 1px solid #999999;\n"
"     height: 3px;\n"
"    margin: 0px 0;\n"
"     left: 5px; right: 5px;\n"
" }\n"
"QSlider::handle:horizontal {\n"
"     border: 0px ;\n"
"     border-image: url(:/img/icon/圆.png);\n"
"     width:15px;\n"
"     margin: -7px -7px -7px -7px;\n"
"}\n"
"QSlider::add-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9);\n"
"\n"
"}\n"
"QSlider::sub-page:horizontal{\n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);\n"
"}")
        self.rateSlider.setMinimum(1)
        self.rateSlider.setMaximum(20)
        self.rateSlider.setSingleStep(1)
        self.rateSlider.setPageStep(1)
        self.rateSlider.setProperty("value", 1)
        self.rateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rateSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.rateSlider.setObjectName("rateSlider")
        self.horizontalLayout_13.addWidget(self.rateSlider)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 42))
        self.groupBox_6.setStyleSheet("#groupBox_6{\n"
"border: 0px solid #42adff;\n"
"border-radius:0px;}")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_36.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.saveCheckBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.saveCheckBox.setStyleSheet("\n"
"QCheckBox\n"
"{font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QCheckBox::indicator {\n"
"    image: url(:/icons/icons/button-on.png);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"\n"
"}\n"
"")
        self.saveCheckBox.setChecked(True)
        self.saveCheckBox.setObjectName("saveCheckBox")
        self.horizontalLayout_36.addWidget(self.saveCheckBox)
        self.verticalLayout_8.addWidget(self.groupBox_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 42))
        self.groupBox_9.setMaximumSize(QtCore.QSize(16777215, 42))
        self.groupBox_9.setStyleSheet("#groupBox_9{\n"
"border: 0px solid #42adff;\n"
"border-top: 1px solid rgba(200, 200, 200,100);\n"
"border-bottom: 1px solid rgba(200, 200, 200,100);\n"
"border-radius:0px;}")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_38.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.label_11 = QtWidgets.QLabel(self.groupBox_9)
        self.label_11.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 22px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_38.addWidget(self.label_11)
        spacerItem2 = QtWidgets.QSpacerItem(37, 39, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem2)
        self.verticalLayout_7.addWidget(self.groupBox_9)
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_10.setMinimumSize(QtCore.QSize(0, 42))
        self.groupBox_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_10.setStyleSheet("#groupBox_10{\n"
"border: 0px solid #42adff;\n"
"\n"
"border-radius:0px;}")
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        # 先创建resultWidget
        self.resultWidget = QtWidgets.QTableWidget(self.groupBox_10)
        self.resultWidget.setStyleSheet("""
                    QTableWidget {
                        background-color: rgba(45, 45, 45, 200);
                        font-family: "Microsoft YaHei";
                        font-size: 14px;
                        color: white;
                        border: none;
                    }
                    QHeaderView::section {
                        background-color: #404040;
                        padding: 4px;
                    }
                """)
        self.resultWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.resultWidget.verticalHeader().setVisible(False)
        self.resultWidget.setObjectName("resultWidget")  # 设置控件的唯一标识
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_39.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout_39.addWidget(self.resultWidget)  # 此时控件已存在
        self.horizontalLayout_39.setStretch(0, 1)

        self.verticalLayout_7.addWidget(self.groupBox_10)
        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_7.addWidget(self.groupBox_8)
        self.groupBox_201 = QtWidgets.QGroupBox(self.groupBox_18)
        self.groupBox_201.setStyleSheet("#groupBox_201{\n"
"background-color: rgba(95, 95, 95, 200);\n"
"border: 0px solid #42adff;\n"
"border-left: 1px solid rgba(200, 200, 200,100);\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-radius:0px;}")
        self.groupBox_201.setTitle("")
        self.groupBox_201.setObjectName("groupBox_201")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_201)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_201)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 42))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 42))
        self.groupBox_3.setStyleSheet("#groupBox_3{\n"
"border: 0px solid #42adff;\n"
"border-bottom: 1px solid rgba(200, 200, 200,100);\n"
"border-radius:0px;}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_6.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 22px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.fps_label = QtWidgets.QLabel(self.groupBox_3)
        self.fps_label.setMinimumSize(QtCore.QSize(100, 40))
        self.fps_label.setMaximumSize(QtCore.QSize(100, 40))
        self.fps_label.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 20px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.fps_label.setText("")
        self.fps_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fps_label.setObjectName("fps_label")
        self.horizontalLayout_6.addWidget(self.fps_label)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.splitter = QtWidgets.QSplitter(self.groupBox_201)
        self.splitter.setEnabled(True)
        self.splitter.setStyleSheet("#splitter::handle{background: 1px solid  rgba(200, 200, 200,100);}")
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setLineWidth(10)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.splitter.setObjectName("splitter")
        self.raw_video = Label_click_Mouse(self.splitter)
        self.raw_video.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.raw_video.sizePolicy().hasHeightForWidth())
        self.raw_video.setSizePolicy(sizePolicy)
        self.raw_video.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        self.raw_video.setFont(font)
        self.raw_video.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.raw_video.setStyleSheet("color: rgb(218, 218, 218);\n"
"")
        self.raw_video.setText("")
        self.raw_video.setScaledContents(False)
        self.raw_video.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_video.setObjectName("raw_video")
        self.out_video = Label_click_Mouse(self.splitter)
        self.out_video.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_video.sizePolicy().hasHeightForWidth())
        self.out_video.setSizePolicy(sizePolicy)
        self.out_video.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        self.out_video.setFont(font)
        self.out_video.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.out_video.setStyleSheet("color: rgb(218, 218, 218);\n"
"\n"
"\n"
"")
        self.out_video.setText("")
        self.out_video.setScaledContents(False)
        self.out_video.setAlignment(QtCore.Qt.AlignCenter)
        self.out_video.setObjectName("out_video")
        self.verticalLayout_4.addWidget(self.splitter)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(11, -1, 11, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.runButton = QtWidgets.QPushButton(self.groupBox_201)
        self.runButton.setMinimumSize(QtCore.QSize(40, 40))
        self.runButton.setStyleSheet("QPushButton {\n"
"    image: url(:/icons/icons/运行.png);\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.runButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/运行.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/暂停.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/运行.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/暂停.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/运行.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/暂停.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/运行.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/暂停.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.runButton.setIcon(icon7)
        self.runButton.setIconSize(QtCore.QSize(30, 30))
        self.runButton.setCheckable(True)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout_12.addWidget(self.runButton)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_201)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 5))
        self.progressBar.setStyleSheet("QProgressBar{ color: rgb(255, 255, 255); font:12pt; border-radius:2px; text-align:center; border:none; background-color: rgba(215, 215, 215,100);}\n"
"QProgressBar:chunk{ border-radius:0px; background: rgba(55, 55, 55, 200);}")
        self.progressBar.setMaximum(1000)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_12.addWidget(self.progressBar)
        self.stopButton = QtWidgets.QPushButton(self.groupBox_201)
        self.stopButton.setMinimumSize(QtCore.QSize(40, 40))
        self.stopButton.setStyleSheet("QPushButton {\n"
"image: url(:/icons/icons/终止.png);\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.stopButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/icon/终止.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon8)
        self.stopButton.setIconSize(QtCore.QSize(30, 30))
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_12.addWidget(self.stopButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.verticalLayout_4.setStretch(1, 1)
        self.horizontalLayout_7.addWidget(self.groupBox_201)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_18)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.groupBox_4.setStyleSheet("#groupBox_4{\n"
"background-color: rgba(75, 75, 75, 200);\n"
"border: 0px solid #42adff;\n"
"border-left: 0px solid rgba(29, 83, 185, 255);\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-top: 1px solid rgba(200, 200, 200,100);\n"
"border-radius:0px;}")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.statistic_label = QtWidgets.QLabel(self.groupBox_4)
        self.statistic_label.setMouseTracking(False)
        self.statistic_label.setStyleSheet("QLabel\n"
"{\n"
"\n"
"    font-size: 16px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: light;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.statistic_label.setText("")
        self.statistic_label.setObjectName("statistic_label")
        self.horizontalLayout_10.addWidget(self.statistic_label)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.verticalLayout_2.addWidget(self.groupBox_18)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        self.minButton.clicked.connect(mainWindow.showMinimized) # type: ignore
        self.maxButton.clicked.connect(mainWindow.showMaximized) # type: ignore
        self.closeButton.clicked.connect(mainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "基于YOLOv8的水下鱼类计数系统"))
        self.label_4.setText(_translate("mainWindow", "YOLOv8 GUI"))
        self.label_5.setText(_translate("mainWindow", "setting"))
        self.label_3.setText(_translate("mainWindow", "model"))
        self.comboBox.setItemText(0, _translate("mainWindow", "yolov8s.pt"))
        self.comboBox.setItemText(1, _translate("mainWindow", "yolov8m.pt"))
        self.comboBox.setItemText(2, _translate("mainWindow", "yolov8l.pt"))
        self.comboBox.setItemText(3, _translate("mainWindow", "yolov8x.pt"))
        self.label_10.setText(_translate("mainWindow", "input"))
        self.fileButton.setToolTip(_translate("mainWindow", "file"))
        self.cameraButton.setToolTip(_translate("mainWindow", "camera"))
        self.rtspButton.setToolTip(_translate("mainWindow", "rtsp"))
        self.label_2.setText(_translate("mainWindow", "IoU"))
        self.label.setText(_translate("mainWindow", "conf"))
        self.label_8.setText(_translate("mainWindow", "latency"))
        self.checkBox.setText(_translate("mainWindow", "enable"))
        self.saveCheckBox.setText(_translate("mainWindow", "save automatically"))
        self.label_11.setText(_translate("mainWindow", "result statistics"))
        self.label_6.setText(_translate("mainWindow", "view"))

img_src = np.zeros((1280, 720, 3), np.uint8)
COLORS = [
    (0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255),
    (255, 0, 255), (192, 192, 192), (128, 128, 128), (128, 0, 0),
    (128, 128, 0), (0, 128, 0)]
LABELS = ['fish']
img_src = cv2.imread('C:\\Users\\Duuuzx\\fish-couting\\testdata\\CS_videoplayback014.png') #指向OpenCv对象
tclose=False
truning=False
tsleep=False

class MainWindow(QMainWindow, Ui_mainWindow):
        #一个初始化函数
        def __init__(self, parent=None):
                super(MainWindow, self).__init__(parent)
                self.setupUi(self) #用于将 UI 设计文件（.ui）中的控件和布局加载到窗口中。
                self.resultWidget = self.findChild(QtWidgets.QTableWidget, "resultWidget")
                # QMainWindow.__init__(self, parent)
                # Ui_mainWindow.__init__(self)
                # self.setupUi(self)

                self.m_flag = False #定义一个标志变量 m_flag，并初始化为 False。它可能用于后续的某些逻辑控制

                # style 1: window can be stretched（窗口可以拉伸）
                self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
                #Qt.CustomizeWindowHint 和 Qt.WindowStaysOnTopHint 表示该窗口会始终保持在其他窗口之上，并且窗口的外观可以自定义。
                # style 2: window can not be stretched（窗口不能拉伸）
                # self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint
                #                     | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
                # self.setWindowOpacity(0.85)  # Transparency of window

                #三个事件处理函数
                self.minButton.clicked.connect(self.showMinimized)#最小化窗口
                self.maxButton.clicked.connect(self.max_or_restore)#最大化窗口
                self.maxButton.animateClick(10) #设置最大化动画的函数
                self.closeButton.clicked.connect(self.close) #关闭窗口
                #设定一个定时器
                self.qtimer = QTimer(self)
                self.qtimer.setSingleShot(True) #只触发一次
                self.qtimer.timeout.connect(lambda: self.statistic_label.clear())

                # search models automatically
                self.comboBox.clear()
                #加载.pt模型列表
                self.pt_list = os.listdir('./pt')
                self.pt_list = [file for file in self.pt_list if file.endswith('.pt')]
                self.pt_list.sort(key=lambda x: os.path.getsize('./pt/' + x))
                #self.pt_list = os.listdir('/absolute/path/to/pt')  # 使用别的绝对路径来搜索

                #更新模型选择框
                self.comboBox.clear()
                self.comboBox.addItems(self.pt_list)#更新UI上的下拉款comboBox，将模型文件列表.pt添加到下拉框中
                #创建一个定时器qtimer_search，每2秒触发一次 search_pt() 函数，可能用于自动搜索模型或其他资源。
                self.qtimer_search = QTimer(self)
                self.qtimer_search.timeout.connect(lambda: self.memory_check())
                self.qtimer_search.start(2000)

                # yolov8 线程设置
                self.det_thread = DetThread()  #创建一个 DetThread 线程，用于执行 YOLOv8 模型推理任务。
                self.model_type = self.comboBox.currentText()#获取当前选择的模型（model_type），并设置 YOLOv5 使用的模型权重文件路径。
                self.det_thread.weights = "./pt/%s" % self.model_type
                self.det_thread.source = '0'
                #信号与槽连接（用于显示图片与信息等）
                self.det_thread.percent_length = self.progressBar.maximum()
                self.det_thread.send_raw.connect(lambda x: self.show_image(x, self.raw_video))
                self.det_thread.send_img.connect(lambda x: self.show_image(x, self.out_video))
                self.det_thread.send_msg.connect(lambda x: self.show_msg(x))
                self.det_thread.send_percent.connect(lambda x: self.progressBar.setValue(x))
                self.det_thread.send_fps.connect(lambda x: self.fps_label.setText(x))
                #按钮时间连接
                self.fileButton.clicked.connect(self.open_file)#选择文件
                # self.cameraButton.clicked.connect(self.chose_cam)#选择相机 暂时没有self.chose_cam的定义
                #self.rtspButton.clicked.connect(self.chose_rtsp)#选择PTSP流
                #运行与停止按钮
                #self.runButton.clicked.connect(self.run_or_continue)
                # self.stopButton.clicked.connect(self.stop)
                # self.stopButton.clicked.connect(self.stopsc)
                #为复选框（checkBox, saveCheckBox）连接点击事件，可能用于启用/禁用某些设置或保存设置。
                # self.checkBox.clicked.connect(self.checkrate)
                # self.saveCheckBox.clicked.connect(self.is_save)
                #加载之前保存的设置，可能是从文件中读取应用程序的配置或用户的设置。
                self.tclose = False  # 窗口关闭标志
                self.tsleep = False  # 检测暂停标志
                self.truning = False  # 运行状态标志
                self.img_lock = threading.Lock()  # 图像数据锁
                self.img_src = None  # 初始化图像存储
                self.mem_timer = QTimer(self)
                self.mem_timer.timeout.connect(self.memory_check)
                self.mem_timer.start(1000)  # 每秒检查
                # 添加统计信号连接
                self.det_thread.send_statistic.connect(self._update_statistic_ui)
                # 添加模型切换信号连接
                self.comboBox.currentTextChanged.connect(self.change_model)
                # 初始化统计表格
                self.resultWidget.setColumnCount(2)
                self.resultWidget.setHorizontalHeaderLabels(["类别", "数量"])
                self.resultWidget.horizontalHeader().setStretchLastSection(True)
                self.det_thread.error_occurred.connect(self.show_msg)

        # 在MainWindow类中添加以下方法
        def open_file(self):
                """选择图片文件并触发检测"""
                config_file = './pt/best.pt'  # 这里的模型名称更改无用，需要到线程里面进行修改
                if not os.path.exists(config_file):
                        QMessageBox.warning(self, "警告", "未找到模型文件")
                        return

                # 打开文件对话框选择图片或视频
                file, _ = QFileDialog.getOpenFileName(
                        self,
                        "选择文件",
                        "",
                        "媒体文件 (*.jpg *.png *.jpeg *.bmp *.mp4 *.avi *.mov)"
                )

                if file:
                        self.current_source = file
                        self.show_initial_preview(file)

                        # 停止当前线程
                        if self.det_thread.isRunning():
                                self.det_thread.stop()
                                self.det_thread.wait()

                        # 初始化检测线程
                        self.det_thread = DetThread()
                        self.det_thread.source = file
                        self.det_thread.send_raw.connect(lambda x: self.show_image(x, self.raw_video))
                        self.det_thread.send_img.connect(lambda x: self.show_image(x, self.out_video))
                        self.det_thread.send_statistic.connect(self._update_statistic_ui)
                        self.det_thread.send_msg.connect(self.show_msg)

                        # 连接控制按钮
                        self.runButton.clicked.connect(self.toggle_detection)
                        self.stopButton.clicked.connect(self.stop_detection)

                        # 初始化进度条
                        self.progressBar.setValue(0)
                        self.det_thread.start()

        def show_initial_preview(self, file_path):
                """显示文件预览"""
                if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                        pixmap = QPixmap(file_path)
                        self.raw_video.setPixmap(pixmap.scaled(self.raw_video.size(),
                                                               Qt.KeepAspectRatio,
                                                               Qt.SmoothTransformation))
                else:  # 视频文件
                        cap = cv2.VideoCapture(file_path)
                        ret, frame = cap.read()
                        if ret:
                                self.show_image(frame, self.raw_video)
                        cap.release()

        # def show_original_image(self, img_path):
        #         """显示原始图片到左侧窗口"""
        #         pixmap = QPixmap(img_path)
        #         scaled_pixmap = pixmap.scaled(
        #                 self.raw_video.size(),
        #                 Qt.KeepAspectRatio,
        #                 Qt.SmoothTransformation
        #         )
        #         self.raw_video.setPixmap(scaled_pixmap)

        def show_msg(self, msg):
                """在界面底部状态栏显示消息"""
                self.statistic_label.setText(msg)  # 使用已有的统计标签显示消息

        # 修改现有的show_image方法
        def show_image(self, img_src, label):
                try:
                        if img_src is None:
                                return

                        # 获取当前label尺寸
                        label_width = label.width()
                        label_height = label.height()

                        # 计算缩放比例
                        h, w = img_src.shape[:2]
                        scale = min(label_width / w, label_height / h)

                        # 优化大尺寸图像处理
                        if max(w, h) > 1920:  # 对大于1080p的图像进行下采样
                                img_src = cv2.resize(img_src, (int(w * 0.5), int(h * 0.5)))

                        # 转换为RGB
                        img_rgb = cv2.cvtColor(img_src, cv2.COLOR_BGR2RGB)
                        qimg = QImage(img_rgb.data, img_rgb.shape[1], img_rgb.shape[0],
                                      img_rgb.strides[0], QImage.Format_RGB888)
                        pixmap = QPixmap.fromImage(qimg)

                        # 保持比例缩放
                        scaled_pixmap = pixmap.scaled(
                                label.size() * 0.95,  # 保留5%的边距
                                Qt.KeepAspectRatio,
                                Qt.SmoothTransformation
                        )
                        label.setPixmap(scaled_pixmap)

                except Exception as e:
                        print(f"显示错误: {str(e)}")

                 # 根据某个按钮的状态来决定窗口的显示方式
        def max_or_restore(self):
                if self.maxButton.isChecked():  # 检查maxButton是否被选中
                        self.showMaximized()  # 最大化
                else:
                        self.showNormal()
                # 根据按钮状态来控制某些操作的执行

        def closeEvent(self, event):
                # 先停止检测线程
                self.det_thread.jump_out = True
                self.det_thread.quit()

                # 等待线程结束
                if not self.det_thread.wait(3000):  # 3秒超时
                        self.det_thread.terminate()

                # 释放资源
                if hasattr(self, 'mem_timer'):
                        self.mem_timer.stop()

                super().closeEvent(event)

        def memory_check(self):
                """内存使用监控"""
                process = psutil.Process(os.getpid())
                mem = process.memory_info().rss / 1024 / 1024  # MB
                if mem > 2048:  # 2GB阈值
                        self.show_msg(f"内存使用过高: {mem:.1f}MB，正在释放资源...")
                        if self.det_thread.isRunning():
                                self.det_thread.stop()
                        torch.cuda.empty_cache()
                        QMessageBox.warning(self, "内存警告", "已释放资源，请重新启动检测")

                # 新增统计信息更新方法

        def _update_statistic_ui(self, class_count):
                try:
                        self.resultWidget.setRowCount(0)
                        if class_count:
                                for row, (name, count) in enumerate(class_count.items()):
                                        self.resultWidget.insertRow(row)
                                        self.resultWidget.setItem(row, 0, QTableWidgetItem(str(name)))
                                        self.resultWidget.setItem(row, 1, QTableWidgetItem(str(count)))
                        else:
                                self.resultWidget.insertRow(0)
                                self.resultWidget.setItem(0, 0, QTableWidgetItem("无检测结果"))
                except Exception as e:
                        print(f"更新表格错误: {e}")

        def change_model(self):
                """切换模型处理"""
                try:
                        # 停止当前检测线程
                        if self.det_thread.isRunning():
                                self.det_thread.stop()
                                self.det_thread.wait()  # 等待线程结束

                        # 设置新模型路径
                        self.model_type = self.comboBox.currentText()
                        model_path = os.path.join("./pt", self.model_type)
                        if not os.path.exists(model_path):
                                raise FileNotFoundError(f"模型文件 {model_path} 不存在")

                        # 加载新模型
                        self.det_thread.set_weights(model_path)
                        self.show_msg(f"模型已切换为: {self.model_type}")

                except Exception as e:
                        self.show_msg(f"模型切换失败: {str(e)}")

        def toggle_detection(self):
                """切换检测状态（播放/暂停）"""
                if self.det_thread.isRunning():
                        if self.det_thread.is_paused:
                                self.det_thread.resume()
                                self.runButton.setChecked(True)
                                self.runButton.setToolTip("暂停检测")
                        else:
                                self.det_thread.pause()
                                self.runButton.setChecked(False)
                                self.runButton.setToolTip("继续检测")

        def stop_detection(self):
                """停止检测"""
                if self.det_thread.isRunning():
                        self.det_thread.stop()
                        self.runButton.setChecked(False)
                        self.progressBar.setValue(0)
                        self.statistic_label.setText("检测已停止")

class DetThread(QThread):
        # 定义信号
        send_img = pyqtSignal(np.ndarray)
        send_raw = pyqtSignal(np.ndarray)
        send_statistic = pyqtSignal(dict)
        send_msg = pyqtSignal(str)
        send_percent = pyqtSignal(int)
        send_fps = pyqtSignal(str)
        error_occurred = pyqtSignal(str)  # 新增错误信号

        def __init__(self):
                super().__init__()
                # 初始化参数
                self.weights = './pt/best.pt'  # 默认模型路径
                self.source = ''  # 输入源（图片路径）
                self.conf = 0.25  # 置信度阈值
                self.iou = 0.45  # IOU阈值
                self.is_continue = True  # 继续检测标志
                self.jump_out = False  # 跳出循环标志
                self.save_fold = './result'  # 结果保存路径
                self.model = None  # YOLO模型实例
                self.vid_writer = None
                self.cap = None
                self.frame_count = 0
                self.total_frames = 0
                self.is_paused = False
                self.lock = threading.Lock()

        def run(self):
                try:
                        self.model = YOLO(self.weights, task='detect')
                        self.model.to('cpu')
                        self.model.conf = self.conf
                        self.model.iou = self.iou

                        # 判断输入类型
                        if self.source.lower().endswith(('.mp4', '.avi', '.mov')):
                                self.process_video()
                        else:
                                self.process_image()

                except Exception as e:
                        self.send_msg.emit(f"检测错误: {str(e)}")
                        self.error_occurred.emit(str(e))
                finally:
                        if self.cap:
                                self.cap.release()
                        if self.vid_writer:
                                self.vid_writer.release()
                        self.model = None
                        torch.cuda.empty_cache()

        def process_video(self):
                """处理视频流"""
                self.cap = cv2.VideoCapture(self.source)
                if not self.cap.isOpened():
                        raise ValueError("无法打开视频文件")

                # 获取视频信息
                self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
                fps = self.cap.get(cv2.CAP_PROP_FPS)
                frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

                # 初始化视频保存
                if self.save_fold and not os.path.exists(self.save_fold):
                        os.makedirs(self.save_fold)
                save_path = os.path.join(self.save_fold,
                                         os.path.basename(self.source))
                self.vid_writer = cv2.VideoWriter(save_path,
                                                  cv2.VideoWriter_fourcc(*'mp4v'),
                                                  fps,
                                                  (frame_width, frame_height))

                while not self.jump_out and self.cap.isOpened():
                        with self.lock:
                                if self.is_paused:
                                        time.sleep(0.1)
                                        continue

                        ret, frame = self.cap.read()
                        if not ret:
                                break

                        # 处理帧
                        self.frame_count += 1
                        self.send_percent.emit(int(self.frame_count / self.total_frames * 1000))

                        # 发送原始帧
                        self.send_raw.emit(frame)

                        # 执行检测
                        results = self.model(frame, verbose=False)

                        # 绘制结果
                        annotated_frame = self.annotate_frame(frame, results[0])

                        # 发送检测结果
                        self.send_img.emit(annotated_frame)

                        # 保存结果
                        if self.vid_writer:
                                self.vid_writer.write(annotated_frame)

                        # 更新统计
                        class_count = self.get_statistics(results[0])
                        self.send_statistic.emit(class_count)

                        # 保持播放速度
                        time.sleep(0.03)  # ~30fps

        def process_image(self):
                """处理单张图片"""
                img = cv2.imread(self.source)
                if img is None:
                        raise ValueError("无法读取图片文件")

                # 发送原始图像
                self.send_raw.emit(img)

                # 执行检测
                results = self.model(img, verbose=False)

                # 绘制结果
                annotated_img = self.annotate_frame(img, results[0])

                # 发送检测结果
                self.send_img.emit(annotated_img)

                # 保存结果
                if self.save_fold:
                        if not os.path.exists(self.save_fold):
                                os.makedirs(self.save_fold)
                        save_path = os.path.join(self.save_fold,
                                                 os.path.basename(self.source))
                        cv2.imwrite(save_path, annotated_img)

                # 更新统计
                class_count = self.get_statistics(results[0])
                self.send_statistic.emit(class_count)

        def annotate_frame(self, frame, result):
                """绘制检测结果"""
                annotated = frame.copy()
                class_count = defaultdict(int)

                for box in result.boxes:
                        # 绘制边界框
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)

                        # 绘制标签
                        class_id = int(box.cls)
                        class_name = self.model.names[class_id]
                        conf = float(box.conf)
                        label = f"{class_name} {conf:.2f}"
                        cv2.putText(annotated, label, (x1, y1 - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                        class_count[class_name] += 1

                return annotated

        def get_statistics(self, result):
                """获取统计信息"""
                class_count = defaultdict(int)
                for box in result.boxes:
                        class_id = int(box.cls)
                        class_name = self.model.names[class_id]
                        class_count[class_name] += 1
                return dict(class_count)

        def pause(self):
                with self.lock:
                        self.is_paused = True

        def resume(self):
                with self.lock:
                        self.is_paused = False

        def stop(self):
                self.jump_out = True
                self.quit()
                self.wait()

        def set_weights(self, weights_path):
                """更换模型"""
                try:
                        # 释放旧模型资源
                        if self.model:
                                del self.model
                                torch.cuda.empty_cache()

                        # 加载新模型
                        self.weights = weights_path
                        self.model = YOLO(self.weights, task='detect')
                        self.model.to('cpu')  # 确保使用CPU
                except Exception as e:
                        self.error_occurred.emit(f'加载模型失败: {str(e)}')

        def update_args(self, kwargs):
                """动态更新参数"""
                for key, value in kwargs.items():
                        if hasattr(self, key):
                                setattr(self, key, value)



