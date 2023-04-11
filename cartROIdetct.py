import cv2 as cv
import numpy as np

class CartROIdetector(object ):

    def getCartROIimg(self,src_image):
        '''
        # 将车号文本区域图像提取出
        :param src_image:
        :return:
        '''
        # src_image=cv.imread(r'F:\PycharmProjects\pp_ocr_py34\img\274.jpg')
        deliate_img = self.preProcessImg(src_image) #图片预处理，二值化+膨胀
        x,y,w,h=self.Extract(deliate_img)
        #提却ROI区域图像
        cut_img = src_image[y - 3:y + h + 10, x - 3:x + w + 10]
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
        contours, hierarchy = cv.findContours(op_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        # 绘制矩形包围框，得到轮廓的坐标
        max_x, max_y, max_w, max_h = cv.boundingRect(contours[0])
        for c in contours:
            x, y, w, h = cv.boundingRect(c)
            #高/宽之比
            occupy = float(h) / w
            # 7<=比值<=11，可以配置成参数
            if occupy >= 7.0 and occupy <= 12:
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
        img_src = cv.cvtColor(img_src, cv.COLOR_BGR2GRAY)
        # img_src = cv.equalizeHist(img_src)
        # cv.imshow('Original GRAY image', img_src)
        # cv.waitKey(0)
        # 将图像转化成标准大小
        # img_src = cv.resize(img_src, (1200, 1800))
        cv.imshow('original image', img_src)
        cv.waitKey(0)
        # 图像二值化
        # ret, binary_img = cv.threshold(img_src, 150, 255, cv.THRESH_BINARY_INV  )
        ret, binary_img = cv.threshold(img_src, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
        # cv.imshow('Binary image', binary_img)
        # cv.waitKey(0)

        # 膨胀卷积核 RECTANGULAR
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 5))
        dilate = cv.dilate(binary_img, kernel, iterations=5)

        cv.imshow('Eroded image', dilate)
        cv.waitKey(0)
        return dilate


