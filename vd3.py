##Cách chuyển đổi  ản RGB sang Grayscale sử dụng OpenCV

import cv2
import numpy as np

I=cv2.imread('D:/NhapMonXuLyAnh/img/Traffic.jpg')
cv2.imshow('anh goc',I)
print('chuyen anh sang grayscale bang cach tu code')
#2a
Ig=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) #I2=cv2.cvtColor(I,cv2.COLOR_BGR2RGB)
cv2.imshow('anh gray su dung OpenCV',Ig)
#2b
nguong=120
Ib=np.zeros((Ig.shape[0],Ig.shape[1]),dtype='uint8')
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        if Ig[i][j] < nguong:
            Ib[i][j]=0#đen tuyệt đối
        else:
            Ib[i][j]=255#trắng tuyệt đối
############################################
sz='anh nhi phan theo nguong ' + str(nguong)
cv2.imshow(sz,Ib)
##############################################
cv2.waitKey()