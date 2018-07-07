# -*- coding: utf-8 -8-
"""
11.1 使用OpenCV 检测程序效率
    cv2.getTickCount()
        返回值：从参考点到这个函数被执行的时钟数。

    cv2.getTickFrequency()
        返回值：返回时钟频率，或者说每秒钟的时钟数。

蒋小军
2018.7.5
"""


import cv2
import numpy as np
import os


e1 = cv2.getTickCount()
# your code execution.
for i in range(10):
    ret = i * i
    print (ret)
e2 = cv2.getTickCount()     
time = (e1 - e2)/cv2.getTickFrequency()
print('time%s'%time)

os.system("Pause")


