# -*- coding: utf-8 -*-
"""
读取视频
    cap = cv2.VideoCapture(0)
        第一个参数：视频路径（包含网络路径）。0、1 通过摄像头捕获视频
        返回值： 类对象实例

    注意：cv2.VideoCapture()是一个类对象
        cap.read() -> 返回一个布尔值。
        cap.isOpened() -> 检测对象是否成功初始化了
        cap.open() -> 如果cap.isOpened()返回值为‘Flase’,则使用该函数。
        cap.get(0) -> 取值范围 0-18 。详细见表格
        cap.set(3,320) -> 参数1 取值范围 0-18 同上。参数2 为 参数1 的值(value)

            • CV_CAP_PROP_POS_MSEC Current position of the video file
            in milliseconds.
            • CV_CAP_PROP_POS_FRAMES 0-based index of the frame to
            be decoded/captured next.
            • CV_CAP_PROP_POS_AVI_RATIO Relative position of the
            video file: 0 - start of the film, 1 - end of the film.
            • CV_CAP_PROP_FRAME_WIDTH Width of the frames in the
            video stream.
            • CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the
            video stream.
            • CV_CAP_PROP_FPS Frame rate.
            • CV_CAP_PROP_FOURCC 4-character code of codec.
            • CV_CAP_PROP_FRAME_COUNT Number of frames in the
            video file.
            • CV_CAP_PROP_FORMAT Format of the Mat objects returned
            by retrieve() .
            • CV_CAP_PROP_MODE Backend-specific value indicating the
            current capture mode.
            • CV_CAP_PROP_BRIGHTNESS Brightness of the image (only
            for cameras).
            • CV_CAP_PROP_CONTRAST Contrast of the image (only for
            cameras).
            • CV_CAP_PROP_SATURATION Saturation of the image (only
            for cameras).
            • CV_CAP_PROP_HUE Hue of the image (only for cameras).
            • CV_CAP_PROP_GAIN Gain of the image (only for cameras).
            • CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
            • CV_CAP_PROP_CONVERT_RGB Boolean flags indicating
            whether images should be converted to RGB.
            • CV_CAP_PROP_WHITE_BALANCE Currently unsupported
            • CV_CAP_PROP_RECTIFICATION Rectification flag for stereo
            cameras (note: only supported by DC1394 v 2.x backend currently)
    注意：你应该确保你已经装了合适版本的ffmpeg 或者gstreamer。如果你装
    错了那就比较头疼了。

蒋小军
.7.4
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
