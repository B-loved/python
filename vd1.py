## Bài tập 1. Sử dụng python và thư viện OpenCV.
## Đọc ảnh traffic.jpg vào biến bộ nhớ.
##Hiển thi kích thước ảnh, số kênh
## Hiển thị từng kênh ảnh


import cv2
import numpy

I=cv2.imread('D:/NhapMonXuLyAnh/img/Traffic.jpg')
cv2.imshow('anh',I)
print('size anh',I.shape)
print('so dong',I.shape[0])
print('so cot',I.shape[1])
print('anh la ma tran ',len(I.shape),' chieu')

#kenh B
IB=I[:,:,0]
cv2.imshow('kenh B',IB)
IG=I[:,:,1]
cv2.imshow('kenh G',IG)
IR=I[:,:,2]
cv2.imshow('kenh R',IR)

##############################################
cv2.waitKey()