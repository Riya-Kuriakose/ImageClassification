# -*- coding: utf-8 -*-
"""CIFAR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QehRDXxVT6YALS3oGY3GJKQS0o6C23BC
"""

# Importing necessary libraries

import tensorflow as tf
from tensorflow.keras import datasets,layers,models
import matplotlib.pyplot as plt
import keras

#Loading the CIFAR-10 dataset

(X_train,Y_train) , ( X_test,Y_test) = datasets.cifar10.load_data()

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)

# Reshaping to 1D array

Y_train = Y_train.reshape(-1,)
Y_train[:5]

classes = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]			

def plot_sample(x,y,index):

    plt.figure(figsize=(15,2))
    plt.imshow(X_train[index])
    plt.xlabel(classes[y[index]])

#Normalizing the data

X_train = X_train/255
X_test = X_test/255

# Creating an artificial neural network

ann = models.Sequential([keras.layers.Flatten(input_shape=(32,32,3)),
                          keras.layers.Dense(3000,activation='relu'),
                          keras.layers.Dense(1000,activation = 'relu'),
                          keras.layers.Dense(10,activation='sigmoid')])
ann.compile(optimizer='SGD',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
ann.fit(X_train,Y_train,epochs=5)
ann.evaluate(X_test,Y_test)

from sklearn.metrics import confusion_matrix,classification_report
import numpy as np
y_pred = ann.predict(X_test)
y_pred_classes = [np.argmax(element) for element in y_pred]
print("Classification Report:\n",classification_report(Y_test,y_pred_classes))

# Using CNN to improve accuracy
	
  cnn = keras.Sequential([keras.layers.Conv2D(filters=32,kernel_size=(3,3),activation='relu',input_shape=(32,32,3)),
                        keras.layers.MaxPool2D((2,2)),

                        keras.layers.Conv2D(filters=32,kernel_size=(3,3),activation='relu',input_shape=(32,32,3)),
                        keras.layers.MaxPool2D((2,2)),

                        keras.layers.Flatten(),
                        keras.layers.Dense(3000,activation='relu'),
                        keras.layers.Dense(10,activation='softmax')])
  
cnn.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
cnn.fit(X_test,Y_test,epochs=10)

