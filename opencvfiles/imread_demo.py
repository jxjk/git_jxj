# -*- coding: utf-8 -*-
"""
读取图片
    cv2.imread('messi5.jpg',0)
        第一个参数：图片路径
        第二个参数：
            cv2.IMREAD_COLOR -> 读入一副彩色图像。图像透明度会被忽略，这是默认参数。
            cv2.IMREAD_GRAYSCALE:以灰度模式读入图像。
            cv2.IMREAD_UNCHANGED:读入一副图像，并且包括图像的alpha通道。

    警告：就算图像的路径是错的，OpenCV也不会提醒你的，但是当你使用命令print(img)时得到的结果是None。

显示图像
    cv2.imshow('imgWindowName',img)
        第一个参数：图像窗口的名字
        第二个参数：要显示的图像

键盘等待
    cv2.waitKey(0)
        第一个参数：等待键盘输入时间，毫秒级的。如果设为‘0’，则无限期的等待键盘输入。
        返回值：当按下任意键，返回按键的ASCII码。如果没有输入返回值为-1.
        
删除显示窗口
    cv2.destroyAllWindows('imgWindowName')
        第一个参数：输入你想要删除的窗口名字。无输入，则删除所有窗口。

蒋小军
2018.7.4
"""


import cv2
import numpy as np


img = cv2.imread(r'C:\Users\Public\Pictures\Sample Pictures\lina.jpg',0)

cv2.imshow('lina',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
