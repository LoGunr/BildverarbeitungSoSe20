# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:20:59 2020

@author: logam
"""
import numpy as np
import scipy.stats as st
import cv2
from scipy import ndimage
import sys

def calc_kernel(img, size, nsig):
    
    #erstellt vektor von -nsig bis +nsig mit size+1 schritten
    # Bsp -3, 3, 5: [-3.  -1.8 -0.6  0.6  1.8  3. ]
    x = np.linspace(-nsig, nsig, size+1)
    #print(x)
    
    #Bestimmt dichte 
    #[0.0013499  0.03593032 0.27425312 0.72574688 0.96406968 0.9986501 ]
    x = st.norm.cdf(x)
    #print(x)
    
    #np diff: rekursiv: out[i] = a[i+1] - a[i] 
    #[0.03458042 0.2383228  0.45149376 0.2383228  0.03458042]
    kern1d = np.diff(x)
    
    #sprint(kern1d)
    
    # to 2D
    kern2d = np.outer(kern1d, kern1d)
    #normalize
    kern2d = kern2d/kern2d.sum()
   
    return cv2.filter2D(img,-1,kern2d)


def laplace_kernel(img):
    
    kern2d = np.array([[0,  1,  0],[1, -4,  1],[0,  1,  0]])
    #kern2d = np.outer(x, x)
    #print(kern2d)

    #return normalized
    return cv2.filter2D(img,-1,kern2d)

def sobel_kernel(img):  
    filtered_x = sobel_horizontal(img) 
    filtered_y = sobel_vertical(img)
    
    filtered_result, theta = edge_gradient(filtered_x, filtered_y)
    return (filtered_result, theta)


def edge_gradient(filtered_x, filtered_y):
     #filtered_result = (abs(filtered_x) + abs(filtered_y))/2
    filtered_result = np.sqrt(np.square(filtered_x, dtype = np.dtype(np.float32)) + np.square(filtered_y, dtype = np.dtype(np.float32)))

    filtered_result = np.sqrt(np.square(filtered_x, dtype = np.dtype(np.float32)) + np.square(filtered_y, dtype = np.dtype(np.float32)))
    #print(filtered_result)
    filtered_result *= 255.0 / filtered_result.max()
    
    theta = np.arctan2(filtered_y, filtered_x)
    
    angle = theta * 180. / np.pi
    angle[angle < 0] += 180
    
    #print(angle)
      
    return (filtered_result, angle)

def sobel_horizontal(img):
    kern2d_x = np.array([[1, 0, -1],[2, 0,  -2],[1,  0,  -1]], np.float32)/8
    return cv2.filter2D(img,-1,kern2d_x)
 
def sobel_vertical(img):
    kern2d_y = np.array([[1, 2,  1],[0, 0,  0],[-1, -2, -1]],  np.float32)/8
    return cv2.filter2D(img,-1,kern2d_y)
 
def non_max_sup(img, angle):
    X, Y = img.shape
    filtered_image = np.zeros((X,Y), dtype=np.int32)
    for i in range(1,X-1):
        for j in range(1,Y-1):
            try:
                q = 255
                r = 255
                
                if (0 <= angle[i,j] < 22.5):
                    q = img[i, j+1]
                    r = img[i, j-1]
                elif(157.5 <= angle[i,j] <= 180):
                    q = img[i, j+1]
                    r = img[i, j-1]      
                elif (22.5 <= angle[i,j] < 67.5):
                    q = img[i+1, j-1]
                    r = img[i-1, j+1]
    
                elif (67.5 <= angle[i,j] < 112.5):
                    q = img[i+1, j]
                    r = img[i-1, j]
    
                elif (112.5 <= angle[i,j] < 157.5):
                    q = img[i-1, j-1]
                    r = img[i+1, j+1]
    
                if (img[i,j] >= q) and (img[i,j] >= r):
                    filtered_image[i,j] = img[i,j]
                else:
                    filtered_image[i,j] = 0
            except IndexError as e:
                pass
    return filtered_image
   
def canny_kernel(img):
    gaussfiltered = calc_kernel(img, 5, 3)
    sobel_filtered, angle = sobel_kernel(gaussfiltered)
    return non_max_sup(sobel_filtered, angle)

def LoG(img):
    kern_laplace = np.array([[0,  1,  0],[1, -4,  1],[0,  1,  0]])
    kern_gauss =   np.array([[1,  2,  1],[2,  4,  2],[1,  2,  1]])
    print(np.matmul(kern_laplace, kern_gauss))
    #log_filter = kern_laplace.dot(kern_gauss)
    log_filter = np.array([[0,1,2,1,0],[1,0,-2,0,1],[2,-2,-8,-2,2],[1,0,-2,0,1],[0,1,2,1,0]])/16
    return cv2.filter2D(img,-1,log_filter)

def DoG(img):
    
    #log_filter = kern_laplace.dot(kern_gauss)
    dog_filter = np.array([[1,4,6,4,1],[4,0,-8,0,4],[6,-8,-28,-8,6],[4,0,-8,0,4],[1,4,6,4,1]])
    return cv2.filter2D(img,-1,dog_filter)

def jacobian_filter(img, num_dir):
    X, Y = img.shape
    result_img = np.zeros((X,Y))
    
    for i in range(1,X-1):
        for j in range(1,Y-1):
            try:
                cur = img[i, j]
                
                up_dif   =  img[i, j+1] - cur
                #down_dif =  img[i, j-1] - cur 
                #left_dif =  img[i-1, j] - cur
                right_dif = img[i+1, j] - cur
                jacobian_xy = np.array([[up_dif,0],[0,right_dif]])
                
                ew, ev = np.linalg.eig(jacobian_xy)
                det = np.linalg.det(ev)
                if(det == num_dir):
                    result_img[i,j] = 255#img[i, j]
            except IndexError as e:
                pass
    return result_img

def create_jacobian(img):           
    f_vert = sobel_vertical(img)
    f_horiz = sobel_horizontal(img)
    
    jac_11 = np.square(f_vert)
    jac_12_21 = np.multiply(f_vert, f_horiz)
    jac_22 = np.square(f_horiz)
    
    
def test():
    sys.setrecursionlimit(100000)
    print(sys.getrecursionlimit())
    
                
def get_eight_neighbours(x, y, shape):
    out = []
    maxx = shape[1]-1
    maxy = shape[0]-1

    #top left
    outx = min(max(x-1,0),maxx)
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #top center
    outx = x
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #top right
    outx = min(max(x+1,0),maxx)
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #left
    outx = min(max(x-1,0),maxx)
    outy = y
    out.append((outx,outy))

    #right
    outx = min(max(x+1,0),maxx)
    outy = y
    out.append((outx,outy))

    #bottom left
    outx = min(max(x-1,0),maxx)
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    #bottom center
    outx = x
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    #bottom right
    outx = min(max(x+1,0),maxx)
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    return out

def get_four_neighbours(x, y, shape):
    # resulting neighbours
    out_pix = []
    #alwas check if we`re close to border
    border_x = shape[1]-1
    border_y = shape[0]-1
    
    #right
    outx = min(max(x+1,0),border_x)
    outy = y
    out_pix.append((outx,outy))

    #top
    outx = x
    outy = min(max(y-1,0),border_y)
    out_pix.append((outx,outy))
    
    #left
    outx = min(max(x-1,0),border_x)
    outy = y
    out_pix.append((outx,outy))

    #bottom
    outx = x
    outy = min(max(y+1,0),border_y)
    out_pix.append((outx,outy))
    
    return out_pix


def get_four_neighbours_ext(x, y, shape):
    # resulting neighbours
    out_pix = []
    #alwas check if we`re close to border
    border_x = shape[1]-1
    border_y = shape[0]-1
    
    #right
    outx = min(max(x+1,0),border_x)
    outy = y
    out_pix.append(((outx,outy),0))

    #top
    outx = x
    outy = min(max(y-1,0),border_y)
    out_pix.append(((outx,outy),1))
    
    #left
    outx = min(max(x-1,0),border_x)
    outy = y
    out_pix.append(((outx,outy),2))

    #bottom
    outx = x
    outy = min(max(y+1,0),border_y)
    out_pix.append(((outx,outy),3))
    
    return out_pix
    

def get_eight_neighbours_ext(x, y, shape):
    out = []
    maxx = shape[1]-1
    maxy = shape[0]-1

    #right
    outx = x
    outy = min(max(y+1,0),maxy)
    out.append(((outx,outy),0))

    
    #top right
    outx = min(max(x-1,0),maxx)
    outy = min(max(y+1,0),maxy)
    out.append(((outx,outy),1))
    
    #top
    outx = min(max(x-1,0),maxx)
    outy = y
    out.append(((outx,outy),2))
    
    #top left
    outx = min(max(x-1,0),maxx)
    outy = min(max(y-1,0),maxy)
    out.append(((outx,outy),3))

    #left
    outx = x
    outy = min(max(y-1,0),maxy)
    out.append(((outx,outy),4))
    
    #bottom left
    outx = min(max(x+1,0),maxx)
    outy = min(max(y-1,0),maxy)
    out.append(((outx,outy),5))
    
    #bottom
    outx = min(max(x+1,0),maxx)
    outy = y
    out.append(((outx,outy),6))
    
    #botom right
    outx = min(max(x+1,0),maxx)
    outy = min(max(y+1,0),maxy)
    out.append(((outx,outy),7))    
    
    return out
    