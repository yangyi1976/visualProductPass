import  sys,os,time
import shelve
from PyQt5 import QtGui
from PyQt5.QtCore import QEvent, Qt, QSize, QPoint, pyqtSlot,  QProcess
from PyQt5.QtWidgets import QApplication, QWidget, QListView, QListWidgetItem, QLabel, QMessageBox, QMenu, QAction, \
    QFileDialog

from CameraPropSetupDlg import CameraPropSetupDlg
from ui_mainWindow import Ui_Form
from cameraThread import CameraThread
from delFileByDaysThread import DelFileByDaysThread
from ViewImageWin import ViewImageWidget
from PyQt5.QtGui import QPixmap, QIcon, QCursor, QTransform
from roiTableWindow import ViewROITableWin
from paramSetupWindow import ParamSetupWin
from cartROIdetct import  CartROIdetector
import  cv2
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class MainWindow(QWidget):

    def __init__(self,parent=None):

        if hasattr(sys, 'frozen'):
            os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
        super().__init__(parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.lbCamera.setMouseTracking(True)
        self.ui.lbCamera.installEventFilter(self) #安装事件监听器
        self.ui.btnSetup.setText("")
        #QIcon来自资源文件pic_rc.py,路径格式:icon/icon/*.ico,也可以之前来自ico文件icon/*.ico
        self.setWidgetsIcon()
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
        #删除文件存储时间大于指定天数的文件夹
        self.delFilesTh=DelFileByDaysThread(self.storeFilesDays)
        self.delFilesTh.start()
        self.showMaximized()
        self.ui.editFlag.setText("5")
        # 初始化车号文本框
        year = time.gmtime().tm_year
        year=year%100     # get the last 2bits of year
        yearlist = [str(year - 1), str(year), str(year + 1)]
        self.ui.comYear.clear()
        self.ui.comYear.addItems(yearlist)
        self.ui.comYear.setCurrentIndex(1)
        QApplication.processEvents()
        self.setWindowTitle("废票信息可视化传递")

        self.initListWidget()  #初始化水平图片显示组件
        self.cap = cv2.VideoCapture(self.cameraIndex + cv2.CAP_DSHOW)  # cv2.CAP_DSHOW参数为操作系统提供的后台视频流库处理接口
        self.th = CameraThread(self.cap)
        self.th.setCameraWH(int(self.cameraWidth),int(self.cameraHeight))  #根据配置文件设置摄像头分辨率
        self.th.setVideoSize(self.ui.lbCamera.width()-60, self.ui.lbCamera.height()-20) #按照控件尺寸缩放视频
        self.th.flashPixmap.connect(self.setImage)
        self.th.start()
        self.label_mousePos = QLabel( self.ui.lbCamera,alignment=Qt.AlignCenter)
        self.label_mousePos.setStyleSheet('background-color:green; border: 1px solid black')
        self.cartNoDetector=CartROIdetector()
        self.ui.editK.editingFinished.connect(self.editK_finish)
        print("初始化时：", self.ui.lbCamera.width(), self.ui.lbCamera.height())

    def setWidgetsIcon(self):
        self.ui.btnSetup.setIcon(QIcon(":icon/icon/setup.ico"))
        self.ui.btnSetup.setIconSize(QSize(64, 64))
        self.ui.btnCounterRot.setIcon(QIcon(":icon/icon/rotate-left.ico"))
        self.ui.btnCounterRot.setIconSize(QSize(32, 32))
        self.ui.btnRot.setIcon(QIcon(":icon/icon/rotate-right.ico"))
        self.ui.btnRot.setIconSize(QSize(32, 32))
        self.ui.btnViewROITable.setIcon(QIcon(":icon/icon/winprops.ico"))
        self.ui.btnViewROITable.setIconSize(QSize(32, 32))
        self.ui.btnUploadRIO.setIcon(QIcon(":icon/icon/remote.ico"))
        self.ui.btnUploadRIO.setIconSize(QSize(32, 32))
        self.ui.btnUpLocal.setIcon(QIcon(":icon/icon/kwrite.ico"))
        self.ui.btnUpLocal.setIconSize(QSize(32, 32))

    def initListWidget(self):
        self.ui.lsImgROIWidget.setFlow(QListView.Flow(1))  # 0: left to right,1: top to bottom
        self.ui.lsImgROIWidget.setViewMode(QListView.IconMode)
        self.ui.lsImgROIWidget.setContextMenuPolicy(Qt.CustomContextMenu) #允许右键自定义菜单
        self.ui.lsImgROIWidget.customContextMenuRequested[QPoint].connect(self.rightMenuListWidget)
        h=self.ui.lsImgROIWidget.height()-40
        self.ui.lsImgROIWidget.setIconSize(QSize(h/0.75, h))  #4；3显示ROI图
        self.ui.lsImgROIWidget.itemDoubleClicked.connect(self.showImage)
        self.lastItem=QListWidgetItem()

    def getInitParam(self):
        shelf = shelve.open('cfg')
        self.OCRServIP = shelf['ORCServer_IP'] + ":8089"
        self.cameraIndex=int(shelf['cameraIndex'])
        self.storeFilesDays=int(shelf['storeFilesDays'])
        self.uploadUrl="http://"+shelf['upload_servIp']+":"+shelf['upload_servPort']+shelf['upload_servAPI']
        self.uploadParamUrl=shelf['uploadPosParams_API']
        self.cartInfoUrl=shelf['getCartInfo_API']
        self.cameraHeight=shelf['cameraHeight']
        self.cameraWidth=shelf['cameraWidth']
        shelf.close()
        #获取屏幕分辨率尺寸
        self.screenW,self.screenH=self.getScreenRect()

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
        del listformatPosInfo[currentImgIdx]   #清空开位信息列表
        # currentItem = self.ui.lsImgROIWidget.currentItem()
        # self.ui.lsImgROIWidget.removeItemWidget(currentItem)
        self.ui.lsImgROIWidget.takeItem(currentImgIdx)  #删除listWidget里选择的item
        # self.freshImgListWidget(self.listROI_fileName)  #刷新listwidget

    def addListWidgetImageItem(self,pixImage,img_name):
        item = QListWidgetItem(QIcon(pixImage), img_name)
        self.ui.lsImgROIWidget.addItem(item)

    def splitCartNum(self,cartNumStr):  #将条码ID拆分成产品类型与车号
        producttype=cartNumStr[0]
        cartNum=cartNumStr[1:5]  #1-4位
        productId=cartNumStr[5:10]
        return producttype,cartNum

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
    @pyqtSlot()

    def editK_finish(self):
        '''
        2T\3T, 为40K；4T-7T，为35k。其余默认99k
        :return:
        '''
        maxK=99
        if self.ui.editProductType.text()=="" or len(self.ui.editProductID.text())!=4:
            QMessageBox.information(self, "错误", " 录入正确格式的产品车号！")
            self.ui.editK.clear()
            return
        elif 3<int(self.ui.editProductType.text())<=7:
            maxK=35
        elif self.ui.editProductType.text() =='2'or self.ui.editProductType.text()=='3':
            maxK=40
        if self.ui.editK.text().isnumeric():
            if self.ui.editK.isModified():
                k=int(self.ui.editK.text())
                if k>maxK:
                    QMessageBox.information(self, "错误", "开位超过最大值 %d，请输入正确开位值！" %maxK)
                    self.ui.editK.clear()
            self.ui.editK.setModified(False)
        elif self.ui.editK.text() !="":
            QMessageBox.information(self, "错误", " 请输入数字")
            self.ui.editK.clear()

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
                if len(self.ui.editProductID.text())!=4 or self.ui.editK.text()=="":
                    QMessageBox.information(self,"错误","请输入正确的产品车号与开位信息")
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
                # global  params
                formatPosInfo['format_pos'] = self.ui.editK.text()
                formatPosInfo['remark'] = self.ui.txtDescribe.toPlainText()
                fileFullPath = dirName+"\\" + imgFileName
                imgROI = self.frame.copy(startX, startPY, ROIw, ROIh)
                imgROI.save(fileFullPath+".jpg","JPG",100) #创建ROI文件，重名就覆盖
                # 通过在文件列表里查重，判断ROI 开是否已经存在，存在，则替换listwidget里的Icon图，
                if fileFullPath in self.listROI_fileName:
                    listIndex=self.listROI_fileName.index(fileFullPath)
                    item=self.ui.lsImgROIWidget.item(listIndex)
                    item.setIcon(QIcon(QPixmap.fromImage(imgROI)))
                    self.ui.lsImgROIWidget.repaint() #刷新列表
                    #更换开信息列表里的开信息
                    listformatPosInfo[listIndex]=formatPosInfo
                else:
                    self.listROI_fileName.append(fileFullPath)  #添加改RIO截图文件名
                    # imgROI=imgROI.scaled(w,h, Qt.KeepAspectRatio)
                    # 给水平Listwidget组件添加ROI list image
                    self.addListWidgetImageItem(QPixmap.fromImage(imgROI),imgFileName)
                    listformatPosInfo.append(formatPosInfo)
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
        self.viewRoiTable = ViewROITableWin(self.listROI_fileName,self.ui.editProductID.text(),listformatPosInfo)
        self.viewRoiTable.imageFileListChanged.connect(self.freshImgListWidget)
        self.viewRoiTable.show()

    @pyqtSlot()
    def on_btnDetcCart_clicked(self):
        '''
        根据车号ROI识别OCR车号，并从MES中获取该车号对应的车号信息。
        :return:
        '''
        #获取预处理后的车号ROI图像，cv2格式,并保存为文件。
        cartNumImg=self.th.cartNumCapture()
        fullName="img\\"+'cartNum.jpg'
        cv2.imwrite(fullName, cartNumImg)
        print("开始识别车号")
        ## self.postImg(r'F:\PycharmProjects\pp_ocr_py34\img\1cartNum.jpg')
        ## servIP='172.16.18.127:8089'
        try:
            cartId=self.postImg(fullName,self.OCRServIP) #发送图片到ocr服务器
        except Exception as e:
            QMessageBox.information(self,"错误",str(e)+"\n --无法进行车号的OCR识别，请重新调整再进识别！")
        #在控件里显示车号图片
        pixImage = QPixmap(fullName)
        pixImage=pixImage.scaled(200, 190, Qt.KeepAspectRatio)
        self.ui.lbNumberpPic.setPixmap(pixImage)
        productType,cartNum=self.splitCartNum(cartId)  #条码ID拆分成产品类与大万号
        self.ui.editProductType.setText(productType)
        self.ui.editProductID.setText(cartNum)
        #拼接完整车号
        # carNo=self.ui.comYear.currentText()+"7"+self.ui.editFlag.text()+self.ui.editProductID.text()
        carNo=self.getWholeCartNo()
        # 通过MES接口根据车号获取工序，机台以及设备
        self.cartInfo=self.getCartInfoByCartNo(carNo, self.cartInfoUrl)
        print("车号：",self.cartInfo)
        if self.cartInfo !={} :
            w=self.cartInfo['currentWorkSeq']               #workseq format: "big_Seq"."producttype"."sub_Seq"
            if w is not  None:
                self.ui.lbWorkSeq.setText(w[w.rfind('.')+1:])   #get "sub_Seq" after the last '.'
                self.ui.lbMachineLeader.setText( self.cartInfo['machineLeader'])
            else:
                QMessageBox.information(self, "错误", "无法获取该车号的当前工序，请确认车号是否正确！")
        else:
            QMessageBox.information(self, "错误", "MES系统接口异常，无法获取产品当前机台信息" )


    def getCartInfoByCartNo(self,cartNo,cartInfoUrl):
        '''
        根据车号，从MES获取车号信息：工序、几台、设备等。
        :param cartNo:车号
        :param getCartInfoUrl:MES接口API地址
        :return: cartInfo 车号信息
        '''
        headers = {'Content-type': 'application/json'}
        param={"carno":cartNo}
        try:
            res = requests.post(cartInfoUrl, headers=headers, json=param)
        except requests.exceptions.ConnectionError as e:
            QMessageBox.information(self, "错误", "MES系统接口异常，无法获取车号信息，" + str(e))
            raise e
        resInfo = res.json()
        cartInfo={}
        if res.status_code==200:
            cartInfo['preWorkSeq']=resInfo['data'][0]['Location_Desc']       #前一工序
            cartInfo['currentEquipmentId']=resInfo['data'][0]['machine_id']   #当前设备ID
            cartInfo['currentEquipment']=resInfo['data'][0]['CurrentUnit_Desc']  #当前设备名
            cartInfo['machineLeader']=resInfo['data'][0]['Class_Desc']       #机长
            cartInfo['currentWorkSeq']=resInfo['data'][0]['Next_Location_Desc'] #当前工序
        return cartInfo

    def postImg(self,fileName,OCRServIP):
        '''
        将保存的车号ROI图像文件发送到OCR server，进行识别
        :param fileName:
        :param OCRservIP: OCR server IP
        :return: json格式的识别结果，['data']['raw_out'][0][1]为条码ID
        '''
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
            # 'Content-type':'multipart/form-data',
            'X-Requested-With': 'XMLHttpRequest'}
        post_url='http://'+OCRServIP+'/api/tr-run/'

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

            return cartNum

    @pyqtSlot()
    def on_btnGetWorkseqInfo_clicked(self):
        '''
        当可以根据手工录入的车号，获取工序信息。
        :return:
        '''
        if self.ui.editProductType.text()=="" or self.ui.editProductID.text()=="":
            QMessageBox.information(self, "错误", "还未录入车号信息！")
        carNo = self.getWholeCartNo()
        # 通过MES接口根据车号获取工序，机台以及设备
        self.cartInfo = self.getCartInfoByCartNo(carNo, self.cartInfoUrl)
        if self.cartInfo !={} :
            w=self.cartInfo['currentWorkSeq']               #workseq format: "big_Seq"."producttype"."sub_Seq"
            if w is not  None:
                self.ui.lbWorkSeq.setText(w[w.rfind('.')+1:])   #get "sub_Seq" after the last '.'
                self.ui.lbMachineLeader.setText( self.cartInfo['machineLeader'])
            else:
                QMessageBox.information(self, "错误", "无法获取该车号的当前工序，请确认车号是否正确！")
        else:
            QMessageBox.information(self, "错误", "MES系统接口异常，无法获取产品当前机台信息" )

    @pyqtSlot()
    def on_btnUploadRIO_clicked(self):
        '''
        1. 上传ROI图片 2.上传废票信息
        :return:
        '''
        #---fileName格式 img\车号\车号#开位
        #上传完清除listWidget列表及listParams列表
        imgInfo = {}          #要上传的ROI图像信息
        global listformatPosInfo       #字典变量可以不加全局
        params['cart_number']=self.getWholeCartNo()
        params['pu_desc']= '胶一印' #self.ui.lbWorkSeq.text()
        params['machine_id']=7704  #self.cartInfo['currentEquipmentId']
        params['machine_name']=self.cartInfo['currentEquipment']
        params['captain']=self.ui.lbMachineLeader.text()
        print(self.ui.lbWorkSeq.text())
        print(self.cartInfo['currentEquipment'])

        if len(self.listROI_fileName)==0:
            QMessageBox.information(self, "错误", "注意，未选择废票信息截图，不能上传废票信息！，")
            return
        if self.ui.txtDescribe.toPlainText()=="":
            QMessageBox.information(self, "错误", "请输入说明信息！，")
            return
        for i in range(len(self.listROI_fileName)):
            imgfile=self.listROI_fileName[i]   #无法确定是否批量的，先测试传第一个图像
            fileName = (imgfile)[imgfile.rfind('\\') + 1:]  #解析出img name
            imgInfo['filename']=fileName
            imgInfo['fullpath']=imgfile+'.jpg'
            imgInfo['info']=""
            print("上传废票信息说明：",listformatPosInfo[i]['remark'])
            params['format_pos']=listformatPosInfo[i]['format_pos']
            params['remark']=listformatPosInfo[i]['remark']
            imgSaveUrl= self.uploadImgToQualitySys(imgInfo,self.uploadUrl)
            if  imgSaveUrl is not None:
                params['url']=imgSaveUrl   #图像上传保存地址
            else:
                QMessageBox.information(self, "错误", "质量信息系统接口异常，无法上传图像数据，" +self.uploadUrl)
                return
            if self.uplaodImgParamToQualitySys(params,self.uploadParamUrl)==200:    #上传废票信息到质量系统
                uploadOk=True
            else:
                uploadOk=False
                QMessageBox.information(self, "错误", "废票数据未传递到质量信息系统")
                return
        if uploadOk:
            QMessageBox.information(self, "信息", "废票数据传递到质量信息系统成功，")
        self.listROI_fileName=[]
        del listformatPosInfo
        self.ui.txtDescribe.clear()
        self.ui.lsImgROIWidget.clear()
        # self.ui.lbMachineLeader.clear()
        # self.ui.lbWorkSeq.clear()

    def getWholeCartNo(self):
        '''
        connect the whole 8 bits cartNo
        :return: whole 8bits cartNo
        '''
        wholeCartNo=self.ui.comYear.currentText()+self.ui.editProductType.text()+\
                    self.ui.editFlag.text()+self.ui.editProductID.text()
        return wholeCartNo

    def uploadImgToQualitySys(self,imgInfo,uploadUrl):
        '''
        将图片文件上传质量信息系统接口
        :param imgfile:dict类型 {“filename”：“fullpath”：“info”}
        :param uploadUrl: 质量信息系统API接口
        :return: 成功，True
        '''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
            # 'Content-type':'multipart/form-data',
            'X-Requested-With': 'XMLHttpRequest'}

        imgData = {'file': (imgInfo['filename'], open(imgInfo['fullpath'], 'rb'), 'image/jpeg'), 'info': imgInfo['info']}
        imgData_encoder = MultipartEncoder(imgData)
        headers['Content-type'] = imgData_encoder.content_type
        # data = {'compress': '200'}  可以不用request_toolbelt库以及Content-type,而使用下面一行代码
        # r = requests.post(post_url, headers=headers, files=imgData_encoder,data=data)
        try:
            res = requests.post(uploadUrl, headers=headers, data=imgData_encoder)
            res.raise_for_status() #判断网络连接状态，错误就抛出异常
        except requests.exceptions.ConnectionError as e:
            QMessageBox.information(self,"错误","质量信息系统接口异常，无法上传图像，"+str(e))
            raise e
        resInfo = res.json()
         
        if resInfo['msg']=="上传成功" and resInfo['url'] !='':
            return resInfo['url']
        else :
            return None

    def uplaodImgParamToQualitySys(self,params,uploadParamUrl):
        '''
        上传图像参数数据到质量平台
        :param params: 图像参数（车号、开位、工序、设备、机长、描述、图片地址）
        :param uploadParamUrl:质量参数写入接口
        :return:res.status_code 200
        '''
        headers = {'Content-type': 'application/json'}
        try:
            res=requests.post(uploadParamUrl,headers=headers,json=params)
        except requests.exceptions.ConnectionError as e:
            QMessageBox.information(self, "错误", "质量信息系统接口异常，无法上传废票信息数据，" + str(e))
            raise e
        # resInfo = res.json()
        return res.status_code

    @pyqtSlot()
    def on_txtDescribe_textChanged(self):
        '''
        限制说明文本框字数不能超过最大值（数据库该字段为255字符，对应汉字127个。）
        :return:
        '''
        txt=(self.ui.txtDescribe.toPlainText())
        txtlength=len(txt)
        maxlen=120
        if txtlength>maxlen:
            cursor = self.ui.txtDescribe.textCursor()
            # 设置文本框的值
            self.ui.txtDescribe.setPlainText(txt[0:maxlen])
            # 设置文本框光标的位置
            cursor.setPosition(maxlen, cursor.MoveAnchor)
            # 设置光标
            self.ui.txtDescribe.setTextCursor(cursor)
            QMessageBox.information(self, "错误", " 字数太多了，达到最大值了！")

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
        self.paramSetupWin.rebootSignal.connect(self.rebootApp)
        self.paramSetupWin.show()

    @pyqtSlot()
    def on_btnCameraProp_clicked(self):
        '''
        弹出摄像头参数设置窗口
        :return:
        '''
        # self.cap.set(cv2.CAP_PROP_SETTINGS, 0) #弹出opencv自带的设置摄像头参数的窗口
        cameraPropDlg = CameraPropSetupDlg(self.cap)
        cameraPropDlg.exec_()

    def getScreenRect(self):
        desktop = QApplication.desktop()
        # 获取显示器分辨率大小
        screenRect = desktop.screenGeometry()
        height = screenRect.height()
        width =  screenRect.width()
        return width,height

    def rebootApp(self):
        print("reboot.......")
        # python = sys.executable
        # print(python)
        # os.execl(python,python,   *sys.argv)
        QApplication.quit()
        status = QProcess.startDetached(sys.executable, sys.argv)
        print(status)

    @pyqtSlot()
    def on_btnCounterRot_clicked(self):
        '''
        图像反时针旋转90度
        :return:
        '''
        currentImgIdx = self.ui.lsImgROIWidget.currentIndex().row()
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

    # app=QApplication(sys.argv)
    # mainWin=MainWindow()
    #
    # mainWin.show()
    #
    # sys.exit(app.exec_())
    current_exit_code = 2023
    params={}                  # ROI info ，包含车号、机长、开位、工序、设备名称、说明信息
    formatPosInfo = {}         # each k info，includ k-pos,remark
    listformatPosInfo=[]       # k list
    while current_exit_code == 2023:
        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec_())


