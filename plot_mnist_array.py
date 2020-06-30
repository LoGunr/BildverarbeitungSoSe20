# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:41:12 2020

@author: logun
"""

import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D

import tensorflow as tf

import numpy as np 
import wandb
from wandb.keras import WandbCallback

# logging code
run = wandb.init(project="cnn_test")
config = run.config

# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

one = np.array(X_test[2], dtype='float')
one = one.reshape((28, 28))


two = np.array(X_test[1], dtype='float')
two = two.reshape((28, 28))


seven = np.array(X_test[0], dtype='float')
seven = seven.reshape((28, 28))

## reshapes all images to to width = 28, height = 28, 
#adds extra dimension for colour
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
input_shape = (28,28,1)

X_train = X_train.astype("float32")
X_test = X_test.astype("float32")
labels = range(10)

X_train /= 255
X_test /= 255

model = Sequential()

##
model.add(Conv2D(28, kernel_size=(3,3), input_shape = input_shape, activation="relu"))
#model.add(Conv2D(32,
#    (config.first_layer_conv_width, config.first_layer_conv_height),
#    input_shape=input_shape,
#    activation='relu'))


##Pooling: Shrinks Image
model.add(MaxPooling2D(pool_size = (3,3)))
model.add(Flatten())
model.add(Dense(128, activation =tf.nn.relu))
model.add(Dropout(0.2))
#10 is number of outputs
model.add(Dense(10, activation = tf.nn.softmax))

#sparse optional:
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam',
                metrics=['accuracy'])

# Fit the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test),
                    callbacks=[WandbCallback(labels=labels, data_type="image")])

image_index = 4444
plt.imshow(X_test[image_index].reshape(28, 28),cmap = plt.get_cmap("gray"))
pred = model.predict(X_test[image_index].reshape(1, 28, 28 , 1))
print(pred.argmax ())