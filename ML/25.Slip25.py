#Q.1. Write a python program to implement Polynomial Regression for house price dataset.  

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

data = {
    'Area': [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000],
    'Price': [75000, 85000, 95000, 110000, 130000, 150000, 165000, 185000, 210000, 230000]
}
df = pd.DataFrame(data)
print("Original Dataset:\n", df)

X = df[['Area']]
y = df['Price']

poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)

new_area = np.array([[3200], [3500]])
new_area_poly = poly.transform(new_area)
pred = model.predict(new_area_poly)
print(f"\nPredicted Price for 3200 sq.ft: ₹{pred[0]:,.2f}")
print(f"Predicted Price for 3500 sq.ft: ₹{pred[1]:,.2f}")

plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Polynomial Regression (degree=3)')
plt.xlabel("House Area (sq.ft)")
plt.ylabel("House Price (₹)")
plt.title("Polynomial Regression: House Price Prediction")
plt.legend()
plt.show()



#Q.2. Create a two layered neural network with relu and sigmoid activation function. 

import numpy as np
X = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
y = np.array([[0],[1],[1],[0]])

np.random.seed(0)
W1 = np.random.randn(3,4)
W2 = np.random.randn(4,1)


relu = lambda x: np.maximum(0,x)
sigmoid = lambda x: 1/(1+np.exp(-x))


for i in range(10000):
    # Forward pass
    A1 = relu(np.dot(X,W1))
    A2 = sigmoid(np.dot(A1,W2))
    
   
    A2_error = y - A2
    A2_delta = A2_error * (A2*(1-A2))
    A1_error = A2_delta.dot(W2.T)
    A1_delta = A1_error * (A1>0)
    
    W2 += A1.T.dot(A2_delta) * 0.1
    W1 += X.T.dot(A1_delta) * 0.1

print("Final Output:\n", A2.round(3))

