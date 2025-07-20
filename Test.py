import os
import numpy as np
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

c = np.array([10, 20, 50, 80, 100, 150, 200])
f = np.array([3.94, 7.87, 19.69, 31.50, 39.37, 59.06, 78.74])
#f = np.array([50, 68, 122, 176, 212, 302, 392])

# Create a sequential neural network model with a single dense layer.
# The dense layer has 1 unit (output neuron) and 1 input feature.
# The activation function is linear, meaning the output is the same as the input.
model = keras.Sequential([Dense(units=1, input_shape=(1,), activation='linear')])

# Loss is the difference between the predicted and actual values.
# Adam is an optimizer that adjusts the learning rate based on the gradient of the loss function.
model.compile(loss='mean_squared_error', optimizer=Adam(0.1))

# Epochs is the number of times the model will see the data.
# Verbose is the level of output. -1 means no output.
model.fit(c, f, epochs=800, verbose = -1)

# Predict the Fahrenheit temperature for a Celsius temperature of 300.
print(model.predict(np.array([300])))

print(model.get_weights())
