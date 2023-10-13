# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateWindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_updateDlg(object):
    def setupUi(self, updateDlg):
        updateDlg.setObjectName("updateDlg")
        updateDlg.resize(777, 203)
        self.label = QtWidgets.QLabel(updateDlg)
        self.label.setGeometry(QtCore.QRect(50, 20, 171, 31))
        self.label.setStyleSheet("font: 20pt \"Algerian\";")
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(updateDlg)
        self.progressBar.setGeometry(QtCore.QRect(310, 80, 421, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(updateDlg)
        self.label_2.setGeometry(QtCore.QRect(190, 80, 101, 31))
        self.label_2.setStyleSheet("font: 16pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.lbFileName = QtWidgets.QLabel(updateDlg)
        self.lbFileName.setGeometry(QtCore.QRect(20, 80, 161, 31))
        self.lbFileName.setStyleSheet("font: 16pt \"Arial\";\n"
"")
        self.lbFileName.setText("")
        self.lbFileName.setAlignment(QtCore.Qt.AlignCenter)
        self.lbFileName.setObjectName("lbFileName")

        self.retranslateUi(updateDlg)
        QtCore.QMetaObject.connectSlotsByName(updateDlg)

    def retranslateUi(self, updateDlg):
        _translate = QtCore.QCoreApplication.translate
        updateDlg.setWindowTitle(_translate("updateDlg", "Form"))
        self.label.setText(_translate("updateDlg", "系统升级中："))
        self.label_2.setText(_translate("updateDlg", "下载进度："))

