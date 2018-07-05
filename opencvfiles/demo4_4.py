# -*- coding: utf-8 -*-
"""
4.4 总结一下
    下面的程序将会加载一个灰度图，显示图片，按下’s’键保存后退出，或者
按下ESC 键退出不保存。

警告：如果你用的是64 位系统，你需要将 k = cv2.waitKey(0) 这行改成
k = cv2.waitKey(0)&0xFF。

蒋小军
2018.7.4
"""

import cv2
import numpy as np


img = cv2.imread(r'C:\Users\Public\Pictures\Sample Pictures\lina.jpg',3)
cv2.imshow('lina',img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit.
    cv2.destroyAllWindows()
elif k == ord('s'): # Wait for 's' key to save and exit.
    cv2.imwrite(r'C:\Users\Public\Pictures\Sample Pictures\linacopy.jpg',img)
    cv2.destroyAllWindows()
