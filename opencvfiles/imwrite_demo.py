# -*- coding: utf-8 -*-
"""
保存图片
    cv2.imwrite('messi5.jpg',img)
        第一个参数：图片路径
        第二个参数：图像

蒋小军
2018.7.4
"""


import cv2
import numpy as np


img = cv2.imread(r'C:\Users\Public\Pictures\Sample Pictures\lina.jpg',cv2.IMREAD_UNCHANGED)

cv2.imshow('lina',img)
cv2.imwrite(r'C:\Users\Public\Pictures\Sample Pictures\linacopy.png',img)
cv2.waitKey(0)
cv2.destroyAllW.jpgindows()
