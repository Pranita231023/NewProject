#Q.1. Write a python program to implement Multiple Linear Regression for Fuel Consumption dataset.                                                                                                                      

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

data = {
    'Engine_Size': [1.0, 1.3, 1.5, 1.8, 2.0, 2.4, 3.0, 3.2, 3.5, 4.0],
    'Cylinders': [4, 4, 4, 4, 4, 6, 6, 6, 6, 8],
    'Horsepower': [68, 102, 120, 132, 140, 160, 200, 210, 250, 300],
    'Fuel_Consumption': [6.5, 7.0, 7.2, 8.0, 8.5, 9.0, 10.0, 10.5, 11.0, 12.0]
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df)

X = df[['Engine_Size', 'Cylinders', 'Horsepower']]
y = df['Fuel_Consumption']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("\nPrediction Results:\n", results)

print("\nModel Performance:")
print("R² Score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))




#Q.2. Write a python program to implement k-nearest Neighbors ML algorithm to build 
#prediction model (Use iris Dataset) 

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
