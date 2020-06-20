# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:43:49 2020

@author: logun
"""
import matplotlib.pyplot as plt
import cv2


img = cv2.imread('binary_small.png', cv2.IMREAD_GRAYSCALE)
plt.figure(dpi=700)
dims = img.shape

M_0_0 = 0
M_1_0 = 0
M_0_1 = 0

for row in range (dims[0]):
    for col in range (dims[1]):
        M_0_0 += img[row][col]
        M_1_0 += row * img[row][col]
        M_0_1 += col * img[row][col]
        
x_strich = M_1_0 / M_0_0
y_strich = M_0_1 / M_0_0

#return central moment pq
def cm(p,q):
    mü_p_q = 0
    for row in range (dims[0]):
        for col in range (dims[1]):
            mü_p_q += ((row - x_strich) ** p) * ((col - y_strich)**q) * img[row][col]
    return mü_p_q

#return pq as string for labeling the plot
def pq_str(p,q):
    return(str(p)+","+str(q))

#calcs scale invariants
def scale_inv(mü_p_q, mü_0_0, p, q):
    return(mü_p_q/mü_0_0**(1+(p+q)/2))
           

steps=[0,1,2,5]
müs = []
mü_strich =[]
müs_divided =[]
labels = []

for p in steps:
    for q in steps:
        cur = cm(p,q)
        müs.append(cur)
        labels.append(pq_str(p,q))
        if(p+q>=2):
            mü_strich.append(scale_inv(cur,müs[0],p,q))
        elif(p==0 and q==0):
            mü_strich.append(1)
        else:
            mü_strich.append(0)

mü_strich_2_0 = scale_inv(cm(2,0),müs[0],2,0)  
mü_strich_0_2 = scale_inv(cm(0,2),müs[0],0,2)  
mü_strich_1_1 = scale_inv(cm(1,1),müs[0],1,1)  
quadr_2_0_0_2 = (mü_strich_2_0-mü_strich_0_2)**2
    
ellipse_exz = (quadr_2_0_0_2 - 4*mü_strich_1_1)/quadr_2_0_0_2


print(ellipse_exz)
#plt.plot(['0,0', '0,1', '0,2'], [1, 2, 3])
#plt.plot(labels, müs_divided)