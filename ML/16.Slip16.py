#Q.1. Create a two layered neural network with relu and sigmoid activation function. 

import numpy as np

X = np.array([[0,0,1],
              [1,1,1],
              [1,0,1],
              [0,1,1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

np.random.seed(0)
W1 = np.random.randn(3,4)
W2 = np.random.randn(4,1)

relu = lambda x: np.maximum(0, x)
sigmoid = lambda x: 1 / (1 + np.exp(-x))

for i in range(10000):
    # Forward pass
    A1 = relu(np.dot(X, W1))
    A2 = sigmoid(np.dot(A1, W2))

   
    A2_error = y - A2
    A2_delta = A2_error * (A2 * (1 - A2))   # andsigmoid derivative

    A1_error = A2_delta.dot(W2.T)
    A1_delta = A1_error * (A1 > 0)          # relu derivative

   
    W2 += A1.T.dot(A2_delta) * 0.1
    W1 += X.T.dot(A1_delta) * 0.1

print("Final Output:\n", A2.round(3))



#Q.2. Write a python program to implement Simple Linear Regression for Boston housing 
dataset.    

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("boston_houses.csv")   

print('Original dataset\n',df)

print("\nNull values in each column:\n", df.isnull().sum())
df = df.dropna()
print("\nDataset after removing null values:\n", df)

X = df[['RM']]         # Independent variable
y = df['Price']         # Dependent variable (house price)

model = LinearRegression()
model.fit(X,y)

df['Predicted_Price'] = model.predict(X)
print("\nPredicted Prices:\n", df)

plt.scatter(df['RM'], df['Price'], color='blue', label='Actual Price')
plt.plot(df['RM'], df['Predicted_Price'], color='red', label='Predicted Price')
plt.xlabel("RM")
plt.ylabel("Price")
plt.title("Simple Linear Regression: House Price Prediction")
plt.legend()
plt.show()
