# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zoomImgWin.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_zoomImgWin(object):
    def setupUi(self, zoomImgWin):
        zoomImgWin.setObjectName("zoomImgWin")
        zoomImgWin.resize(500, 425)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(zoomImgWin)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbZoomImg = QtWidgets.QLabel(zoomImgWin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbZoomImg.sizePolicy().hasHeightForWidth())
        self.lbZoomImg.setSizePolicy(sizePolicy)
        self.lbZoomImg.setStyleSheet("")
        self.lbZoomImg.setAlignment(QtCore.Qt.AlignCenter)
        self.lbZoomImg.setObjectName("lbZoomImg")
        self.verticalLayout.addWidget(self.lbZoomImg)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(zoomImgWin)
        QtCore.QMetaObject.connectSlotsByName(zoomImgWin)

    def retranslateUi(self, zoomImgWin):
        _translate = QtCore.QCoreApplication.translate
        zoomImgWin.setWindowTitle(_translate("zoomImgWin", "Form"))
        self.lbZoomImg.setText(_translate("zoomImgWin", "TextLabel"))


