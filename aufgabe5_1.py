# -*- coding: utf-8 -*-
"""
Created on Mon May 25 13:25:00 2020

@author: logam
"""

from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np 
import kernel_function as kf
import cv2
import random

original = cv2.imread('test2.png')#
img = cv2.imread('test2.png', cv2.IMREAD_GRAYSCALE)#
plt.figure(dpi=700)

#kf.test()

canny = cv2.Canny(img,50,250)
dims = canny.shape
#result_pic = np.zeros_like(img)
result_pic = 0 * np.ones((dims[0],dims[1],3), np.uint8)

def edge_seg(row_cur, col_cur, row_start, col_start, color):
    #set pixel in current picture black so it wont be used again
    canny[row_cur, col_cur] = 0
    result_pic[row_cur,col_cur] = color
      

    for coord in kf.get_eight_neighbours(row_cur, col_cur, dims):
        #pass, if we got to the start again (break?!)
        if (coord[0] == row_start and coord[1] == col_start):
            break
        elif (canny[coord[0]][[coord[1]]] == 255):
            edge_seg(coord[0], coord[1], row_start, col_start, color)
        else:
            pass
"""

def edge_seg(row_cur, col_cur, row_start, col_start, color):
    #set pixel in current picture black so it wont be used again
    canny[row_cur, col_cur] = 0
    start = True
    while ((row_cur != row_start and col_cur != col_start) or start == True):
        for coord in kf.get_eight_neighbours(row_cur, col_cur, dims):
            if (canny[coord[0]][[coord[1]]] == 255):
                canny[coord[0]][[coord[1]]] = 0
                result_pic[row_cur, col_cur] = color
                row_cur = coord[0]
                col_cur = coord[1]
                
        cv2.imshow("progress",result_pic)
        cv2.waitKey(1)        
                
        start = False
""" 
      
def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)



for row in range (dims[0]):
    for col in range (dims[1]):
        cur_val = canny[row][col]
        if cur_val == 255:
            #print(cur_val)
            #whiteFrame[row,col] = (225, 50, 90)
            edge_seg(row, col, row, col, random_color())
            

result_pic2 = ndimage.binary_fill_holes(result_pic[:,:,0]).astype(int)


plt.subplot(231),plt.imshow(original),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(result_pic),plt.title('Connected Edges')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(result_pic2, cmap = plt.get_cmap("gray")),plt.title('Filled Regions')
plt.xticks([]), plt.yticks([])




        
    
    