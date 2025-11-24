#Q.1. Write a python program to implement Polynomial Regression for  
#Boston Housing Dataset.                                                                                        

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

data = {
    'RM': [4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0],
    'PRICE': [15.0, 17.5, 20.0, 22.0, 25.0, 28.5, 30.0, 35.0]
}

df = pd.DataFrame(data)
print("Boston Housing Manual Dataset:\n", df)

X = df[['RM']]
y = df['PRICE']

poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)

r2 = r2_score(y, y_pred)
print(f"\nModel Accuracy (R² Score): {r2:.4f}")

new_value = np.array([[7]])
new_value_poly = poly.transform(new_value)
pred = model.predict(new_value_poly)
print(f"Predicted Price for RM=7: ${pred[0]*1000:.2f}")

plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Polynomial Regression (degree=3)')
plt.xlabel("Average Number of Rooms (RM)")
plt.ylabel("House Price ($1000s)")
plt.title("Polynomial Regression - Boston Housing (Manual Data)")
plt.legend()
plt.show()



#Q.2. Write a python program to Implement Decision Tree classifier model on Data which  
#is extracted from images that were taken from genuine and forged banknote-like  
#specimens. 
#(refer UCI dataset https://archive.ics.uci.edu/dataset/267/banknote+authentication) 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

column_names = ['variance', 'skewness', 'curtosis', 'entropy', 'class']
df = pd.read_csv('data_banknote_authentication.txt', names=column_names)

X = df.drop('class', axis=1)
y = df['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
