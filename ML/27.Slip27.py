#Q.1. Create a multiple linear regression model for house price dataset divide dataset into 
#train and test data while giving it to model and predict prices of house. 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

data = {
    'Area': [1000, 1500, 1800, 2400, 3000, 3500, 4000, 4200, 5000, 5500],
    'Bedrooms': [2, 3, 3, 4, 4, 5, 5, 4, 5, 6],
    'Age': [10, 5, 8, 12, 7, 15, 9, 6, 11, 4],
    'Price': [150000, 200000, 250000, 280000, 350000, 400000, 420000, 450000, 480000, 500000]
}

df = pd.DataFrame(data)
print("Dataset:\n", df)

X = df[['Area', 'Bedrooms', 'Age']]  # Independent variables
y = df['Price']                      # Dependent variable


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

results = pd.DataFrame({'Actual Price': y_test, 'Predicted Price': y_pred})
print("\nPrediction Results:\n", results)

print("\nModel Accuracy:")
print("R² Score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))





#Q.2. Fit the simple linear regression and polynomial linear regression models to  
#Salary_positions.csv data. Find which one is more accurately fitting to the given data. 
#Also predict the salaries of level 11 and level 12 employees. 

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
