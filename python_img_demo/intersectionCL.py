# -*- coding: utf-8 -*-
"""
求圆与直线的交点
蒋小军
2018.6.26
"""
import cv2
import numpy as np


def bresenhamCircle(xc=0,yc=0,r=1):
    x = 0
    y = r
    d = 3 - 2 * r
    points = [] 
    while x< y:
        points.append([xc+x,yc-y])
        points.append([xc+y,yc-x])
        points.append([xc+y,yc+x])
        points.append([xc+x,yc+y])
        points.append([xc-x,yc+y])
        points.append([xc-y,yc+x])
        points.append([xc-y,yc-x])
        points.append([xc-x,yc-y])
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x -y) + 10
            y -= 1
        x += 1
    return points


def o_bresenhamLine(x1=0,y1=0,x2=1,y2=1):
    dx = x2 - x1
    dy = y2 - y1
    k = dy / dx
    e = 0.5 
    x = x1 
    y = y1
    points = [] 
    for x in range(x1,x2,1):
        points.append([x,y])
        e = e + k
        if e > 0 :
            y += 1
            e -= 1
    k = (y2-y1) / (x2-x1)
    b = y1 - k * x1
    return points ,k ,b


def bresenhamLine(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    ux = ((dx > 0) << 1) - 1 # x的增量方向，取或-1
    uy = ((dy > 0) << 1) - 1 # y的增量方向，取或-1
    x = x1
    y = y1
    eps = 0 #eps为累加误差
    dx = abs(dx)
    dy = abs(dy)
    points = [] 
    if dx > dy:
        for x in range(x1,x2,ux):
            points.append([x,y])
            eps += dy
            if (eps << 1) >= dx:
                y += uy
                eps -= dx
    else:
        for y in range(y1,y2,uy):
            points.append([x,y])
            eps += dx
            if (eps << 1) >= dy:
                x += ux
                eps -= dy 
    k = (y2-y1) / (x2-x1)
    b = y1 - k * x1
    return points ,k ,b
        

def excludepoints(points = [] ):
    ref = []
    for i in range(len(points)):
        exclude = False
        for j in range(len(points)):
            if j > i :
                if abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]) <= 4:
                    exclude = True
                    break
                else:
                    pass
        if exclude == False:
            ref.append(points[i])
    return ref



Xc = 300
Yc = 240
r = 100
C = bresenhamCircle(Xc,Yc,r)
L2,k2,b2 = bresenhamLine(10,100,499,0)
L,k,b = bresenhamLine(0,10,599,479)
# print(L2)
print(k2)
print(b2)
img = np.zeros((480,600,1),np.uint8)
for w,h in C:
    img[h,w] = 255
for w,h in L:
    img[h,w] = 255
for w,h in L2:
    img[h,w] = 255
cv2.imshow("img",img)
Points = []
for x, y in C:
    if abs(k * x + b - y) < 0.8:
        Points.append([x,y])
# print(Points)
ps = excludepoints(Points)
print(ps)
Points_ = []
for x, y in L:
    if abs((x - Xc)**2 + (y - Yc)**2 - r**2 ) < 160:
        Points_.append([x,y])
# print(Points_)
ps = excludepoints(Points_)
print(ps)
Points2 = []
for x, y in L2:
    if abs(k * x + b - y) < 0.8:
        Points2.append([x,y])
# print(Points2)
ps = excludepoints(Points2)
print(ps)

cv2.waitKey(0)
