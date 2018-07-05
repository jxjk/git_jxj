# -*- coding: utf-8 -*-
"""
bresenham画圆法
蒋小军
2018.6.26
"""
import cv2
import numpy as np 


def bresenhamCircle(xc=0,yc=0,r=1):
    x=0
    y=r
    d=3-2*r
    point = set()
    while x < y:
        point.add((xc+x,yc-y))
        point.add((xc+y,yc-x))
        point.add((xc+y,yc+x))
        point.add((xc+x,yc+y))
        point.add((xc-x,yc+y))
        point.add((xc-y,yc+x))
        point.add((xc-y,yc-x))
        point.add((xc-x,yc-y))
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x-y) +10
            y -= 1
        x += 1
    return point

points = bresenhamCircle(300,240,100)
# print(points)
img = np.zeros((480,600,1),np.uint8)
for w,h in points:
    # print(w,h)
    img[h,w] = 255

cv2.imshow('img',img)
cv2.waitKey(0)
