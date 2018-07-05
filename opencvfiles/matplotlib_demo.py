
# -*- coding: utf-8 -*-
"""
使用Matplotlib
    Matplotib 是python 的一个绘图库，里头有各种各样的绘图方法。之后
会陆续了解到。现在，你可以学习怎样用Matplotib 显示图像。你可以放大图
像，保存它等等。

蒋小军
2018.7.4
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread(r'C:\Users\Public\Pictures\Sample Pictures\lina.jpg',0)
plt.imshow(img,cmap = 'gray',interpolation = 'bicubic')
plt.xticks([]),plt.yticks([]) # To hide tick values on X and Y axis.
plt.show()

