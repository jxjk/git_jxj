# -*- coding: utf-8 -8-
"""
    我们将会用下面的例子演示。下面的例子是用窗口大小不同（5，7，9）的
核函数来做中值滤波：
蒋小军
2018.7.5
"""


import cv2
import numpy as np
import os


img1 = cv2.imread(r'C:\Users\Public\Pictures\Sample Pictures\lina.jpg')
e1 = cv2.getTickCount()

# your code execution.
for i in range(5,9,2):
    img1 = cv2.medianBlur(img1,i)
    cv2.imshow('lina',img1)
    #os.system("Pause")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

e2 = cv2.getTickCount()     
time = (e2- e1)/cv2.getTickFrequency()
print('time%s'%time)


