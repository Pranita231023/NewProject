#Q.1.Fit the simple linear regression and polynomial linear regression models to 
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


#Q.2.Write a python program to implement Naive Bayes on weather forecast dataset. 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

df = pd.read_csv("Weather_Forecast.csv")

le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])

X = df.drop('Play', axis=1)
y = df['Play']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predicted values:", y_pred)
print("Actual values   :", y_test.values)
print("Accuracy:", accuracy_score(y_test, y_pred))









#Without CSV File

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

dataset = pd.DataFrame(data)
print("Weather Forecast Dataset:\n")
print(dataset)

le = LabelEncoder()
for col in dataset.columns:
    dataset[col] = le.fit_transform(dataset[col])

X = dataset.drop('Play', axis=1)
y = dataset['Play']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nPrediction for new weather condition (Sunny, Cool, High, Strong):", "Play" if prediction[0]==1 else "Don't Play")
