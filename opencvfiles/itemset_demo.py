# -*- coding: utf-8 -*-
"""
9.1 获取并修改像素值
    img.item(10,10,2)
        第一、第二个参数：图像的高度与宽度对应的像素位置
        第三个参数：RGB颜色通道下标值。0 -> R , 1 -> G , 2 -> B

    img.itemset((10,10,2),100)
        第一个参数：图像的高度与宽度对应的像素位置和RGB颜色通道下标值。0 -> R , 1 -> G , 2 -> B
        第二个参数：RGB颜色设置值

    警告：Numpy 是经过优化了的进行快速矩阵运算的软件包。所以我们不推荐
    逐个获取像素值并修改，这样会很慢，能有矩阵运算就不要用循环。

    注意：上面提到的方法被用来选取矩阵的一个区域，比如说前5 行的后3
    列。对于获取每一个像素值，也许使用Numpy 的array.item() 和array.
    itemset() 会更好。但是返回值是标量。如果你想获得所有B，G，R 的
    值，你需要使用array.item() 分割他们。

9.2 获取图像属性
    h,w,c = img.shape()
        返回值：行，列，通道
    img.size()
        返回值：图像尺寸。 行*列*通道数
    img.dtype()
        返回值：图像的数据类型

9.3 图像ROI
    roi = img[280:340,330:390]
    img[273:333,100,160] = roi

9.4 拆分及合并图像通道
    b,g,r = cv2.split(img)
    img = cv2.merge(b,g,r)
    或者 b = img[:,:,0]

    警告：cv2.split() 是一个比较耗时的操作。只有真正需要时才用它，能用
    Numpy 索引就尽量用。

蒋小军
2018.7.5
"""
import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Public\Pictures\Sample Pictures\lina.jpg')
px = img[100,100]
print("px:")
print(px)
blue = img[100,100,0]
print("blue:")
print(blue)
img[100,100] = [255,255,255]
print(img[100,100])
print("item:")
print(img.item(10,10,2))
img.itemset((10,10,2),100)
print("itemset:")
print(img.item(10,10,2))
print("img.shape:")
print(img.shape)

print("img.size:")
print(img.size)

print("img.dtype:")
print(img.dtype)

ball=img[280:340,330:390]
img[273:333,100:160]=ball
cv2.imshow('roi',img)
b,g,r=cv2.split(img)
img=cv2.merge((g,b,r))
cv2.imshow("gbr",img)
b=img[:,:,0]
img[:,:,2] = 0
cv2.imshow('gb0',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
