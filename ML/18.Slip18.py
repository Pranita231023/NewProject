#Q.1. Write a python program to implement k-means algorithm on a Diabetes dataset.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.cluster import KMeans

diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
print("Diabetes Dataset\n",df)

X = df[['bmi', 'bp']]

kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)
print("\nClustered Data:",df)

plt.scatter(df['bmi'], df['bp'], c=df['Cluster'])
plt.xlabel("BMI")
plt.ylabel("Blood Pressure")
plt.title("K-Means Clustering on Diabetes Dataset")
plt.show()


#Q.2. Write a python program to implement Polynomial Linear Regression for  
salary_positions dataset.         

# Polynomial Linear Regression for Salary Positions Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

data = {
    'Level': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary': [15000, 20000, 30000, 35000, 40000, 45000, 50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
print("Original Dataset:\n", df)

X = df[['Level']]
y = df['Salary']

poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)

plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Polynomial Regression (degree=4)')
plt.xlabel("Position Level")
plt.ylabel("Salary (₹)")
plt.title("Polynomial Linear Regression: Salary Prediction")
plt.legend()
plt.show()
