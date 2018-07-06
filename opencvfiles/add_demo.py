# -*- coding: utf-8 -*-
"""
10.1 图像加法
    cv2.add(x,y)

    注意：OpenCV 中的加法与Numpy 的加法是有所不同的。OpenCV 的加法
    是一种饱和操作，而Numpy 的加法是一种模操作。

10.2 图像混合
    g(x) = (1 -a) * f0(x) + a * f1(x)
    cv2.addWeighted(img1,0.7,img2,0.3,0)
        参数1：欲混合图像1
        参数2：欲混合图像1的所占百分比
        参数3：欲混合图像2
        参数4：欲混合图像2的所占百分比
        参数5：偏置值γ
        返回值：dst = α * img1 + β * img2 + γ

蒋小军
2018.7.5
"""


import cv2
import numpy as np


x = np.uint8([250])
y = np.uint8([10])
print("cv2.add(x,y):")
print(cv2.add(x,y)) # 250 + 10 = 260 => 255

print('numpy . + ')
print(x + y) # 250 + 10 =260 % 256 = 4

# 两幅图像需要有同样的shape
img1 = cv2.imread(r'C:\Users\Public\Pictures\Sample Pictures\78.jpg')
img2 = cv2.imread(r'C:\Users\Public\Pictures\Sample Pictures\77.jpg')

dst = cv2.addWeighted(img1,0.2,img2,0.8,0)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindow()
