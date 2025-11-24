#Q.1. Write a python program to implement k-nearest Neighbors ML algorithm to build 
#prediction model (Use iris Dataset). 

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target

df = pd.DataFrame(X, columns=iris.feature_names)
print(df)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("✅ Model Accuracy:", accuracy_score(y_test, y_pred))


#Q.2. Fit the simple linear regression and polynomial linear regression models to  
#Salary_positions.csv data. Find which one is more accurately fitting to the given    
#data. Also predict the salaries of level 11 and level 12 employees. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("Salary_positions.csv")
print("Dataset:\n", df)

X = df[['Level']]
y = df['Salary']

lin_reg = LinearRegression()
lin_reg.fit(X, y)

poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)

levels = np.array([[11], [12]])
lin_pred = lin_reg.predict(levels)
poly_pred = poly_reg.predict(poly.transform(levels))

print("Level 11 → Linear:", lin_pred[0])
print("Level 11 → Polynomial:", poly_pred[0])
print("Level 12 → Linear:", lin_pred[1])
print("Level 12 → Polynomial:", poly_pred[1])

plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, lin_reg.predict(X), color='red', label='Linear Regression')
plt.plot(X, poly_reg.predict(X_poly), color='green', label='Polynomial Regression')
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Linear vs Polynomial Regression")
plt.legend()
plt.show()

print("\nConclusion: Polynomial Regression fits the data more accurately.")
