# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1283, 768)
        Form.setStyleSheet("background-color: rgb(26, 29, 60);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"黑体\"")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(300, 70))
        self.label_4.setStyleSheet("image: url(:/img/icon/logo.png);\n"
"background-color: qlineargradient(spread:pad, x1:0.0113636, y1:0.011, x2:1, y2:0, stop:0 rgba(26, 29, 60, 255), stop:0.568182 rgba(57, 94, 150, 255), stop:0.75 rgba(57, 94, 150, 255), stop:1 rgba(26, 29, 60, 255));\n"
"\n"
"border-radius:5px;\n"
" \n"
" ")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setStyleSheet("font: 75 40pt \"黑体\";\n"
"color: rgb(4, 170, 255);\n"
"\n"
" ")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.btnCameraProp = QtWidgets.QPushButton(Form)
        self.btnCameraProp.setMinimumSize(QtCore.QSize(16, 16))
        self.btnCameraProp.setMaximumSize(QtCore.QSize(64, 64))
        self.btnCameraProp.setStyleSheet("image: url(:/icon/icon/camera.ico);\n"
"border-radius:7px;")
        self.btnCameraProp.setText("")
        self.btnCameraProp.setObjectName("btnCameraProp")
        self.horizontalLayout_2.addWidget(self.btnCameraProp)
        self.btnSetup = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSetup.sizePolicy().hasHeightForWidth())
        self.btnSetup.setSizePolicy(sizePolicy)
        self.btnSetup.setMinimumSize(QtCore.QSize(16, 16))
        self.btnSetup.setMaximumSize(QtCore.QSize(64, 64))
        self.btnSetup.setBaseSize(QtCore.QSize(32, 32))
        self.btnSetup.setStyleSheet("image: url(:/icon/icon/setup.ico);\n"
"border-radius:7px;")
        self.btnSetup.setText("")
        self.btnSetup.setObjectName("btnSetup")
        self.horizontalLayout_2.addWidget(self.btnSetup)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 12)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setStyleSheet("font: 75 14pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.lbMachineLeader = QtWidgets.QLabel(self.groupBox)
        self.lbMachineLeader.setStyleSheet("background-color: rgb(48, 48, 85);\n"
"border-radius:7px;\n"
"border:1px solid green;\n"
"color: rgb(0, 255, 255);\n"
"font: 36pt \"幼圆\";")
        self.lbMachineLeader.setAlignment(QtCore.Qt.AlignCenter)
        self.lbMachineLeader.setObjectName("lbMachineLeader")
        self.gridLayout_4.addWidget(self.lbMachineLeader, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setStyleSheet(" \n"
"\n"
"font: 75 14pt \"微软雅黑\";\n"
" ")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 3, 1, 1, 1)
        self.lbWorkSeq = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbWorkSeq.sizePolicy().hasHeightForWidth())
        self.lbWorkSeq.setSizePolicy(sizePolicy)
        self.lbWorkSeq.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbWorkSeq.setStyleSheet("background-color: rgb(48, 48, 85);\n"
"font: 36pt \"幼圆\";\n"
"color: rgb(0, 255, 255);\n"
" \n"
"border-radius:7px;\n"
"border:1px solid green;")
        self.lbWorkSeq.setAlignment(QtCore.Qt.AlignCenter)
        self.lbWorkSeq.setObjectName("lbWorkSeq")
        self.gridLayout_4.addWidget(self.lbWorkSeq, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 2, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 2)
        self.gridLayout_4.setColumnStretch(1, 7)
        self.gridLayout_4.setColumnStretch(2, 1)
        self.gridLayout_4.setRowStretch(0, 2)
        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_4.setRowStretch(2, 2)
        self.gridLayout_4.setRowStretch(3, 1)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setHorizontalSpacing(1)
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setStyleSheet(" border-top:1px solid rgb(122,122,122);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setStyleSheet("border-bottom:1px solid white;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 2, 1, 1)
        self.comYear = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comYear.sizePolicy().hasHeightForWidth())
        self.comYear.setSizePolicy(sizePolicy)
        self.comYear.setMinimumSize(QtCore.QSize(4, 4))
        self.comYear.setStyleSheet("color: rgb(0, 255, 255);\n"
"font: 50pt \"黑体\";\n"
" \n"
" \n"
"\n"
"")
        self.comYear.setMaxCount(5)
        self.comYear.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comYear.setObjectName("comYear")
        self.comYear.addItem("")
        self.comYear.addItem("")
        self.comYear.addItem("")
        self.gridLayout_2.addWidget(self.comYear, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet(" \n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setStyleSheet("border-bottom:1px solid white;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.editProductType = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editProductType.sizePolicy().hasHeightForWidth())
        self.editProductType.setSizePolicy(sizePolicy)
        self.editProductType.setMinimumSize(QtCore.QSize(2, 0))
        self.editProductType.setStyleSheet("color: rgb(0, 255, 255);\n"
"font: 50pt \"黑体\";\n"
"border:0px solid rgb(100,100,100);\n"
"")
        self.editProductType.setMaxLength(1)
        self.editProductType.setAlignment(QtCore.Qt.AlignCenter)
        self.editProductType.setObjectName("editProductType")
        self.gridLayout_2.addWidget(self.editProductType, 1, 1, 1, 1)
        self.txtDescribe = QtWidgets.QTextEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.txtDescribe.sizePolicy().hasHeightForWidth())
        self.txtDescribe.setSizePolicy(sizePolicy)
        self.txtDescribe.setObjectName("txtDescribe")
        self.gridLayout_2.addWidget(self.txtDescribe, 4, 1, 1, 3)
        self.editK = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.editK.sizePolicy().hasHeightForWidth())
        self.editK.setSizePolicy(sizePolicy)
        self.editK.setMouseTracking(False)
        self.editK.setStyleSheet("background-color: rgb(240, 240, 240);\n"
" \n"
"color: rgb(81, 81, 81);\n"
"font: 40pt \"黑体\";\n"
"border-top:1px solid white;")
        self.editK.setMaxLength(2)
        self.editK.setAlignment(QtCore.Qt.AlignCenter)
        self.editK.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.editK.setObjectName("editK")
        self.gridLayout_2.addWidget(self.editK, 3, 1, 1, 2)
        self.editProductID = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.editProductID.sizePolicy().hasHeightForWidth())
        self.editProductID.setSizePolicy(sizePolicy)
        self.editProductID.setStyleSheet("\n"
" \n"
"color: rgb(0, 255, 255);\n"
"font: 50pt \"黑体\";\n"
"border:0px solid rgb(100,100,100);\n"
"")
        self.editProductID.setMaxLength(4)
        self.editProductID.setPlaceholderText("")
        self.editProductID.setObjectName("editProductID")
        self.gridLayout_2.addWidget(self.editProductID, 1, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setStyleSheet("border-bottom:1px solid white;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1)
        self.editFlag = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editFlag.sizePolicy().hasHeightForWidth())
        self.editFlag.setSizePolicy(sizePolicy)
        self.editFlag.setMinimumSize(QtCore.QSize(2, 0))
        self.editFlag.setStyleSheet("color: rgb(0, 255, 255);\n"
"font: 50pt \"黑体\";\n"
"border:0px solid rgb(100,100,100);\n"
"")
        self.editFlag.setMaxLength(1)
        self.editFlag.setAlignment(QtCore.Qt.AlignCenter)
        self.editFlag.setObjectName("editFlag")
        self.gridLayout_2.addWidget(self.editFlag, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setStyleSheet("border-bottom:1px solid white;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setMinimumSize(QtCore.QSize(0, 1))
        self.line.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 4)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 3, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 4)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(2, 3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbCamera = QtWidgets.QLabel(Form)
        self.lbCamera.setStyleSheet("border:4px solid green;\n"
"background-color: rgb(0, 0, 0);")
        self.lbCamera.setAlignment(QtCore.Qt.AlignCenter)
        self.lbCamera.setObjectName("lbCamera")
        self.verticalLayout_4.addWidget(self.lbCamera)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnDetcCart = QtWidgets.QPushButton(Form)
        self.btnDetcCart.setStyleSheet(":hover\n"
"{\n"
" \n"
" color: rgb(53, 161, 0);\n"
" border: 1px solid rgb(15 , 150 , 255);\n"
"}\n"
":pressed\n"
"{\n"
" color:rgb(75, 75, 75);\n"
" background-color:rgb(204 , 228 , 247);\n"
"  \n"
" padding-left:3px;\n"
" padding-top:3px;\n"
"}\n"
"QPushButton{background-color: qlineargradient(spread:pad, x1:0.488636, y1:0.898, x2:0.500318, y2:0.302, stop:0 rgba(181, 181, 181, 255), stop:0.948864 rgba(243, 243, 243, 255));\n"
"color: rgb(75, 75, 75);}")
        self.btnDetcCart.setObjectName("btnDetcCart")
        self.gridLayout_3.addWidget(self.btnDetcCart, 1, 0, 1, 1)
        self.btnUploadRIO = QtWidgets.QPushButton(Form)
        self.btnUploadRIO.setStyleSheet("QPushButton{background-color: rgb(0, 255, 0);\n"
"border-radius:7px;\n"
"height:35px;\n"
"}\n"
"\n"
":pressed\n"
"{ \n"
" padding-left:3px;\n"
" padding-top:3px;\n"
"}\n"
":hover\n"
"{\n"
" color:rgb(75, 75, 75);\n"
"}")
        self.btnUploadRIO.setObjectName("btnUploadRIO")
        self.gridLayout_3.addWidget(self.btnUploadRIO, 1, 5, 1, 1)
        self.lsImgROIWidget = QtWidgets.QListWidget(Form)
        self.lsImgROIWidget.setObjectName("lsImgROIWidget")
        self.gridLayout_3.addWidget(self.lsImgROIWidget, 0, 1, 1, 7)
        self.lbNumberpPic = QtWidgets.QLabel(Form)
        self.lbNumberpPic.setStyleSheet("border:1px solid blue;\n"
"background-color: rgb(148, 148, 148);")
        self.lbNumberpPic.setTextFormat(QtCore.Qt.AutoText)
        self.lbNumberpPic.setAlignment(QtCore.Qt.AlignCenter)
        self.lbNumberpPic.setObjectName("lbNumberpPic")
        self.gridLayout_3.addWidget(self.lbNumberpPic, 0, 0, 1, 1)
        self.btnCounterRot = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCounterRot.sizePolicy().hasHeightForWidth())
        self.btnCounterRot.setSizePolicy(sizePolicy)
        self.btnCounterRot.setMinimumSize(QtCore.QSize(16, 16))
        self.btnCounterRot.setMaximumSize(QtCore.QSize(72, 72))
        self.btnCounterRot.setStyleSheet("")
        self.btnCounterRot.setText("")
        self.btnCounterRot.setObjectName("btnCounterRot")
        self.gridLayout_3.addWidget(self.btnCounterRot, 1, 2, 1, 1)
        self.btnUpLocal = QtWidgets.QPushButton(Form)
        self.btnUpLocal.setStyleSheet("QPushButton{background-color: rgb(0, 255, 0);\n"
"border-radius:7px;\n"
"\n"
"}\n"
":pressed\n"
"{ \n"
" padding-left:3px;\n"
" padding-top:3px;\n"
"}\n"
":hover\n"
"{\n"
" color:rgb(75, 75, 75);\n"
"}")
        self.btnUpLocal.setObjectName("btnUpLocal")
        self.gridLayout_3.addWidget(self.btnUpLocal, 1, 6, 1, 1)
        self.btnViewROITable = QtWidgets.QPushButton(Form)
        self.btnViewROITable.setStyleSheet("QPushButton{background-color: rgb(0, 255, 0);\n"
"border-radius:7px;\n"
"height:35px;\n"
"}\n"
":pressed\n"
"{ \n"
" padding-left:3px;\n"
" padding-top:3px;\n"
"}\n"
":hover\n"
"{\n"
" color:rgb(75, 75, 75);}\n"
"\n"
"\n"
"")
        self.btnViewROITable.setObjectName("btnViewROITable")
        self.gridLayout_3.addWidget(self.btnViewROITable, 1, 1, 1, 1)
        self.btnRot = QtWidgets.QPushButton(Form)
        self.btnRot.setMinimumSize(QtCore.QSize(16, 16))
        self.btnRot.setMaximumSize(QtCore.QSize(72, 72))
        self.btnRot.setText("")
        self.btnRot.setObjectName("btnRot")
        self.gridLayout_3.addWidget(self.btnRot, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 4, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 5)
        self.gridLayout_3.setColumnStretch(1, 3)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.gridLayout_3.setColumnStretch(3, 1)
        self.gridLayout_3.setColumnStretch(4, 1)
        self.gridLayout_3.setColumnStretch(5, 3)
        self.gridLayout_3.setColumnStretch(6, 3)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.verticalLayout_4.setStretch(0, 5)
        self.verticalLayout_4.setStretch(1, 2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)
        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.comYear.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "可视化废票信息传递系统"))
        self.groupBox.setTitle(_translate("Form", "工序信息"))
        self.label_3.setText(_translate("Form", "机长"))
        self.lbMachineLeader.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "工序"))
        self.lbWorkSeq.setText(_translate("Form", "凹印"))
        self.groupBox_2.setTitle(_translate("Form", "产品废票信息"))
        self.label.setText(_translate("Form", "说明"))
        self.label_11.setText(_translate("Form", "标记"))
        self.comYear.setCurrentText(_translate("Form", "23"))
        self.comYear.setItemText(0, _translate("Form", "22"))
        self.comYear.setItemText(1, _translate("Form", "23"))
        self.comYear.setItemText(2, _translate("Form", "24"))
        self.label_7.setText(_translate("Form", "开位"))
        self.label_5.setText(_translate("Form", "产品年份"))
        self.txtDescribe.setPlaceholderText(_translate("Form", "请输入说明"))
        self.editK.setPlaceholderText(_translate("Form", "?k"))
        self.label_10.setText(_translate("Form", "品种"))
        self.label_9.setText(_translate("Form", "车号"))
        self.label_8.setText(_translate("Form", "  <--请录入开位"))
        self.lbCamera.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; color:#19c80c;\">未发现摄像头。。。</span></p></body></html>"))
        self.btnDetcCart.setText(_translate("Form", "识别车号"))
        self.btnUploadRIO.setText(_translate("Form", "上传废票截图"))
        self.lbNumberpPic.setText(_translate("Form", "车号"))
        self.btnUpLocal.setText(_translate("Form", "上传本地图片"))
        self.btnViewROITable.setText(_translate("Form", "ROI图查看"))

import pic_rc
