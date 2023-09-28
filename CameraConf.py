from configparser import ConfigParser
import cv2
from PyQt5.QtWidgets import QMessageBox, QDialog
class CameraConf:
    def getCameraConf(self):
        '''
        获取摄像头配置
        :return:
        '''
        cfg = ConfigParser()
        cfg.read('cameraParam.ini')
        return cfg

    def setCamera(self, cap):
        cfg = self.getCameraConf()
        cap.set(cv2.CAP_PROP_FPS, int(cfg.get('camera', 'fps')))
        # cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)
        cap.set(cv2.CAP_PROP_ZOOM, int(cfg.get('camera', 'zoom')))

        cap.set(cv2.CAP_PROP_BRIGHTNESS, int(cfg.get('camera', 'bright')))
        cap.set(cv2.CAP_PROP_CONTRAST, int(cfg.get('camera', 'contrast')))

    def saveCamera(self,param):
        cfg=self.getCameraConf()
        cfg['camera']['zoom']=param['zoom']
        cfg['camera']['bright']=param['bright']
        cfg['camera']['contrast']=param['contrast']
        with open('cameraParam.ini', mode='w') as fp:
            cfg.write(fp)
        QMessageBox.information(QDialog(), '信息', '保存成功！')