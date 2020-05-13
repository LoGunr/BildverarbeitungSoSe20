# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:10:03 2020

@author: logam
"""


import matplotlib.pyplot as plt
import numpy as np 
import kernel_function as kf
import cv2



#img = cv2.imread('rotation1.jpg')
img = cv2.imread('grayscale.png', cv2.IMREAD_GRAYSCALE)
plt.figure(dpi=300)
#img = np.float32(img)


#The higher the central_value, the less is the blur
gaussfiltered0 = kf.calc_kernel(img, 20, 4)
#einfachster, super anfällig für noise

plt.imshow(gaussfiltered0, cmap = plt.get_cmap("gray"))    