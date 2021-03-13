import numpy as np
import keras
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense 
from data import X_train, y_train


def create_model():
    model = Sequential()

    model.add(Dense(units = 17, kernel_initializer = 'uniform', activation = 'relu', input_dim = 27))

    model.add(Dense(units = 17, kernel_initializer = 'uniform', activation = 'relu'))
    model.add(Dense(units = 17, kernel_initializer = 'uniform', activation = 'relu'))

    model.add(Dense(units = 7, kernel_initializer = 'uniform', activation = 'softmax'))

    return model


model = create_model()
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
model.fit(X_train, y_train, batch_size = 5, epochs = 500)

model.save('./models/model-area.hdf5')