from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QImage
from cartROIdetct import CartROIdetector
import  cv2, time

class CameraThread(QThread):#采用线程来播放视频

    flashPixmap = pyqtSignal(QImage)


    def __init__(self,cap):
        super().__init__()
        self.cap=cap
        self.cartNoDetector=CartROIdetector()

    def __del__(self):
        print("拍照线程析构。。。。。")

    def cartNumCapture(self):
       '''
       车号图片截图
       :return: cv2数组格式的图片
       '''
       cartNumImg= self.cartNoDetector.getCartROIimg(self.frame)
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
                img = convertToQtFormat.scaled(1024, 540, Qt.KeepAspectRatio)
                self.flashPixmap.emit(img)
                time.sleep(0.1) #控制视频播放的速度
            else:
                break

        self.cap.release()