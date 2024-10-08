# -*- coding: utf-8 -*-
"""7- Random Forest Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ak0_gTECDGr6olVNoJehoNMin8JM6FTK
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1: -1].values
Y = dataset.iloc[:, -1].values
print(X)
print(Y)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X, Y)

regressor.predict([[6.5]])

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, Y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title("Random forest classification")
plt.xlabel("Position")
plt.ylabel("Salaries")
plt.show()