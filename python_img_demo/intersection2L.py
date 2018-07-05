# -*- coding: utf-8 -*-
"""
求两直线的交点
蒋小军
2018.6.27
"""
import cv2
import numpy as np 


Line1 = input("Frist Line(x0,y0,x1,y1)")
Line2 = input("Second Line(x0,y0,x1,y1)")

L1 = Line1.split(',')
L2 = Line2.split(',')

print(L1)
print(L2)
L1x0,L1y0,L1x1,L1y1 = L1
L2x0,L2y0,L2x1,L2y1 = L2

L1x0 = float(L1x0)
L1y0 = float(L1y0)
L1x1 = float(L1x1)
L1y1 = float(L1y1)
L2x0 = float(L2x0)
L2y0 = float(L2y0)
L2x1 = float(L2x1)
L2y1 = float(L2y1)

a = []
b = []
c = []

a.append(L1y0 - L1y1)
b.append(L1x1 - L1x0)
c.append(L1x0 * L1y1 - L1x1 * L1y0)
a.append(L2y0 - L2y1)
b.append(L2x1 - L2x0)
c.append(L2x0 * L2y1 - L2x1 * L2y0)

D = a[0] * b[1] - a[1] * b[0]

if D != 0:
    x =(b[0] * c[1] - b[1] * c[0]) / D
    y =(a[1] * c[0] - a[0] * c[1]) / D
    print("%.3f%8.3f"%(x,y))
else:
    print('coincidence lines 两直线重合！')
