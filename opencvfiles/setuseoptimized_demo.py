# -*- coding: utf-8 -*-
"""

11.2 OpenCV 中的默认优化
    查看优化是否开启
        cv2.useOptimized()
    开启优化
        cv2.setUseOptimized()

蒋小军
2018.7.7
"""


import cv2
import numpy as np
import os

print(cv2.useOptimized())

img1 = cv2.imread(r'C:\Users\Public\Pictures\Sample Pictures\lina.jpg')

e1 = cv2.getTickCount()

# your code execution.
for i in range(5,9,2):
    img1 = cv2.medianBlur(img1,i)
    cv2.imshow('lina',img1)
    #os.system("Pause")
    cv2.waitKey(20)
    cv2.destroyAllWindows()

e2 = cv2.getTickCount()     
time = (e2- e1)/cv2.getTickFrequency()
print('time%s'%time)

cv2.setUseOptimized(False)
print(cv2.useOptimized())

e1 = cv2.getTickCount()

# your code execution.
for i in range(5,9,2):
    img1 = cv2.medianBlur(img1,i)
    cv2.imshow('lina',img1)
    #os.system("Pause")
    cv2.waitKey(20)
    cv2.destroyAllWindows()

e2 = cv2.getTickCount()     
time = (e2- e1)/cv2.getTickFrequency()
print('time%s'%time)


os.system("Pause")
