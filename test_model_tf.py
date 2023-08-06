import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf 
from tensorflow import keras
from tensorflow.python.keras import layers, Sequential

mnist = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_Test = x_train / 255.0, x_test / 255.0

model = keras.models.Sequential()
model.add(keras.Input(shape=(28, 28)))
model.add(layers.SimpleRNN(128, activation='relu'))
model.add(layers.Dense(10))
print(model.summary())

import sys; sys.exit()


loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = keras.optimizers.Adam(lr=0.001)
metrics = tf.keras.metrics.FalsePositives(thresholds=None, name=None, dtype=None)
metrics += ["accuracy"]

model.compile(Loss=loss, optimizer=optimizer, metrics=metrics)

# loss and optimizer
