# -*- coding: utf-8 -*-
"""
橘子与苹果金字塔融合
蒋小军
2018.6.25
"""
import cv2
import numpy as np
import sys


A = cv2.imread('apple.jpg')
B = cv2.imread('orange.jpg')

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B 
G = B.copy()
gpB= [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian pyramid for A 
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    print(i)
    print(GE.shape)
    print(gpA[i-1].shape)
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)

# generate Laplacian pyramid for B 
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

# Now add left and right halves of image in each level
# numpy.hstack(tup)
# Take a sequence of arrays and stack them horizontally
# to make a singe array.
LS = []
for la,lb in zip(lpA,lpB):
    row ,cols ,dpt = la.shape
    print(cols/2)
    ls = np.hstack((la[:,0:int(cols/2)],lb[:,int(cols/2):]))
    LS.append(ls)

# Now reconstruct
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_,LS[i])

# image with direct connecting each half
real = np.hstack((A[:,:int(cols/2)],B[:,int(cols/2):]))

cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)
