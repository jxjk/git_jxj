# -*- coding: utf-8 -*-
"""
查询cv2中是否包含‘EVENT’属性

蒋小军
2018.7.3
"""
import cv2
import os


events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

os.system("pause")

