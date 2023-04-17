import sys
import shelve

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, pyqtSlot, QSize
from ui_pramaSetup import Ui_winParamSetup
from infoMessageBox import InfoMessageBox
import cv2

class ParamSetupWin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_winParamSetup()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint |Qt.WindowStaysOnTopHint)
        self.setAutoFillBackground(True)
        self.infoBox=InfoMessageBox(self)
        self.infoBox.setStyleSheet("background-color:#285a91;"
                              "color:#00ffff;"
                              "font-weight:bold;"
                              "font-size:18px;" )
        # cameraCount=self.getCameraCount()
        self.ui.btnSwitch.setIcon(QIcon("icon/greenDBArrow.ico"))
        self.ui.btnSwitch.setIconSize(QSize(32, 32))
        self.cameraModified=False
        self.initParamData()


    def getCameraCount(self):
        '''
        获取摄像头数量，但是遍历需要依次捕获每个摄像头的视频流，速度有些慢，尤其是usb摄像头。
        :return:
        '''
        i=0
        while(True):
            cap = cv2.VideoCapture(i,cv2.CAP_DSHOW)
            stream=cap.grab()
            cap.release()
            if not stream :
                break
            i=i+1
        return i



    def initParamData(self):
        shelf = shelve.open('cfg')
        self.ui.lnOcrServIP.setText(shelf['ORCServer_IP'])
        self.ui.lnKernelWidth.setText(shelf['kernelWidth'])
        self.ui.lnKernelHeight.setText(shelf['kernelHeight'])
        self.ui.lnCamraWidth.setText(shelf['cameraWidth'])
        self.ui.lnCamraHeight.setText(shelf['cameraHeight'])
        self.ui.lnOcuppyMin.setText(shelf['ocuppyMin'])
        self.ui.lnOcuppyMax.setText(shelf['ocuppyMax'])
        self.ui.comCameraIndx.setCurrentText(shelf['cameraIndex'])

    @pyqtSlot(int)
    def on_comCameraIndx_currentIndexChanged(self):
        self.cameraModified=True

    @pyqtSlot()
    def on_btnSave_clicked(self):
        shelf = shelve.open('cfg')
        shelf['ORCServer_IP'] =  self.ui.lnOcrServIP.text()
        shelf['kernelWidth'] =  self.ui.lnKernelWidth.text()
        shelf['kernelHeight'] = self.ui.lnKernelHeight.text()
        shelf['cameraWidth'] =  self.ui.lnCamraWidth.text()
        shelf['cameraHeight'] =  self.ui.lnCamraHeight.text()
        shelf['ocuppyMin'] =  self.ui.lnOcuppyMin.text()
        shelf['ocuppyMax'] =  self.ui.lnOcuppyMax.text()
        shelf['cameraIndex']=self.ui.comCameraIndx.currentText()
        # self.close()

    @pyqtSlot()
    def on_btnDefault_clicked(self):

        reply=self.infoBox.warn("确定是否要恢复默认值？")
        if reply==InfoMessageBox.Yes:
            shelf = shelve.open('cfg')
            shelf['ORCServer_IP'] = '172.16.18.127'
            shelf['kernelWidth'] = '2'
            shelf['kernelHeight'] = '5'
            shelf['cameraWidth'] = '1900'
            shelf['cameraHeight'] = '1600'
            shelf['ocuppyMin'] = '7'
            shelf['ocuppyMax'] = '11'
            shelf['cameraIndex']='0'
            shelf.close()
            self.initParamData()

    @pyqtSlot()
    def on_btnSwitch_clicked(self):
        '''
        交换卷积kernel宽与高
        :return:
        '''
        width=self.ui.lnKernelWidth.text()
        self.ui.lnKernelWidth.setText(self.ui.lnKernelHeight.text())
        self.ui.lnKernelHeight.setText(width)



    @pyqtSlot()
    def on_btnClose_clicked(self):
        self.close()


    def closeEvent(self, QCloseEvent):
        if self.cameraModified:
            reply = self.infoBox.warn("摄像头参数修改，需重启程序生效")
        else:
            reply = self.infoBox.warn("确定已经保存修改？")
        if reply == InfoMessageBox.Yes:
            self.on_btnSave_clicked()
            self.close()
        else:
            QCloseEvent.ignore()



if __name__ == "__main__":


    app = QApplication(sys.argv)
    mainWin = ParamSetupWin()
    mainWin.show()

    sys.exit(app.exec_())