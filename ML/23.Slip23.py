#Q.1. Fit the simple linear regression and polynomial linear regression models to 
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

print("\nPredicted Salaries:")
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


#Q.2. Write a python program to find all null values from a dataset and remove them.

import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, None, 30, 28, 22],
    'City': ['Pune', 'Mumbai', None, 'Delhi', 'Chennai']
}
df = pd.DataFrame(data)
print("Original Dataset:\n", df)

print("\nNull Values in Each Column:\n", df.isnull().sum())

df_clean = df.dropna()
print("\nDataset After Removing Null Values:\n", df_clean)
