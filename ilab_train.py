from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
import numpy
from termcolor import cprint
from keras.layers import Dense
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn import preprocessing
import seaborn as sns
import re
import numpy as np
import pandas as pd
from keras.layers.merge import Concatenate
from keras.layers import Input
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from keras.layers.embeddings import Embedding
from keras.models import Model
from keras.layers import GlobalMaxPooling1D
from keras.layers import Flatten, LSTM
from keras.layers.core import Activation, Dropout, Dense
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import one_hot
from numpy import array
import os
import scipy
import torch
import tensorflow as tf

dataframe = pd.read_csv("/term-deposit-marketing-2020.csv")

y = dataframe['y'].map({'yes': 1, 'no': 0})
dataframe.drop(["y"], axis=1, inplace=True)
dataframe.head()
y.head()

X = pd.get_dummies(dataframe[["job", "marital", "education",
                              "default", "housing", "loan", "contact", "month"]])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42)

scaler = StandardScaler()

scaler.fit(X_train)
x_train_scaled = scaler.transform(X_train)

scaler.fit(X_test)
x_test_scaled = scaler.transform(X_test)

mlp_model = MLPClassifier(solver="adam").fit(x_train_scaled, y_train)

y_pred = mlp_model.predict(x_test_scaled)

accuracy_score(y_test, y_pred)

mlp_params = {"alpha": [1, 2, 3, 4, 5, 0.1, 0.01, 0.03, 0.005, 0.0001],
              "hidden_layer_sizes": [(10, 10), (3, 5), (100, 100), (100, 100, 100)]}

mlp_cv_model = GridSearchCV(
    mlp_model, mlp_params, cv=5, verbose=2, n_jobs=-1).fit(x_train_scaled, y_train)

mlp_tuned = MLPClassifier(alpha=0.0001, hidden_layer_sizes=(
    3, 5), solver="adam", activation="logistic").fit(x_train_scaled, y_train)

y_pred = mlp_tuned.predict(x_test_scaled)
accuracy_score(y_test, y_pred)
