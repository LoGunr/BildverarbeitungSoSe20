# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:41:12 2020

@author: logun
"""


import tensorflow as tf
from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np 
import wandb
from wandb.keras import WandbCallback

# logging code
run = wandb.init()
config = run.config

# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

one = np.array(X_test[2], dtype='float')
one = one.reshape((28, 28))


two = np.array(X_test[1], dtype='float')
two = two.reshape((28, 28))


seven = np.array(X_test[0], dtype='float')
seven = seven.reshape((28, 28))





#axs[0,0].imshow(y_test[0], origin="upper", cmap = plt.get_cmap("gray"))