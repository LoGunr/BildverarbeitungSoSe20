
import cv2 as cv
from win32api import GetSystemMetrics
import matplotlib.pyplot as plt
import numpy as np 

#the [x, y] for each right-click event will be stored here
right_clicks = [0, 0]
img = cv.imread("F:/Dokumente/Bildverarbeitung/Bildverarbeitung/grayscale.png", 0)
#img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

plt_img = plt.imread("test.png")


def get_four_neighbours(x, y, shape):
    # resulting neighbours
    out_pix = []
    #alwas check if we`re close to border
    border_x = shape[1]-1
    border_y = shape[0]-1
    
    #left
    outx = min(max(x-1,0),border_x)
    outy = y
    out_pix.append((outx,outy))
    
    #right
    outx = min(max(x+1,0),border_x)
    outy = y
    out_pix.append((outx,outy))

    #top
    outx = x
    outy = min(max(y-1,0),border_y)
    out_pix.append((outx,outy))

    #bottom
    outx = x
    outy = min(max(y+1,0),border_y)
    out_pix.append((outx,outy))
    
    return out_pix
    
    
def region_grow(img, threshold):
    print (right_clicks)

    #create empty image with size of the picture
    dims = img.shape
    orig_size = dims[0]*dims[1]
    result_pic = np.zeros_like(img)

    result_list = []
    processed_pix = []

    #starting with position at mouseclick
    start_pix = right_clicks
    #initializing region mean. Value of start point
    region_mean = float(img[right_clicks[0], right_clicks[1]])

    #append cur_pix to list
    result_list.append(start_pix)

    while(len(result_list) > 0):
        pix = result_list[0]
        #color pixel in result pic like in original
        result_pic[pix[0],pix[1]] = img[pix[0],pix[1]]

        for coord in get_four_neighbours(pix[0], pix[1], dims):
            dist_to_start_pix = abs(int(value_of_start_pix) - int(img[coord[0], coord[1]]))
            print(coord, dist_to_start_pix)
            if ((dist_to_start_pix < threshold)):
                if not coord in processed_pix:
                    result_list.append(coord)    
                processed_pix.append(coord)
        result_list.pop(0)
        cv.imshow("progress",result_pic)
        cv.waitKey(1)
    #direction to be checked from cur_pix
    #neighbour_dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
     
    #cv.Zero(result_pic)
    plt.imshow(result_pic, cmap = plt.get_cmap("gray"))    



#this function will be called whenever the mouse is right-clicked
def mouse_callback(event, x, y, flags, params):

    #right-click event value is 2
    if event == 2:
        global right_clicks

        #store the coordinates of the right-click event
        right_clicks = ([x, y])

        #this just verifies that the mouse data is being collected
        #you probably want to remove this later
       
        region_grow(img, 5)

#path_image = urllib.urlretrieve("http://www.bellazon.com/main/uploads/monthly_06_2013/post-37737-0-06086500-1371727837.jpg", "local-filename.jpg")[0]
scale_width = 640 / img.shape[1]
scale_height = 480 / img.shape[0]
scale = min(scale_width, scale_height)
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.resizeWindow('image', window_width, window_height)

#set mouse callback function for window
cv.setMouseCallback('image', mouse_callback)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()

