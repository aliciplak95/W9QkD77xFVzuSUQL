from pandas import DataFrame
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

df = pd.read_csv("/term-deposit-marketing-2020.csv")

df['y'] = df['y'].map({'yes': 1, 'no': 0})
df.head()

print('No', round(df['y'].value_counts()[0]/len(df) * 100, 2), '% of the data')
print('Yes', round(df['y'].value_counts()[
      1]/len(df) * 100, 2), '% of the data')

len(df["y"])
ages = []

for i in range(0, 40000):
    if df["y"][i] == 1:
        ages.append((df["age"][i]))

ages = DataFrame(ages, columns=['Ages'])

ages.head()

len(ages)


plt.figure(figsize=(24, 8))
sns.set(style="darkgrid")
ax = sns.countplot(x="Ages", data=ages)

marital = []

for i in range(0, 40000):
    if df["y"][i] == 1:
        marital.append((df["marital"][i]))

maritals = DataFrame(marital, columns=['Marital'])

maritals.head()
len(maritals)


plt.figure(figsize=(24, 8))
sns.set(style="darkgrid")
ax = sns.countplot(x="Marital", data=maritals)

education = []

for i in range(0, 40000):
    if df["y"][i] == 1:
        education.append((df["education"][i]))

educations = DataFrame(education, columns=['Education'])

educations.head()

plt.figure(figsize=(24, 8))
sns.set(style="darkgrid")
ax = sns.countplot(x="Education", data=educations)

job = []

for i in range(0, 40000):
    if df["y"][i] == 1:
        job.append((df["job"][i]))

jobs = DataFrame(job, columns=['Job'])

jobs.head()

plt.figure(figsize=(24, 8))
sns.set(style="darkgrid")
ax = sns.countplot(x="Job", data=jobs)

housing = []

for i in range(0, 40000):
    if df["y"][i] == 1:
        housing.append((df["housing"][i]))

housings = DataFrame(housing, columns=['housing'])

housings.head()

plt.figure(figsize=(24, 8))
sns.set(style="darkgrid")
ax = sns.countplot(x="housing", data=housings)

duration = []

for i in range(0, 40000):
    if df["y"][i] == 1:
        duration.append((df["duration"][i]))

durations = DataFrame(duration, columns=['duration'])

durations.head()

plt.figure(figsize=(24, 8))
sns.set(style="darkgrid")
#ax = sns.countplot(x="duration", data=durations)
ax = sns.displot(data=durations, x="duration", kde=True)

default = []

for i in range(0, 40000):
    if df["y"][i] == 1:
        default.append((df["default"][i]))

defaults = DataFrame(default, columns=['default'])

defaults.head()

plt.figure(figsize=(24, 8))
sns.set(style="darkgrid")
#ax = sns.displot(data=defaults, x="default", kde=True)
ax = sns.countplot(x="default", data=defaults)

balance = []

for i in range(0, 40000):
    if df["y"][i] == 1:
        balance.append((df["balance"][i]))

balances = DataFrame(balance, columns=['balance'])

balances.head()

plt.figure(figsize=(24, 8))
sns.set(style="darkgrid")
ax = sns.displot(data=balances, x="balance", kde=True)

loan = []

for i in range(0, 40000):
    if df["y"][i] == 1:
        loan.append((df["loan"][i]))

loans = DataFrame(loan, columns=['loan'])

loans.head()

plt.figure(figsize=(24, 8))
sns.set(style="darkgrid")
ax = sns.countplot(x="loan", data=loans)

campaign = []

for i in range(0, 40000):
    if df["y"][i] == 1:
        campaign.append((df["campaign"][i]))

campaigns = DataFrame(campaign, columns=['campaign'])

campaigns.head()

plt.figure(figsize=(24, 8))
sns.set(style="darkgrid")
ax = sns.countplot(x="campaign", data=campaigns)
