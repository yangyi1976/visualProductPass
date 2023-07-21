from PyQt5.QtCore import  QThread, pyqtSignal, Qt
from PyQt5.QtGui import  QImage

from CameraConf import CameraConf
from cartROIdetct import CartROIdetector
import  cv2, time

class CameraThread(QThread):#采用线程来播放视频

    flashPixmap = pyqtSignal(QImage)


    def __init__(self,cap):
        super().__init__()
        self.cap=cap
        self.cartNoDetector=CartROIdetector()
        #根据cameraparam.ini文件设置摄像头参数
        cameraCfg = CameraConf()
        cameraCfg.setCamera(self.cap)

    def __del__(self):
        print("拍照线程析构。。。。。")

    def setCameraWH(self,w,h):
        '''
        设置摄像头原始分辨率及其他属性
        :param w:
        :param h:
        :return:
        '''
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')) #设置成视频流mjpg格式，默认为yuy2
        self.cap.set(cv2.CAP_PROP_FPS, 30)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(w))
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(h))

        # self.cap.set(cv2.CAP_PROP_ZOOM, 60)
        # self.cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)




    # def setScreenWH(self,w,h):
    #     self.screenW=w
    #     self.screenH=h
    def setVideoSize(self,w,h):
        '''
        根据label image控件的尺寸设置视频显示尺寸。
        :param w: ui.lbCamera控件的宽
        :param h:
        :return:
        '''
        self.videoW=w
        self.videoH=h
        # self.videoW=h*16/9
    def cartNumCapture(self):
       '''
       车号图片截图
       :return: cv2数组格式的图片
       '''
       cartNumImg= self.cartNoDetector.getCartROIimg(self.frame)   #传入原始帧图片
       return  cartNumImg

    def run(self):
        # cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)  #cv2.CAP_DSHOW参数为操作系统提供的后台视频流库处理接口类型

        print("开始捕捉")
        while (self.cap.isOpened()==True):
            ret, self.frame = self.cap.read()
            if ret:
                # x, y, w, h = self.cartNoDetector.getCartNumRect(frame)  获取车号文字区域坐标
                # cv2.rectangle(rgbImage, (x - 3, y - 3), (x + w + 3, y + h + 3), (255, 0, 0), 2)
                rgbImage = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                # rgbImage = cv2.flip(rgbImage, 1)  #沿Y轴图像反转
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)#在这里可以对每帧图像进行处理，
                img = convertToQtFormat.scaled(self.videoW, self.videoH, Qt.KeepAspectRatio)

                self.flashPixmap.emit(img)
                time.sleep(0.02) #控制视频播放的速度
            else:
                break

        self.cap.release()