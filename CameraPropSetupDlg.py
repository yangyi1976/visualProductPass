import sys,cv2
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QPushButton, QDialogButtonBox
from PyQt5.QtCore import Qt, pyqtSlot

from CameraConf import CameraConf
from ui_cameraPropSetup import Ui_CameraPropDlg

class CameraPropSetupDlg(QDialog):
    def __init__(self,cap,parent=None):
        super().__init__(parent)
        self.ui=Ui_CameraPropDlg()
        self.ui.setupUi(self)
        self.setWindowTitle("相机设置")
        self.setWindowFlags(Qt.Drawer|Qt.MSWindowsFixedSizeDialogHint)  #只显示关闭图标，并固定窗口大小
        btnSave=QPushButton('保存',self)
        btnCancle=QPushButton('关闭',self)
        self.ui.buttonBox.addButton(btnSave,QDialogButtonBox.AcceptRole)  #添加自定义按钮给buttonbox控件，默认是ok&cancle
        self.ui.buttonBox.addButton(btnCancle, QDialogButtonBox.RejectRole)
        self.ui.buttonBox.accepted.connect(self.onAccepted)
        self.ui.buttonBox.rejected.connect(self.onRejected)
        self.ui.SliderZoom.valueChanged.connect(self.changeZoom)
        self.ui.SliderBrightness.valueChanged.connect(self.changeBrightness)
        self.ui.SliderContrast.valueChanged.connect(self.changeContrast)
        self.cap=cap
        self.initCameraProp()

    def initCameraProp(self):
        zoom=self.cap.get(cv2.CAP_PROP_ZOOM)
        brightness=self.cap.get(cv2.CAP_PROP_BRIGHTNESS)
        contrast=self.cap.get(cv2.CAP_PROP_CONTRAST)
        self.ui.SliderZoom.setValue(zoom)
        self.ui.SliderBrightness.setValue(brightness)  #让亮度滑块居中
        self.ui.SliderContrast.setValue(contrast)

    @pyqtSlot()
    def on_btnDefault_clicked(self):
        '''
        设置摄像头参数为默认值
        :return:
        '''
        self.cap.set(cv2.CAP_PROP_ZOOM, 0)
        self.cap.set(cv2.CAP_PROP_BRIGHTNESS, 0)
        self.cap.set(cv2.CAP_PROP_CONTRAST, 32)
        self.ui.SliderZoom.setValue(0)
        self.ui.SliderBrightness.setValue(0)  # 让亮度滑块居中
        self.ui.SliderContrast.setValue(32)

        # self.cap.set(cv2.CAP_PROP_SETTINGS)
        # self.cap.set(cv2.CAP_PROP_AUTOFOCUS,1)
        # self.cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)

    def  changeZoom(self,value):
        print("zoom changing to:",value)
        self.cap.set(cv2.CAP_PROP_ZOOM, value)

    def changeBrightness(self,value):
        print("bright changing ...",value)
        self.cap.set(cv2.CAP_PROP_BRIGHTNESS, value)

    def changeContrast(self,value):
        print("contrast changing ...")
        self.cap.set(cv2.CAP_PROP_CONTRAST, value)

    def onAccepted(self ):
        # 保存参数
        param={}
        param['zoom']=str(self.ui.SliderZoom.value())
        param['bright']=str(self.ui.SliderBrightness.value())
        param['contrast']=str(self.ui.SliderContrast.value())
        cameraCfg = CameraConf()
        cameraCfg.saveCamera(param)

    def onRejected(self):
        print("rejected close")
        self.close()

    def closeEvent(self, QCloseEvent):
        print("close event")


if __name__=="__main__":
    app=QApplication(sys.argv)
    cap=""
    cameraPropDlg=CameraPropSetupDlg(cap)
    if cameraPropDlg.exec_()==QDialog.Accepted:
        print("show  Accepted")
        # sys.exit(app.exec_()) #加上此句，app实例无法完全退出
