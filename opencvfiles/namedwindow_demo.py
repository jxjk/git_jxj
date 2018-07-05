# -*- coding: utf-8 -*-
"""
创建窗口
    namedWindow('image',cv2.WINDOW_NORMAL)
        第一个参数：窗口名字
        第二个参数：
            cv2.WINDOW_AUTOSIZE -> 默认设定函数标签
            cv2.WINDOW_NORMAL   -> 可调整窗口大小

        建议：一种特殊的情况是， 你也可以先创建一个窗口， 之后
        再加载图像。这种情况下， 你可以决定窗口是否可以调整
        大小。使用到的函数是cv2.namedWindow()。初始设定函数
        标签是cv2.WINDOW_AUTOSIZE。但是如果你把标签改成
        cv2.WINDOW_NORMAL，你就可以调整窗口大小了。当图像维度太大，
        或者要添加轨迹条时，调整窗口大小将会很有用

蒋小军
2018.7.4
"""


import cv2
import numpy as np


cv2.namedWindow('image',cv2.WINDOW_NORMAL)

img = cv2.imread(r'C:\Users\Public\Pictures\Sample Pictures\lina.jpg',3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
