# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:58:16 2020

@author: logam
"""


import matplotlib.pyplot as plt
import numpy as np 
import cv2

img = cv2.imread('test3.jpg')
plt.figure(dpi=300)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


hist, bins = np.histogram(img.flatten(), 256,[0,256])

equ = cv2.equalizeHist(img)

plt.hist(img.flatten(),256,[0,256], color="r")

#pls.imshow()

plt.subplot(121),plt.hist(img.flatten(),256,[0,256], color="r"),plt.title('Histogramm')

plt.subplot(122),plt.imshow(img, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
