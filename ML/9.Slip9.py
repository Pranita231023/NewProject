#Q.1. Implement Ridge Regression and Lasso regression model using boston_houses.csv  
#and take only ‘RM’ and ‘Price’ of the houses. Divide the data as training and testing  
#data. Fit line using Ridge regression and to find price of a house if it contains 5 rooms 
#and compare results.                                                                                             

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso

df = pd.read_csv("boston_houses.csv")

X = df[['RM']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)

ridge.fit(X_train, y_train)
lasso.fit(X_train, y_train)

ridge_pred = ridge.predict([[5]])[0]
lasso_pred = lasso.predict([[5]])[0]

print("Predicted price using Ridge Regression (for 5 rooms):", round(ridge_pred, 2))
print("Predicted price using Lasso Regression (for 5 rooms):", round(lasso_pred, 2))

plt.scatter(X, y, color='gray', label='Actual Data')
plt.plot(X, ridge.predict(X), color='blue', label='Ridge Regression Line')
plt.plot(X, lasso.predict(X), color='red', linestyle='--', label='Lasso Regression Line')
plt.xlabel('Number of Rooms (RM)')
plt.ylabel('Price')
plt.title('Ridge vs Lasso Regression (Boston Housing)')
plt.legend()
plt.show()



## Another alternate code for boston_house
import pandas as pd
from sklearn.linear_model import Ridge, Lasso

# Sample data (RM = rooms, Price = house price)
data = {'RM': [4, 5, 6, 7, 8], 'Price': [150, 200, 250, 300, 350]}
df = pd.DataFrame(data)

X = df[['RM']]
y = df['Price']

# Ridge and Lasso models
ridge = Ridge().fit(X, y)
lasso = Lasso().fit(X, y)

# Predict price for 5 rooms
print("Ridge Prediction:", ridge.predict([[5]])[0])
print("Lasso Prediction:", lasso.predict([[5]])[0])



#Q.2. Write a python program to implement Linear SVM using UniversalBank.csv

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.DataFrame({
    'Age': [25, 35, 45, 20, 30, 40, 50],
    'Income': [40, 60, 80, 20, 50, 70, 90],
    'Education': [1, 2, 2, 1, 3, 2, 3],
    'Personal_Loan': [0, 0, 1, 0, 0, 1, 1]
})

X = df[['Age', 'Income', 'Education']]
y = df['Personal_Loan']

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3, random_state=1)

model = SVC(kernel='linear')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Predictions:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))

plt.scatter(df['Age'], df['Income'], c=df['Personal_Loan'], s=100)
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Scatter Plot: Age vs Income (Colored by Loan Approval)")
plt.colorbar(label="Personal Loan (0 = No, 1 = Yes)")
plt.show()
