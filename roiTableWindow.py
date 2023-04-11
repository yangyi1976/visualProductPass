import os
import sys

from infoMessageBox import InfoMessageBox
from PyQt5.QtCore import  Qt,   QSize,  pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

from PyQt5.QtGui import QPixmap, QIcon, QFont, QBrush, QColor
from ui_roitable import Ui_ROITableWindow
from zoomImgWiin import ZoomImgwin



class ViewROITableWin(QWidget):

    imageFileListChanged=pyqtSignal(list)
    def __init__(self, imgFileList,carttNo,parent=None):
        super().__init__(parent)
        self.ui = Ui_ROITableWindow()
        self.ui.setupUi(self)
        self.setFixedWidth(1180)
        self.setWindowFlags(Qt.WindowCloseButtonHint |Qt.WindowStaysOnTopHint)
        # self.resize(1160,900)
        self.imgFileList=imgFileList
        self.ui.lbCartNum.setText(carttNo)
        rows= (len(imgFileList)//4 )+1 if len(imgFileList)%4 >0 else len(imgFileList)//4   #//向下取整
        self.displayROITable(rows, 4)   #一行四列


    def displayROITable(self,rows,cols):
        '''
        显示ROI图表格
        :param rows:
        :param cols:
        :return:
        '''

        self.ui.tableWidget.setColumnCount(cols)
        self.ui.tableWidget.setRowCount(rows)
        # self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setIconSize(QSize(64, 64));

        self.ui.tableWidget.horizontalHeader().setVisible(False)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.setStyleSheet("gridline-color: rgb(0, 202, 202);")
        for i in range(cols):  # 让列宽和图片相同
            self.ui.tableWidget.setColumnWidth(i, 286)
        for i in range(rows):  # 让行高和图片相同
            self.ui.tableWidget.setRowHeight(i, 200)

        imgCount=len(self.imgFileList)
        for k in range(imgCount):
            i = k // 4  #行数，取商（整数），/ 结果为浮点数，不是整数。
            j = k % 4   # 取余数
            # item = QTableWidgetItem()
            # item.setFlags(Qt.ItemIsEnabled)  # 用户点击时表格时，图片被选中
            # icon = QIcon("img\\a004.jpg")
            # item.setIcon(QApplication.style().standardIcon(60))
            self.cellDisplayImage(i,j,k)

    def cellDisplayImage(self,i,j,k):
        '''
        在每个单元格里显示图片
        :param i: 显示在表格第i行
        :param j: 在表格第j列
        :param k: 文件列表中的索引位置
        :return:
        '''
        lbPixmap = pixmapLabel()
        paperPixmap=QPixmap()
        paperPixmap.load(self.imgFileList[k]+".jpg")
        lbPixmap.setPixmap(paperPixmap)
        lbPixmap.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        btnDel = QPushButton()
        lbPixname = QLabel()
        lbPixname.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        lbPixname.setFixedHeight(30)
        btnDel.setFixedSize(30, 30)
        lbPixmap.setStyleSheet("border:0px solid red;")
        #获取文件路径最后一个\后面的文件名
        fileName=(self.imgFileList[k])[self.imgFileList[k].rfind('\\')+1:]
        lbPixname.setStyleSheet("background:black;color:white;font-size:14px")
        lbPixname.setFont(QFont('微软雅黑', 14))
        lbPixname.setText(fileName)
        # btnDel.setIcon(QApplication.style().standardIcon(60))
        btnDel.setIconSize(QSize(24,24))
        btnDel.setIcon(QIcon("icon/del_can.ico"))

        # self.ui.tableWidget.setCellWidget(i,j,lb)
        # 单元格添加多个控件/
        vLayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        vLayout.addWidget(lbPixmap)
        hlayout.addWidget(btnDel)
        hlayout.addWidget(lbPixname)

        vLayout.addLayout(hlayout)
        cellWidget = QWidget()  # 构建一个组件放入单元格中
        cellWidget.setStyleSheet("border:1px solid #ffffff;")
        btnDel.setStyleSheet("background-color: rgba(255, 255, 255, 0);border:0px groove cyan;")
        cellWidget.setLayout(vLayout)
        self.ui.tableWidget.setCellWidget(i, j, cellWidget)

        btnDel.clicked.connect(lambda :self.delImage(k))
        lbPixmap.clicked.connect(lambda :self.zoomImage(k))
        # print('e/icons/%d.png i=%d  j=%d' % (k, i, j))
        # self.ui.tableWidget.setItem(i, j, item)

    def delImage(self,k):
        messageWidget=InfoMessageBox(self)
        messageWidget.setStyleSheet("background-color:#285a91;"
                                    "color:#00ffff;"
                                    "font-weight:bold;"
                                    "font-size:18px;"
                                    )
        reply=messageWidget.warn("是否要删除此ROI图像？")

        if reply==QMessageBox.Yes:

            # self.ui.tableWidget.removeCellWidget(i,j)
            os.remove(self.imgFileList[k]+".jpg")
            del self.imgFileList[k]
            #重新显示表格
            self.ui.tableWidget.clear()
            rows = (len(self.imgFileList) // 4) + 1 if len(self.imgFileList) % 4 > 0 else len(self.imgFileList) // 4
            self.displayROITable(rows, 4)
            # self.imageFileListChanged.emit(self.imgFileList)  #将删除后的img列表传递出去。
    #
    @pyqtSlot(int,int,int,int)
    def on_tableWidget_currentCellChanged(self,curretRow,currentCol,previousRow,previousCol):
        '''
        切换单元格时候改变上一次单元格的背景颜色
        :param curretRow:
        :param currentCol:
        :param previousRow:
        :param previousCol:
        :return:
        '''
        if previousCol==-1 or previousRow==-1:
            return
        self.ui.tableWidget.cellWidget(previousRow, previousCol).setStyleSheet("background-color:rgba(255,255,255,0);")

    def zoomImage(self,k):
        '''
        显示第k个图像文件的原始图像，可放大。
        :param k:
        :return:
        '''
        i = k // 4  # 取商（整数），/ 结果为浮点数，不是整数。
        j = k % 4
        print("放大图片:", k)
        self.ui.tableWidget.cellWidget(i,j).setStyleSheet("background-color:cyan;")
        self.imgWin=ZoomImgwin( )  #显示放大图片的窗口
        self.imgWin.setWindowTitle(self.imgFileList[k]+".jpg")
        self.imgWin.ui.lbZoomImg.setAlignment(Qt.AlignCenter)
        self.imgWin.setWindowFlags(Qt.WindowCloseButtonHint |Qt.WindowStaysOnTopHint)
        paperPixmap = QPixmap()
        paperPixmap.load(self.imgFileList[k]+".jpg")
        h=paperPixmap.height()
        w=paperPixmap.width()
        self.imgWin.resize(w,h)
        self.imgWin.ui.lbZoomImg.setPixmap(paperPixmap)
        self.imgWin.show()

    def setImgFileList(self,fileNameList):
        self.imgFileList=fileNameList
        self.displayROITable(len(fileNameList)/4,4)

    def closeEvent(self, event):
        self.imageFileListChanged.emit(self.imgFileList)  # 关闭窗口前给父窗口返回删除后的img list
        event.accept()
        self.close()

#图片显示类，重载鼠标点击事件
class pixmapLabel(QLabel):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = ViewROITableWin()
    mainWin.show()

    sys.exit(app.exec_())