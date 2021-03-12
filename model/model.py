import numpy as np
import keras
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential #For Initializing ANN
from tensorflow.keras.layers import Dense #For Layers of ANN
from data import X_train, y_train
# Initializing the ANN with sequence of layers (Could use a Graph)
#Classifier Model


model = Sequential()
# Adding the input layer and the first hidden layer
model.add(Dense(units = 17, kernel_initializer = 'uniform', activation = 'relu', input_dim = 27))
# Adding the hidden layers
model.add(Dense(units = 17, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dense(units = 17, kernel_initializer = 'uniform', activation = 'relu'))
# Adding the output layer
# Probability for the outcome 
model.add(Dense(units = 7, kernel_initializer = 'uniform', activation = 'softmax'))
# Compiling the ANN
'''Classification'''
#Another Option: categorical_crossentropy
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
model.fit(X_train, y_train, batch_size = 5, epochs = 500)
