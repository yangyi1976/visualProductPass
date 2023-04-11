import sys
import shelve
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt,pyqtSlot
from ui_pramaSetup import Ui_winParamSetup
from infoMessageBox import InfoMessageBox

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
        self.initParamData()

    def initParamData(self):
        shelf = shelve.open('cfg')
        self.ui.lnOcrServIP.setText(shelf['ORCServer_IP'])
        self.ui.lnKernelWidth.setText(shelf['kernelWidth'])
        self.ui.lnKernelHeight.setText(shelf['kernelHeight'])
        self.ui.lnCamraWidth.setText(shelf['cameraWidth'])
        self.ui.lnCamraHeight.setText(shelf['cameraHeight'])
        self.ui.lnOcuppyMin.setText(shelf['ocuppyMin'])
        self.ui.lnOcuppyMax.setText(shelf['ocuppyMax'])

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
        print("save")
        self.close()

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
            shelf.close()
            self.initParamData()


if __name__ == "__main__":


    app = QApplication(sys.argv)
    mainWin = ParamSetupWin()
    mainWin.show()

    sys.exit(app.exec_())