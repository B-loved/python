## Bài 2. Viết chương trình đọc vào ảnh traffic.jpg và chuyển đổi ảnh:
##2.a. sang ảnh grayscale 256 mức xám, được ma trận ảnh Igray và hiển thị lên màn hình ảnh Igray.
## 2.b. chuyển đổi ảnh Igray sang ảnh nhị phân với ngưỡng quyết định nhị phân 120 được ma trận ảnh Ib.
## Hiển thị ảnh Ib.(ảnh traffic.jpg ở bài 1)


import cv2
import numpy as np

I = cv2.imread('D:/NhapMonXuLyAnh/img/Traffic.jpg')
cv2.imshow('anh', I)

# 2a
print('chuyen anh sang grayscale bang cach tu code')
so_dong = I.shape[0]
so_cot = I.shape[1]

Igray = np.zeros((so_dong, so_cot), dtype='uint8')

for i in range(so_dong):
    for j in range(so_cot):
        # gray=0.39*r+0.50*g+0.11*b
        d = 39 * int(I[i][j][2]) + 50 * int(I[i][j][1]) + 11 * int(I[i][j][0])
        d = d // 100
        Igray[i][j] = d

cv2.imshow('anh gray', Igray)
cv2.waitKey()
##############################################
cv2.waitKey()