import cv2 as cv
import shelve
import numpy as np
class CartROIdetector(object ):
    def getCartROIimg(self,src_image):
        '''
        # 将车号文本区域图像提取出
        :param src_image:
        :return:
        '''
        shelf = shelve.open('cfg')
        self.kernelWidth=shelf['kernelWidth']
        self.kernelHeight=shelf['kernelHeight']
        self.occpuyMin=shelf['ocuppyMin']
        self.occpuyMax=shelf['ocuppyMax']
        # src_image=cv.imread(r'F:\PycharmProjects\pp_ocr_py34\img\274.jpg')
        deliate_img = self.preProcessImg(src_image) #图片预处理，二值化+膨胀
        x,y,w,h=self.Extract(deliate_img)
        x = x - 50
        y = y - 50
        w = w + 100
        h = h + 100
        img1=cv.rectangle(src_image,(x,y),(x+w,y+h),(0,0,255))
        cv.imshow('Original GRAY image', img1)
        #提取 ROI区域图像
        cut_img = src_image[y :y + h , x :x + w ]
        if w<h:
            cut_img = np.rot90(cut_img, 1)
        # cv.imshow('Enlarged original image', cut_img)
        # cv.waitKey(0)
        return cut_img


    def getCartNumRect(self, src_image):
        '''
        获取车号矩形坐标与长短
        :param src_image:
        :return:
        '''
        deliate_img = self.preProcessImg(src_image)
        x, y, w, h = self.Extract(deliate_img)

        return x, y, w, h

    def Extract(self,op_image):
        '''
        传入膨胀处理过的图片
        :param op_image:
        :return:
        '''
        img,contours, hierarchy = cv.findContours(op_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        # 绘制矩形包围框，得到轮廓的坐标
        max_x, max_y, max_w, max_h = cv.boundingRect(contours[0])
        for c in contours:
            x, y, w, h = cv.boundingRect(c)
            #高/宽之比
            occupy = float(h) / w
            # 7<=比值<=11，可以配置成参数
            print(occupy)
            if occupy >= int(self.occpuyMin) and occupy <= int(self.occpuyMax):
                s = cv.contourArea(c) #计算区域的面积

                if max_w < w:      #宽大于最大值，更换面积s
                    max_x = x
                    max_y = y
                    max_w = w
                    max_h = h
                    s = cv.contourArea(c)
                    continue
        return max_x,max_y,max_w,max_h

    def preProcessImg(self,img_src):
        '''
        图片预处理，膨胀与腐蚀
        :return:
        '''

        #转换为灰度图像
        img_src1 = cv.cvtColor(img_src, cv.COLOR_BGR2GRAY)
        # img_src1 = cv.equalizeHist(img_src1) #直方图均衡

        img_src=cv.blur(img_src1,(3,3)) #均值滤波
        # img_src=cv.GaussianBlur(img_src1,(3,3),0,0)
        # img_src = cv.bilateralFilter(img_src1, 5, 150, 150)
        cv.imshow('Original Filter image', img_src)
        cv.waitKey(0)
        # 将图像转化成标准大小
        h,w=img_src.shape[:2]
        # if w>=1920:
        #     img_src = cv.resize(img_src, (1280, 720))
        # cv.imshow('resize image', img_src)
        # cv.waitKey(0)
        # 图像二值化
        # ret, binary_img = cv.threshold(img_src, 150 , 255, cv.THRESH_BINARY_INV  )
        ret, binary_img = cv.threshold(img_src, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
        cv.imshow('Binary image', binary_img)
        # cv.waitKey(0)

        # 膨胀卷积核 RECTANGULAR

        kernel = cv.getStructuringElement(cv.MORPH_RECT, (int(self.kernelWidth), int(self.kernelHeight)))
        dilate = cv.dilate(binary_img, kernel, iterations=6)

        cv.imshow('Eroded image', dilate)
        cv.waitKey(0)
        return dilate


