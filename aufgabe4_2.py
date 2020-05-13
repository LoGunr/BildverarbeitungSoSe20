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
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


ret, thresh1 = cv2.threshold(img, 30, 90, cv2.THRESH_BINARY)

plt.subplot(121),plt.imshow(img, cmap='gray'),plt.title('Original')

plt.subplot(122),plt.imshow(thresh1, cmap='gray'),plt.title('Threshold')
plt.xticks([]), plt.yticks([])
