# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pramaSetup.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_winParamSetup(object):
    def setupUi(self, winParamSetup):
        winParamSetup.setObjectName("winParamSetup")
        winParamSetup.resize(971, 601)
        winParamSetup.setStyleSheet("QWidget{\n"
"background-color: rgb(48, 48, 85);\n"
"color: rgb(0, 255, 255);}\n"
" \n"
"QLineEdit\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"微软雅黑\";\n"
"background-color: rgb(48, 48, 85);\n"
"border:1px solid rgb(255,255,255);\n"
"border-radius:5px;\n"
"text-align:center;\n"
" \n"
"}\n"
"\n"
" \n"
"")
        self.horizontalLayoutWidget = QtWidgets.QWidget(winParamSetup)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 30, 491, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("font: 20pt \"黑体\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.groupBox_2 = QtWidgets.QGroupBox(winParamSetup)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 220, 381, 221))
        self.groupBox_2.setStyleSheet("font:18pt \"黑体\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 41, 301, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lnCamraWidth = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnCamraWidth.sizePolicy().hasHeightForWidth())
        self.lnCamraWidth.setSizePolicy(sizePolicy)
        self.lnCamraWidth.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lnCamraWidth.setObjectName("lnCamraWidth")
        self.gridLayout_2.addWidget(self.lnCamraWidth, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.lnCamraHeight = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnCamraHeight.sizePolicy().hasHeightForWidth())
        self.lnCamraHeight.setSizePolicy(sizePolicy)
        self.lnCamraHeight.setObjectName("lnCamraHeight")
        self.gridLayout_2.addWidget(self.lnCamraHeight, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setRowStretch(0, 4)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 4)
        self.line = QtWidgets.QFrame(winParamSetup)
        self.line.setGeometry(QtCore.QRect(20, 99, 911, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-top:1px solid white;\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget1 = QtWidgets.QWidget(winParamSetup)
        self.layoutWidget1.setGeometry(QtCore.QRect(290, 490, 321, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnSave = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnSave.setStyleSheet("QPushButton {font: 75 20pt \"微软雅黑\";\n"
"    color: rgb(255, 255, 255);}\n"
"\n"
"\n"
"")
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout_2.addWidget(self.btnSave)
        self.btnDefault = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnDefault.setStyleSheet("QPushButton {font: 75 20pt \"微软雅黑\";\n"
"    color: rgb(255, 255, 255);}\n"
"")
        self.btnDefault.setObjectName("btnDefault")
        self.horizontalLayout_2.addWidget(self.btnDefault)
        self.groupBox = QtWidgets.QGroupBox(winParamSetup)
        self.groupBox.setGeometry(QtCore.QRect(70, 220, 351, 221))
        self.groupBox.setStyleSheet("font: 18pt \"黑体\";\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(15, 47, 261, 131))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lnOcuppyMin = QtWidgets.QLineEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnOcuppyMin.sizePolicy().hasHeightForWidth())
        self.lnOcuppyMin.setSizePolicy(sizePolicy)
        self.lnOcuppyMin.setStyleSheet("background-color: rgba(48, 48, 85,255);\n"
"text-aling:center;")
        self.lnOcuppyMin.setObjectName("lnOcuppyMin")
        self.gridLayout.addWidget(self.lnOcuppyMin, 0, 1, 1, 1)
        self.lnOcuppyMax = QtWidgets.QLineEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnOcuppyMax.sizePolicy().hasHeightForWidth())
        self.lnOcuppyMax.setSizePolicy(sizePolicy)
        self.lnOcuppyMax.setStyleSheet("background-color: rgba(48, 48, 85);")
        self.lnOcuppyMax.setObjectName("lnOcuppyMax")
        self.gridLayout.addWidget(self.lnOcuppyMax, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.gridLayout.setRowStretch(0, 4)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 4)
        self.layoutWidget3 = QtWidgets.QWidget(winParamSetup)
        self.layoutWidget3.setGeometry(QtCore.QRect(500, 140, 391, 40))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_2.setStyleSheet("font: 16pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lnKernelWidth = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lnKernelWidth.setObjectName("lnKernelWidth")
        self.horizontalLayout_3.addWidget(self.lnKernelWidth)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_8.setStyleSheet("font: 16pt \"黑体\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.lnKernelHeight = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lnKernelHeight.setObjectName("lnKernelHeight")
        self.horizontalLayout_3.addWidget(self.lnKernelHeight)
        self.layoutWidget4 = QtWidgets.QWidget(winParamSetup)
        self.layoutWidget4.setGeometry(QtCore.QRect(50, 140, 401, 40))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_3.setStyleSheet("font: 16pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lnOcrServIP = QtWidgets.QLineEdit(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnOcrServIP.sizePolicy().hasHeightForWidth())
        self.lnOcrServIP.setSizePolicy(sizePolicy)
        self.lnOcrServIP.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lnOcrServIP.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lnOcrServIP.setObjectName("lnOcrServIP")
        self.horizontalLayout_4.addWidget(self.lnOcrServIP)

        self.retranslateUi(winParamSetup)
        QtCore.QMetaObject.connectSlotsByName(winParamSetup)

    def retranslateUi(self, winParamSetup):
        _translate = QtCore.QCoreApplication.translate
        winParamSetup.setWindowTitle(_translate("winParamSetup", "系统参数设置"))
        self.label.setText(_translate("winParamSetup", "系统参数设置:"))
        self.groupBox_2.setTitle(_translate("winParamSetup", "视频分辨率(px)："))
        self.label_7.setText(_translate("winParamSetup", "高："))
        self.label_6.setText(_translate("winParamSetup", "宽："))
        self.btnSave.setText(_translate("winParamSetup", "保存"))
        self.btnDefault.setText(_translate("winParamSetup", "重置默认值"))
        self.groupBox.setTitle(_translate("winParamSetup", "车号区域大小："))
        self.label_5.setText(_translate("winParamSetup", "最大："))
        self.label_4.setText(_translate("winParamSetup", "最小："))
        self.label_2.setText(_translate("winParamSetup", "卷积kernel大小："))
        self.label_8.setText(_translate("winParamSetup", "X"))
        self.label_3.setText(_translate("winParamSetup", "OCR Server IP:"))
        self.lnOcrServIP.setInputMask(_translate("winParamSetup", "000.000.000.000"))

