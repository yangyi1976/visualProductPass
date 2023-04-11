import cv2
import numpy as np

# Read image
image = cv2.imread(r"F:\PycharmProjects\pp_ocr_py34\img\capture_img 3386.jpg")

# Select ROI
r = cv2.selectROI("select the area", image,True,False) #r(startX,startY,width,height)
print(r)
# Crop image
cropped_image = image[int(r[1]):int(r[1] + r[3]),  #source_image[ start_row:end_row, start_col:end_col]
                int(r[0]):int(r[0] + r[2])]

# Display cropped image
cv2.imshow("Croppedimage1", cropped_image)
cv2.waitKey(0)