
# -*- coding: utf-8 -*-
"""
保存视频
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
        第一个参数：视频保存路径
        第二个参数：FourCC 编码，详细见下方
        第三个参数：播放频率
        第四个参数：帧的大小
        第五个参数：isColor标签。如果是True，每帧就是彩色图，否则就是灰度图。

        返回值： 类对象实例

    注意：cv2.VideoWriter()是一个类对象
    FourCC 就是一个4 字节码，用来确定视频的编码格式。可用的编码列表
    可以从fourcc.org查到。这是平台依赖的。下面这些编码器对我来说是有用个。
        • In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is
        more preferable. MJPG results in high size video. X264 gives
        very small size video)
        • In Windows: DIVX (More to be tested and added)
        • In OSX : (I don’t have access to OSX. Can some one fill this?)
    FourCC 码以下面的格式传给程序，以MJPG 为例：
        cv2.cv.FOURCC('M','J','P','G') 或者cv2.cv.FOURCC(*'MJPG')。
        
    下面的代码是从摄像头中捕获视频，沿水平方向旋转每一帧并保存它。    

蒋小军
2018.7.4
"""


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
