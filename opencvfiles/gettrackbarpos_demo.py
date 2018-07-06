# -*- coding:utf-8 -*-
"""
创建鼠标事件的回调函数
    cv2.setMouseCallback(windowName, onMouse[, param]) 
        第一个参数：表示将要操作的面板名，
        第二个参数：回调函数名，
        第三个参数：给回调函数的参数。如果要给回调函数传递多个参数的话，则将这么多个参数存入一个
                    列表/元组中，将其传入
                    回调函数，共有5个参数：
                        第一个参数；鼠标事件名
                            EVENT_FLAG_ALTKEY　　 EVENT_FLAG_CTRLKEY
                            EVENT_FLAG_LBUTTON　　EVENT_FLAG_MBUTTON
                            EVENT_FLAG_RBUTTON　　EVENT_FLAG_SHIFTKEY
                            EVENT_LBUTTONDBLCLK　 EVENT_LBUTTONDOWN
                            EVENT_LBUTTONUP　　   EVENT_MBUTTONDBLCLK
                            EVENT_MBUTTONDOWN　　 EVENT_MBUTTONUP
                            EVENT_MOUSEMOVE    　 EVENT_RBUTTONDBLCLK
                            EVENT_RBUTTONDOWN     EVENT_RBUTTONUP
                        第二个，第三个参数：鼠标在面板中的坐标
                        第四个参数：有没有其他特殊控制，比如在按左键的时候，按了Ctrl，Shift，Alt
                                    键等，参数也是刚刚上面的EVENT列表中的，通过事件名可以找到对应
                                    flags
                        第五个参数；setMouseCallback()函数给回调函数传递的参数。(代码中，a没有用，
                                    只是为了演示如何给回调函数传递函数用的)

滑动条绑定到OpenCV 的窗口
    cv2.createTrackbar(trackbarName, windowName, value, count, onChange)
        第一个参数：滑动条的名字，
        第二个参数：滑动条被放置窗口的名字，
        第三个参数：滑动条的默认位置。
        第四个参数：滑动条的最大值，
        第五个函数：回调函数，每次滑动条的滑动都会调用回调函数。回调函数通常都会含有一个默认参数，
                    就是滑动条的位置。

    最后用这两个函数做了下面一个简单的绘图程序：

    每次获取当前的色彩，鼠标按下后开始绘图，鼠标移动到哪，则画到哪，默认是绘制从起始点到终点的矩形，
    如果按了'm'键，则切换绘制以起始点和终点为直径的圆，圆心在两点的中心，如果再按'm'键，则切换会矩
    形。(由于本人对Python的变量作用域这块理解还不是很到位，因此用了很多全局变量，写的不好，请大家多
    多见谅)

    引用：https://www.cnblogs.com/pakfahome/p/3913559.html

蒋小军
2018.7.5
"""


import cv2
import numpy as np
import math
import copy as cp


drawing = False
mode = True
ix,iy = -1,-1
pre_img = np.zeros((512,512,3), np.uint8)
img = np.zeros((512,512,3), np.uint8)


def nothing(x):
    pass


def draw_circle(event, x, y, flags, param):
    print (type(param[0]), param[1])
    pa,pb = param[1]
    global ix,iy,drawing,mode,pre_img,img
    
    # 每次获取当前Trackbar的位置
    r = cv2.getTrackbarPos('R', 'hello') * pa
    g = cv2.getTrackbarPos('G', 'hello') * pb
    b = cv2.getTrackbarPos('B', 'hello') 
    colors=(b,g,r)    
   
    print (colors )
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = cp.deepcopy(pre_img)
            if mode == True:
                cv2.rectangle(img, (ix,iy), (x,y), colors, -1)
            else:
                length = int(math.sqrt((ix-x)**2+(iy-y)**2)/2)
                center = (int(float(ix+x)/2), int(float(iy+y)/2))
                cv2.circle(img, center, length, colors, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix,iy), (x,y), colors,-1)
        else:
            length = int(math.sqrt((ix-x)**2+(iy-y)**2)/2)
            center = (int(float(ix+x)/2), int(float(iy+y)/2))
            cv2.circle(img, center, length, colors, -1)
        pre_img=img
   
   
a = [1,1.2]
# 创建面板       
cv2.namedWindow('hello')

# 在面板'hello'上，创建3个trackbar，分别命名为R,G,B,回调函数都是啥都不做
cv2.createTrackbar('R', 'hello', 0,255, nothing)
cv2.createTrackbar('G', 'hello', 0,255, nothing)
cv2.createTrackbar('B', 'hello', 0,255, nothing)

# 创建鼠标事件的回调函数
cv2.setMouseCallback('hello', draw_circle,[img,a])

while(1):
    cv2.imshow('hello',img)
    k = cv2.waitKey(1) & 0xFF
    # 每次按'm'键都会切换状态，当m=True时，绘制矩形，m=False,绘制圆
    if k == ord('m'):
        mode = not mode
        
    # 如果按了'ESC'键，则关闭面板
    elif k == 27:
        break
    
cv2.destroyAllWindows()
