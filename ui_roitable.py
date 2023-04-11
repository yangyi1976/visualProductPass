# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'roitable.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ROITableWindow(object):
    def setupUi(self, ROITableWindow):
        ROITableWindow.setObjectName("ROITableWindow")
        ROITableWindow.resize(992, 673)
        ROITableWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.068, y1:0.125, x2:0.767, y2:0.800909, stop:0 rgba(2, 37, 56, 255), stop:0.619318 rgba(19, 65, 115, 255), stop:0.823864 rgba(40, 90, 145, 255));\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(ROITableWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ROITableWindow)
        self.label.setStyleSheet("font: 75 40pt \"微软雅黑\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"\n"
"color: rgb(0, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label1 = QtWidgets.QLabel(ROITableWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy)
        self.label1.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"font: 75 30pt \"微软雅黑\";")
        self.label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label1.setObjectName("label1")
        self.horizontalLayout.addWidget(self.label1)
        self.lbCartNum = QtWidgets.QLabel(ROITableWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbCartNum.sizePolicy().hasHeightForWidth())
        self.lbCartNum.setSizePolicy(sizePolicy)
        self.lbCartNum.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"font: 75 30pt \"微软雅黑\";")
        self.lbCartNum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbCartNum.setObjectName("lbCartNum")
        self.horizontalLayout.addWidget(self.lbCartNum)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(ROITableWindow)
        self.tableWidget.setStyleSheet("border-color: rgb(0, 85, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 9)

        self.retranslateUi(ROITableWindow)
        QtCore.QMetaObject.connectSlotsByName(ROITableWindow)

    def retranslateUi(self, ROITableWindow):
        _translate = QtCore.QCoreApplication.translate
        ROITableWindow.setWindowTitle(_translate("ROITableWindow", "Form"))
        self.label.setText(_translate("ROITableWindow", "废票ROI图列表"))
        self.label1.setText(_translate("ROITableWindow", "车号："))
        self.lbCartNum.setText(_translate("ROITableWindow", "TextLabel"))


