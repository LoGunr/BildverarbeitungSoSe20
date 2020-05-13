# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import matplotlib.pyplot as plt
import numpy as np 
import kernel_function as kf
import cv2



#img = cv2.imread('rotation1.jpg')
img = cv2.imread('grayscale.png', cv2.IMREAD_GRAYSCALE)
#plt.figure(dpi=300)
#img = np.float32(img)


#The higher the central_value, the less is the blur
gaussfiltered0 = kf.calc_kernel(img, 7, 4)
#einfachster, super anfällig für noise
dst1 = kf.laplace_kernel(img)
#einfach berechenbar, noise und feine linien verschlectert
dst2, angle = kf.sobel_kernel(img)
#dst2_1, theta2 = kf.sobel_filters(img)
dst3 = kf.sobel_horizontal(img)
dst4 = kf.sobel_vertical(img)
#beste ergebnisse, edgedirection, noise wird verhindert viel rechenaufwand:
dst5 = kf.canny_kernel(img)
#laplace mit gauß, smoothing
log_filtered = kf.LoG(img)
dog_filtered = kf.DoG(img)

#jacobian_1 = kf.jacobian_filter(img,1)
#jacobian_2 = kf.jacobian_filter(img,2)
"""
plt.subplot(231),plt.imshow(img),plt.title('Original')
#plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(dst1),plt.title('Laplace')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(dst2),plt.title('Sobel')
plt.xticks([]), plt.yticks([])
plt.show()
"""

fig, axs = plt.subplots(6,2, figsize=(15,15))


axs[0,0].imshow(img, origin="upper", cmap = plt.get_cmap("gray"))


axs[0,1].imshow(gaussfiltered0, origin="upper", cmap = plt.get_cmap("gray"))


axs[1,0].imshow(dst1, origin="upper", cmap = plt.get_cmap("gray"))


axs[1,1].imshow(dst2, origin="upper", cmap = plt.get_cmap("gray"))


axs[2,0].imshow(dst3, origin="upper", cmap = plt.get_cmap("gray"))


axs[2,1].imshow(dst4, origin="upper", cmap = plt.get_cmap("gray"))


axs[3,0].imshow(dst5, origin="upper", cmap = plt.get_cmap("gray"))

axs[3,1].imshow(log_filtered, origin="upper", cmap = plt.get_cmap("gray"))

axs[4,0].imshow(dog_filtered, origin="upper", cmap = plt.get_cmap("gray"))

#axs[5,0].imshow(jacobian_1, origin="upper", cmap = plt.get_cmap("gray"))

#axs[5,1].imshow(jacobian_2, origin="upper", cmap = plt.get_cmap("gray"))
