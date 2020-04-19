6# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import matplotlib.pyplot as plt
import numpy as np 

img = plt.imread("test.png")

rgb_weights = [0.2989, 0.5870, 0.1140]
#plt.imshow(img)

grayscale_image = np.dot(img[...,:3], rgb_weights)
plt.imshow(grayscale_image, cmap = plt.get_cmap("gray"))