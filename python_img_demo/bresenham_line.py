# -*- coding: utf-8 -*-
"""
bresenham画直线
蒋小军
2018.6.26
"""
import cv2
import numpy as np


def bresenhamLine(x0=0,y0=0,x1=1,y1=1):
    # 设置x/y偏移量、设置斜率
    dx = x1-x0
    dy = y1-y0
    k = dy / dx
    e = -0.5
    x = x0
    y = y0
    points = set()
    for x in range (x0,x1,1):
        points.add((x,y))
        e = e + k
        if e > 0:
            y +=1
            e -=1
    return points


points = bresenhamLine(50,50,380,80)
print(points)
img = np.zeros((480,600,1),np.uint8)
for w,h in points:
    img[h,w] = 255

cv2.imshow("img",img)
cv2.waitKey(0)
