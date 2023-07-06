# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cameraPropSetup.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CameraPropDlg(object):
    def setupUi(self, CameraPropDlg):
        CameraPropDlg.setObjectName("CameraPropDlg")
        CameraPropDlg.resize(557, 448)
        CameraPropDlg.setStyleSheet("color: rgb(223, 223, 223);\n"
"font: 75 20pt \"微软雅黑\";\n"
"background-color: rgb(30, 97, 138);")
        self.buttonBox = QtWidgets.QDialogButtonBox(CameraPropDlg)
        self.buttonBox.setGeometry(QtCore.QRect(260, 390, 175, 43))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.NoButton)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(CameraPropDlg)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 100, 411, 245))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSpacing(24)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.SliderContrast = QtWidgets.QSlider(self.formLayoutWidget)
        self.SliderContrast.setStyleSheet(" margin-top:14px;\n"
" ")
        self.SliderContrast.setSliderPosition(0)
        self.SliderContrast.setOrientation(QtCore.Qt.Horizontal)
        self.SliderContrast.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.SliderContrast.setTickInterval(10)
        self.SliderContrast.setObjectName("SliderContrast")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.SliderContrast)
        self.SliderZoom = QtWidgets.QSlider(self.formLayoutWidget)
        self.SliderZoom.setStyleSheet("  margin-top:14px;")
        self.SliderZoom.setMaximum(70)
        self.SliderZoom.setOrientation(QtCore.Qt.Horizontal)
        self.SliderZoom.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.SliderZoom.setTickInterval(10)
        self.SliderZoom.setObjectName("SliderZoom")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.SliderZoom)
        self.SliderBrightness = QtWidgets.QSlider(self.formLayoutWidget)
        self.SliderBrightness.setStyleSheet(" margin-top:14px;")
        self.SliderBrightness.setMinimum(-60)
        self.SliderBrightness.setMaximum(60)
        self.SliderBrightness.setOrientation(QtCore.Qt.Horizontal)
        self.SliderBrightness.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.SliderBrightness.setTickInterval(10)
        self.SliderBrightness.setObjectName("SliderBrightness")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.SliderBrightness)
        self.label_4 = QtWidgets.QLabel(CameraPropDlg)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 331, 51))
        self.label_4.setStyleSheet("font: 75 22pt \"微软雅黑\";\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.btnDefault = QtWidgets.QPushButton(CameraPropDlg)
        self.btnDefault.setGeometry(QtCore.QRect(160, 390, 101, 41))
        self.btnDefault.setObjectName("btnDefault")

        self.retranslateUi(CameraPropDlg)
        self.buttonBox.accepted.connect(CameraPropDlg.accept)
        self.buttonBox.rejected.connect(CameraPropDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(CameraPropDlg)

    def retranslateUi(self, CameraPropDlg):
        _translate = QtCore.QCoreApplication.translate
        CameraPropDlg.setWindowTitle(_translate("CameraPropDlg", "Dialog"))
        self.label_2.setText(_translate("CameraPropDlg", "变焦："))
        self.label.setText(_translate("CameraPropDlg", "亮度："))
        self.label_3.setText(_translate("CameraPropDlg", "对比度："))
        self.label_4.setText(_translate("CameraPropDlg", "摄像头调节："))
        self.btnDefault.setText(_translate("CameraPropDlg", "默认值"))

