# -*- coding: utf-8 -*-
"""
鼠标事件回调函数
    cv2.setMouseCallback('image',draw_circle)
    第一个参数：回调窗口
    第二个参数：回调函数

    注意：回调函数第一个参数必须为‘event’

双击鼠标左键，以鼠标位置为中心，画一个半径为100pixel的蓝色实心圆

蒋小军
2018.7.4
"""

import cv2
import numpy as np


#mouse callback function
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)


# 创建图像与窗口并将窗口与回调函数绑定
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
        break
cv2.destroyAllWindows()
