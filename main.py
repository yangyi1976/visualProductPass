import  sys,os
import shelve
from PyQt5 import QtGui
from PyQt5.QtCore import QEvent, Qt, QSize, QPoint, pyqtSlot, QDir
from PyQt5.QtWidgets import QApplication, QWidget, QListView, QListWidgetItem, QLabel, QMessageBox, QMenu, QAction, \
    QFileDialog
from ui_mainWindow import Ui_Form
from cameraThread import CameraThread
from ViewImageWin import ViewImageWidget
from PyQt5.QtGui import QPixmap, QIcon, QBrush, QCursor, QTransform
from roiTableWindow import ViewROITableWin
from paramSetupWindow import ParamSetupWin
from cartROIdetct import  CartROIdetector
import  cv2
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
class MainWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.lbCamera.setMouseTracking(True)
        self.ui.lbCamera.installEventFilter(self) #安装事件监听器
        self.ui.btnSetup.setText("")
        self.ui.btnSetup.setIcon(QIcon("icon/setup.ico"))
        self.ui.btnSetup.setIconSize(QSize(32,32))
        self.ui.btnCounterRot.setIcon(QIcon("icon/rotate-left.ico"))
        self.ui.btnCounterRot.setIconSize(QSize(32,32))
        self.ui.btnRot.setIcon(QIcon("icon/rotate-right.ico"))
        self.ui.btnRot.setIconSize(QSize(32, 32))
        self.ui.btnViewROITable.setIcon(QIcon("icon/winprops.ico"))
        self.ui.btnViewROITable.setIconSize(QSize(32, 32))
        self.ui.btnUploadRIO.setIcon(QIcon("icon/remote.ico"))
        self.ui.btnUploadRIO.setIconSize(QSize(32, 32))
        self.ui.btnUpLocal.setIcon(QIcon("icon/kwrite.ico"))
        self.ui.btnUpLocal.setIconSize(QSize(32, 32))
        # self.ui.lbCamera.setScaledContents(True)

        self.lButtonDownFlag = False
        self.startPY = 0
        self.startPX = 0
        self.endPX = 0
        self.endPY = 0
        self.rectH = 0
        self.rectW = 0
        self.listROI_fileName=[]
        self.getInitParam() #获取配置参数
        self.cap = cv2.VideoCapture(self.cameraIndex, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW参数为操作系统提供的后台视频流库处理接口
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


        self.th = CameraThread(self.cap)
        self.th.flashPixmap.connect(self.setImage)
        self.th.start()
        self.showMaximized()
        self.setWindowTitle("废票信息可视化传递")
        self.initListWidget()  #初始化水平图片显示组件
        self.label_mousePos = QLabel( self.ui.lbCamera,alignment=Qt.AlignCenter)
        self.label_mousePos.setStyleSheet('background-color:green; border: 1px solid black')
        self.cartNoDetector=CartROIdetector()


    def initListWidget(self):
        self.ui.lsImgROIWidget.setFlow(QListView.Flow(1))  # 0: left to right,1: top to bottom
        self.ui.lsImgROIWidget.setViewMode(QListView.IconMode)
        self.ui.lsImgROIWidget.setContextMenuPolicy(Qt.CustomContextMenu) #允许右键自定义菜单
        self.ui.lsImgROIWidget.customContextMenuRequested[QPoint].connect(self.rightMenuListWidget)
        h=self.ui.lsImgROIWidget.height()
        self.ui.lsImgROIWidget.setIconSize(QSize(200, h-50))
        self.ui.lsImgROIWidget.itemDoubleClicked.connect(self.showImage)
        self.lastItem=QListWidgetItem()

    def getInitParam(self):
        shelf = shelve.open('cfg')
        self.servIP = shelf['ORCServer_IP'] + ":8089"
        self.cameraIndex=int(shelf['cameraIndex'])
        shelf.close()

    def rightMenuListWidget(self):
        rightMenu = QMenu(self.ui.lsImgROIWidget)
        removeAction =QAction(u"删除", self,
                                     triggered=self.delImgListItem)  # triggered 为右键菜单点击后的激活事件。这里slef.close调用的是系统自带的关闭事件。
        removeAction.setIcon(QIcon("icon/del_x.ico"))
        rightMenu.addAction(removeAction)
        rightMenu.exec_(QCursor.pos())

    def delImgListItem(self):
        currentImgIdx = self.ui.lsImgROIWidget.currentIndex().row()
        print("del img list item:",currentImgIdx)
        os.remove(self.listROI_fileName[currentImgIdx] + ".jpg")
        del self.listROI_fileName[currentImgIdx]
        # currentItem = self.ui.lsImgROIWidget.currentItem()
        # self.ui.lsImgROIWidget.removeItemWidget(currentItem)
        self.ui.lsImgROIWidget.takeItem(currentImgIdx)  #删除listWidget里选择的item
        # self.freshImgListWidget(self.listROI_fileName)  #刷新listwidget


    def addListWidgetImageItem(self,pixImage,img_name):
        item = QListWidgetItem(QIcon(pixImage), img_name)
        self.ui.lsImgROIWidget.addItem(item)

    def splitCartNum(self,cartNumStr):
        producttype=cartNumStr[0]
        cartNum=cartNumStr[1:4]
        productId=cartNumStr[6:9]
        return cartNum,productId

    def showImage(self):
        """
        显示ROI listwidget组件里的ROI截图原始图像
        :return:
        """
        self.imageViewer=ViewImageWidget()
        currentImgIdx = self.ui.lsImgROIWidget.currentIndex().row()  #use row() when icon排列 top to bottom
        imgFileName = self.listROI_fileName[currentImgIdx]
        self.imageViewer.show_label.setPixmap(QPixmap(imgFileName+".jpg"))
        # currentItem= self.ui.lsImgROIWidget.currentItem()
        # currentItem.setBackground(QBrush(Qt.darkGreen))
        # if self.lastItem !=currentItem:
        #     self.lastItem.setBackground(QBrush())
        # self.lastItem=currentItem
        self.imageViewer.show()

        # self.imageViewer.show_label.setText("self.ui.lsImgROIWidget.currentIndex()")
        # self.currentImgIdx = self.list_widget.currentIndex().row()
        # if self.currentImgIdx in range(len(self.image_paths)):
        #     self.currentImg = QPixmap(self.image_paths[self.currentImgIdx]).scaledToHeight(400)
        #     self.show_label.setPixmap(self.currentImg)

    def setImage(self, image):   #显示摄像头图像，以及选择矩形
        # print("图片高度：",image.height())
        # print("图片宽度：

        self.frame=image
        painter = QtGui.QPainter(self.frame)
        pen = QtGui.QPen()  # 添加画笔
        pen.setColor(QtGui.QColor(0,255,0))
        pen.setWidth(3)
        painter.setPen(pen)
        # painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)
        # painter.translate(0-(self.ui.lbCamera.width()-image.width())/2,0) #图片画笔的坐标左平移
        self.xoffset=int((self.ui.lbCamera.width()-image.width())/2)

        if self.startPX != self.endPX  :
            self.rectW = self.endPX - self.startPX
            self.rectH = self.endPY - self.startPY
            painter.drawRect(self.startX, self.startPY, self.rectW,self.rectH)  # 矩形坐标+

        self.pixImage=QPixmap.fromImage(self.frame)
        self.ui.lbCamera.setPixmap(self.pixImage)
        painter.end()


    def eventFilter(self, o, evn):
        '''
        事件过滤器，需要先安装事件监听器
        :param o:  发出事件的对象
        :param evn: 事件
        :return:
        '''
        if o is self.ui.lbCamera and evn.type() == QEvent.MouseButtonPress:
            if (evn.button()==Qt.LeftButton):
                self.lButtonDownFlag = True
                self.startPX = evn.localPos().x()
                self.startPY = evn.localPos().y()

                self.endPX = evn.localPos().x()
                self.endPY = evn.localPos().y()
                self.startX = self.startPX - self.xoffset
        elif o is self.ui.lbCamera and evn.type() == QEvent.MouseMove:
            if self.lButtonDownFlag:
                if self.ui.editProductID.text()=="" or self.ui.editK.text()=="":
                    QMessageBox.information(self,"错误","请输入产品车号与开位信息")
                    self.lButtonDownFlag=False

                    return super().eventFilter(o, evn)
                self.endPX=evn.localPos().x()
                self.endPY=evn.localPos().y()
                w=abs(self.rectW)
                h=abs(self.rectH)
                self.mousePosShow(evn.pos(),w,h)

        elif o is self.ui.lbCamera and evn.type() == QEvent.MouseButtonRelease:  #鼠标释放
                self.lButtonDownFlag=False
                if self.startPX == self.endPX :
                    self.label_mousePos.close()
                    return  super().eventFilter(o, evn)

                ROIw = abs(self.rectW)   #当选择区域的方向与坐标轴相反时候，需要计算起始点
                startX= self.startX if self.rectW>0 else self.startX + self.rectW
                ROIh = abs(self.rectH)
                startPY=self.startPY if self.rectH>0 else self.startPY+self.rectH

                #保存ROI截图----以 img\车号 为目录存放，车号开位为文件名
                dirName="img\\"+self.ui.editProductID.text()
                if not os.path.isdir(dirName):    #当前目录是否存在
                    os.makedirs(dirName)
                imgFileName=str(self.ui.editProductID.text()+"#"+self.ui.editK.text())
                fileFullPath = dirName+"\\" + imgFileName
                imgROI = self.frame.copy(startX, startPY, ROIw, ROIh)
                imgROI.save(fileFullPath+".jpg","JPG",100) #创建ROI文件，重名就覆盖
                # 通过在文件列表里查重，判断ROI 开是否已经存在，存在，则替换listwidget里的Icon图，
                if fileFullPath in self.listROI_fileName:
                    listIndex=self.listROI_fileName.index(fileFullPath)
                    item=self.ui.lsImgROIWidget.item(listIndex)
                    item.setIcon(QIcon(QPixmap.fromImage(imgROI)))
                    self.ui.lsImgROIWidget.repaint() #刷新列表

                else:
                    self.listROI_fileName.append(fileFullPath)  #不带文件扩展名的目录+文件名列表
                    # imgROI=imgROI.scaled(w,h, Qt.KeepAspectRatio)
                    # 给水平Listwidget组件添加ROI list image
                    self.addListWidgetImageItem(QPixmap.fromImage(imgROI),imgFileName)
                self.ui.editK.setText("")
        return super().eventFilter(o, evn)


    def mousePosShow(self,pos,w,h):
        '''
        显示鼠标位置的矩形框
        :param pos: 
        :param w: 
        :param h: 
        :return: 
        '''
        delta = QPoint(30, -15)
        self.label_mousePos.show()
        self.label_mousePos.move(pos + delta)
        self.label_mousePos.setText("(%d, %d) w:%d,h:%d" % (pos.x(), pos.y(),w,h))
        self.label_mousePos.adjustSize()

    @pyqtSlot()
    def on_btnViewROITable_clicked(self):
        '''
        打开ROI图像表格窗口
        :return:
        '''
        self.viewRoiTable = ViewROITableWin(self.listROI_fileName,self.ui.editProductID.text())
        self.viewRoiTable.imageFileListChanged.connect(self.freshImgListWidget)
        self.viewRoiTable.show()

    @pyqtSlot()
    def on_btnDetcCart_clicked(self):
        #获取预处理后的车号ROI图像，cv2格式,并保存为文件。
        cartNumImg=self.th.cartNumCapture()
        fullName="img\\"+'cartNum.jpg'
        cv2.imwrite(fullName, cartNumImg)
        print("开始识别车号")
        # self.postImg(r'F:\PycharmProjects\pp_ocr_py34\img\1cartNum.jpg')
        # servIP='172.16.18.127:8089'
        try:
            self.postImg(fullName,self.servIP)
        except Exception as e:
            QMessageBox.information(self,"错误",str(e)+"\n --无法进行车号的OCR识别，请重新调整再进识别！")
        #在控件里显示车号图片
        pixImage = QPixmap(fullName)
        pixImage=pixImage.scaled(200, 190, Qt.KeepAspectRatio)
        self.ui.lbNumberpPic.setPixmap(pixImage)
        # #弹出窗口显示车号图片
        # cv2.namedWindow('cartNumImg window', cv2.WINDOW_NORMAL)
        # cv2.imshow("cartNumImg window", img)
        #让窗口居于屏幕中间显示
        # desktop = QApplication.desktop()
        # x_center=int(desktop.width()/2)
        # y_center=int(desktop.height()/2)
        # cv2.resizeWindow("cartNumImg window", img.shape[1], img.shape[0])
        # cv2.moveWindow("cartNumImg window", x_center-int(img.shape[1]/2), y_center-int(img.shape[0]/2))
        # k=cv2.waitKey(2000)
        # if k==27:
        #     return
        # cv2.destroyAllWindows()

    def postImg(self,fileName,servIP):
        '''
        将保存的车号ROI图像文件发送到OCR server，进行识别
        :param fileName:
        :param servIP: OCR server IP
        :return: json格式的识别结果，['data']['raw_out'][0][1]为车号
        '''
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
            # 'Content-type':'multipart/form-data',
            'X-Requested-With': 'XMLHttpRequest'}
        post_url='http://'+servIP+'/api/tr-run/'

        imgData = {'file': ('cartNum.jpg',open(fileName, 'rb'),'image/jpeg'),'compress':'300'}
        imgData_encoder = MultipartEncoder(imgData)
        headers['Content-type']=imgData_encoder.content_type
        # data = {'compress': '200'}  可以不用request_toolbelt库以及Content-type
        # r = requests.post(post_url, headers=headers, files=imgData_encoder,data=data)
        try:
            res = requests.post(post_url,headers=headers, data=imgData_encoder)
            res.raise_for_status()
        except requests.exceptions.ConnectionError as e:
            raise e
        ocrtxt=res.json()
        print(ocrtxt['data']['raw_out'])
        if len(ocrtxt['data']['raw_out'])<1:
            QMessageBox.information(self,"错误","未能识别车号，请调整产品位置并重新识别")
            return False
        else:
            cartNum=ocrtxt['data']['raw_out'][0][1]
            cartNum=cartNum[3:]  #获取字符串列表 ‘1、 ’ 后面的，即从第4个字符开始
            #此处应进一步判断读入的车号格式是否正确

            self.ui.editProductID.setText(cartNum)
            return True


    @pyqtSlot()
    def on_btnUploadRIO_clicked(self):
        #上传完删除图像文件
        print("上传。。。。")

    @pyqtSlot()
    def on_btnUpLocal_clicked(self):
        '''
        上传本地图片
        :return:
        '''
        # curPath=QDir.currentPath()
        curPath="C:\\Users\\Administrator\\Desktop"
        filt="图片文件(*.jpg *.jpeg *.png);;所有文件(*.*);"
        fileList,filtUsed=QFileDialog.getOpenFileNames(self,"选择一个图片文件",curPath,filt)
        for i in range(len(fileList)):
            fileName=(fileList[i])[:fileList[i].find(".")]
            fileName=fileName.replace("/","\\")
            self.listROI_fileName.append(fileName)

    def freshImgListWidget(self, imgFileList):
        '''
        刷新 img listwidget
        :param imgFileList: img 列表，
        :return:
        '''
        self.ui.lsImgROIWidget.clear()
        for n in range(len(imgFileList)):
            paperPixmap = QPixmap()
            paperPixmap.load(imgFileList[n] + ".jpg")
            fileName = (imgFileList[n])[imgFileList[n].rfind('\\') + 1:]
            self.addListWidgetImageItem(paperPixmap,fileName)

    @pyqtSlot()
    def on_btnSetup_clicked(self):
        self.paramSetupWin=ParamSetupWin()
        self.paramSetupWin.show()

    @pyqtSlot()
    def on_btnCounterRot_clicked(self):
        '''
        图像反时针旋转90度
        :return:
        '''
        currentImgIdx = self.ui.lsImgROIWidget.currentIndex().row()
        print("rotate img list item:", currentImgIdx)
        if currentImgIdx == -1:
            return
        fileName = self.listROI_fileName[currentImgIdx] + '.jpg'
        roiPix = QPixmap(fileName)
        transfer = QTransform()
        transfer.rotate(-90)
        roiPix = roiPix.transformed(transfer)
        roiPix.save(fileName)
        self.freshImgListWidget(self.listROI_fileName)  # 刷新listwidget
        self.ui.lsImgROIWidget.setCurrentRow(currentImgIdx)

    @pyqtSlot()
    def on_btnRot_clicked(self):
        '''
        图像顺时针旋转90度，其实旋转的是图像文件
        :return:
        '''
        currentImgIdx = self.ui.lsImgROIWidget.currentIndex().row()
        print("rotate img list item:", currentImgIdx)
        if currentImgIdx==-1 :
            return
        fileName=self.listROI_fileName[currentImgIdx]+'.jpg'
        roiPix=QPixmap(fileName)
        transfer=QTransform()
        transfer.rotate(90)
        roiPix=roiPix.transformed(transfer)
        roiPix.save(fileName)
        self.freshImgListWidget(self.listROI_fileName)  # 刷新listwidget，重新加载图像文件列表
        self.ui.lsImgROIWidget.setCurrentRow(currentImgIdx)

    def closeEvent(self,event):
        print("关闭主程序窗口")
        self.th.cap.release()
        self.th.exit()



if __name__=="__main__":
    app=QApplication(sys.argv)
    mainWin=MainWindow()

    mainWin.show()

    sys.exit(app.exec_())