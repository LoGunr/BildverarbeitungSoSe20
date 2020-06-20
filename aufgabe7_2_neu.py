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
c_point = None
last_point = None
chain = []
processed = []

def check_neighbours(cur_point):
    for entry in  kf.get_eight_neighbours_ext(cur_point[0], cur_point[1], (dims[1],dims[0])):
        if img[entry[0]]!=255:
            if not entry[0] in processed:
               return entry
                
while(c_point != sp):
    if c_point == None:
        c_point = sp
    
    out = check_neighbours(c_point)
    c_point = out[0]
    num = out[1]
    chain.append(num)
    processed.append(c_point)
    
print(chain)
plt.imshow(img)