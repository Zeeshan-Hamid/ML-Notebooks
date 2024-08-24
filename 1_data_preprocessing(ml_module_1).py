# -*- coding: utf-8 -*-
"""1- data_preprocessing(ML module_1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n2udrnlxZQrCEHUekiYtEb8G3QA_6vbf

# Data Preprocessing Tools

## Importing the Libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data (1).csv')
X = dataset.iloc[: , : -1].values
Y = dataset.iloc[:, -1].values

print(f"THe dependent dataset is \n {X}")
print(f"The independant dataset is \n {Y}")

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

print(X)

import csv

with open('new_data.csv', 'w', newline='') as csvFile:
  csvWriter = csv.writer(csvFile)
  csvWriter.writerows(X)

"""## Encoding the independent variable"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

import pprint
pprint.pprint(X)
print(X)

"""## Encoding the dependant variable"""

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
Y = le.fit_transform(Y)
print(Y)

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=1)

print(X_train)

print(X_test)

print(Y_train)

print(Y_test)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X[:, 3:] = sc.fit_transform(X[:, 3:])

print(X)

X_test[:, 3:] = sc.fit_transform(X_test[:, 3:])

print(X_test)