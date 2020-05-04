6# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import matplotlib.pyplot as plt
import numpy as np 

img = plt.imread("test.png")

fig, axs = plt.subplots(4,2, figsize=(15,15))

### a
rgb_weights = [1.0, 1.0, 1.0]
coloredImage = np.dot(img[...,:3], rgb_weights)
axs[0,0].imshow(img, origin="upper")
axs[0,0].title('Original')

rgb_weights = [1.0, 0.0, 0.0]
redImage = np.dot(img[...,:3], rgb_weights)
axs[0,1].imshow(redImage, origin="upper", cmap = "Reds")
plt.title('Red')

rgb_weights = [0.0, 1.0, 0.0]
greenImage = np.dot(img[...,:3], rgb_weights)
axs[1,0].imshow(greenImage, origin="upper", cmap = "Greens")
plt.title('Green')

rgb_weights = [0.0, 0.0, 1.0]
blueImage = np.dot(img[...,:3], rgb_weights)
axs[1,1].imshow(blueImage, origin="upper", cmap = "Blues")
plt.title('Blue')



### b
cyanImage = np.full((1024,1024), np.subtract(redImage, coloredImage))
axs[2,0].imshow(cyanImage, origin="upper", cmap = "gray")
plt.title('Cyan')


magentaImage = np.full((1024,1024), np.subtract(blueImage, coloredImage))
axs[2,1].imshow(magentaImage, origin="upper", cmap = "gray")
plt.title('Magenta')


yellowImage = np.full((1024,1024), np.subtract(greenImage, coloredImage))
axs[3,0].imshow(yellowImage, origin="upper", cmap = "gray")
plt.title('Yellow')




plt.show()
#plt.imshow(grayscale_image, cmap = plt.get_cmap("gray"))