# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:47:14 2020

@author: logun
"""


from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np 
import kernel_function as kf
import cv2

img = cv2.imread('ring.png', cv2.IMREAD_GRAYSCALE)
plt.figure(dpi=700)
dims = img.shape

#find start point:
def start_point():
    for row in range (dims[0]):
        for col in range (dims[1]):
            if img[row][col] != 255:
                return row, col
            
sp = start_point()
cur_point = None
last_point = None
chain = []
print(sp)
while (cur_point != sp):
    if cur_point == None: 
        cur_point = sp
    
    for entry in kf.get_four_neighbours_ext(cur_point[0], cur_point[1], dims):
        coord = entry[0]
        num = entry[1]
        if (img[coord[0]][coord[1]] != 255 and coord != last_point):
            chain.append(num)
            last_point = cur_point
            cur_point = coord
            #print(chain)
            break


    
print(chain)
plt.imshow(img)