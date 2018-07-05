# -*- coding: utf-8 -*-
"""
画直线
    cv2.line(img,(0,0),(511,511),(255,0,0),5)
        第一个参数：被操作图像img
        第二个参数：直线起点坐标(0,0)
        第三个参数：直线终点坐标(511,511)
        第四个参数：绘制颜色(G,B,R)
        第五个参数：绘制宽度 5pixel
        第六个参数：线条类型，8连接，抗锯齿cv2.LINE_AA等等。默认情况是8连接。
            cv2.LINE_4,cv2.LINE_8

画矩形
    cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
        第一个参数：被操作图像img
        第二个参数：矩形左上角起点坐标(384,0)
        第三个参数：矩形右下角终点坐标(510,128)
        第四个参数：绘制颜色(G,B,R)
        第五个参数：绘制宽度 3pixel

画圆
    cv2.circle(img,(447,63),63,(0,0,255),-1)
        第一个参数：被操作图像img
        第二个参数：中心坐标(447,63)
        第三个参数：半径大小63
        第四个参数：绘制颜色(G,B,R)
        第五个参数：绘制宽度 整圆填充

画椭圆
    cv2.ellipse(img,(256,256),(100,50),0,0,180,(0,0,255),-1)
        第一个参数：被操作图像img
        第二个参数：中心坐标(256,256)
        第三个参数：长轴和短轴的长度(100,50)
        第四个参数：椭圆沿逆时针方向旋转角度0
        第五个参数：椭圆弧沿顺时针方向起始的角度0
        第六个参数：椭圆弧沿顺时针方向终止的角度360
        第七个参数：绘制颜色(G,B,R)
        第八个参数：绘制宽度 整圆填充

画多边形
    cv2.polylines(img,[Pts],True,(0,255,255),33)
        第一个参数：img:图像,
        第二个参数：顶点集，
        第三个参数：是否闭合，
        第四个参数：颜色，
        第五个参数：线宽度

在图片上添加文字
    cv2.putText(img, ‘HXH’,(50,300),font,4,(255,0,255),2,cv2.LINE_AA)
        第一个参数：图像，
        第二个参数：输入字符串，
        第三个参数：坐标，
        第四个参数：字体，
        第五个参数：字号，
        第六个参数：颜色，
        第七个参数：线宽度，
        第八个参数：线条种类

警告：所有的绘图函数的返回值都是None， 所以不能使用img =
cv2.line(img,(0,0),(511,511),(255,0,0),5)。

蒋小军
2018.7.4
"""


import cv2
import numpy as np

# Create a black imgae.
img = np.zeros((512,512,3),np.uint8)

# Draw a diagonal blue line with thickness of 5 pexil.
cv2.line (img,(0,0),(511,511),(255,0,0),5,cv2.LINE_4)

# Draw a green rectangle with thickness of 3 pexil.
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Draw a red circle with full pexil.
cv2.circle(img,(447,63),63,(0,0,255),-1)

# Draw a ellipse with full pexil.
cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,255,255),-1)

# 画多边形
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
# 这里 reshape 的第一个参数为 -1 ，表明这一维的长度是根据后面的维度计算出来的
print(pts)
cv2.polylines(img,[pts],True,(0,255,255),4)

# 在图片上添加文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,0),2)

winname = 'example'
cv2.namedWindow(winname)
cv2.imshow(winname,img)
cv2.waitKey(0)
cv2.destroyWindow(winname)

