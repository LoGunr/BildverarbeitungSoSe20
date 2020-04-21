# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import matplotlib.pyplot as plt
import numpy as np 
import cv2

img = cv2.imread('test.png')
plt.figure(dpi=200)
kernel = np.ones((5,5),np.float32)/25

central_value = 130.0

kernel2 = np.ones((5,5),np.float32)

kernel2[2][2] = central_value

kernel2 /= 24.0 + central_value

print(kernel2)
#The higher the central_value, the less is the

dst = cv2.filter2D(img,-1,kernel)
dst2 = cv2.filter2D(img,-1,kernel2)

plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(dst2),plt.title('High Center')
plt.xticks([]), plt.yticks([])
plt.show()