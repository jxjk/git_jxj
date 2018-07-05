# -*- coding: utf-8 -*-
"""
Canny 边缘检测
蒋小军
"""


import cv2
import numpy as np 
from matplotlib import pyplot as plt


def nothing(x):
    pass


img = cv2.imread(r"C:/users/public/pictures/Sample Pictures/shapessm.jpg")
cv2.namedWindow('edges')
L = 80
H = 200
cv2.createTrackbar('L','edges',0,255,nothing)
cv2.createTrackbar('H','edges',0,800,nothing)

"""
plt .subplot(121)
plt.imshow(img,cmap='gray')
plt.title("Original Image")
plt.xticks([])
plt.yticks([])

plt .subplot(122)
plt.imshow(edges,cmap='gray')
plt.title("Edge Image")
plt.xticks([])
plt.yticks([])

plt.show()
"""
while(1):
    cv2.imshow('image',img)
    edges = cv2.Canny(img,L,H)
    cv2.imshow('edges',edges)
    k = cv2.waitKey(1)&0xFF
    if k == 27:
        break
    L = cv2.getTrackbarPos('L','edges')
    H = cv2.getTrackbarPos('H','edges')
