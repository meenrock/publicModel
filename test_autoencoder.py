import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf

conv_2D = tf.keras.layers.Conv2D
dense = tf.keras.layers.Dense
max_pooling_2D = tf.keras.layers.MaxPooling2D
up_sampling_2D = tf.keras.layers.UpSampling2D

from keras import Input, Model
from keras.datasets import mnist

encoding_dimension = 15
input_img = Input(shape=784)

encoded = dense(encoding_dimension, activation='relu')(input_img)

decoded = dense(784, activation='sigmoid')(encoded)

autoencoder = Model(input_img, decoded)

encoder = Model(input_img, encoded)

