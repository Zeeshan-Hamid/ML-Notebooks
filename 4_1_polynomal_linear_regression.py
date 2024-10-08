# -*- coding: utf-8 -*-
"""4.1- Polynomal Linear Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uu2hHI-xyicPXhCRGtrQFzh-HOm4jGIp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('complex_polynomial_dataset.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

print(X)
print(Y)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state = 42)

print(X_train)
print(X_test)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train, Y_train)

print(lin_reg.predict(X_test))

print(X.shape)
print(Y.shape)

plt.scatter(X_train[:, 0], Y_train, color='red')  # Plotting the first feature
plt.plot(X_test[:, 0], lin_reg.predict(X_test), color='blue')  # Same feature for prediction
plt.title("Linear Regression")
plt.xlabel('Feature1')
plt.ylabel('Outcome')
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree= 3)
X_poly = poly_reg.fit_transform(X_train)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, Y_train)

# Transform X_test to polynomial features
X_test_poly = poly_reg.transform(X_test)

# Plotting polynomial regression results
plt.scatter(X_train[:, 0], Y_train, color='red')  # Plotting the first feature
plt.plot(X_test[:, 0], lin_reg_2.predict(X_test_poly), color='blue')  # Predicting using polynomial regression
plt.title("Polynomial Regression")
plt.xlabel('Feature1')
plt.ylabel('Outcome')
plt.show()

lin_reg_2.predict(poly_reg.fit_transform([[1.8485445552552704,2.7864646423661146, 8.530094554673601]]))