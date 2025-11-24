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

X = df[['Area', 'Bedrooms', 'Age']]  
y = df['Price']                    

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

results = pd.DataFrame({'Actual Price': y_test, 'Predicted Price': y_pred})
print("\nPrediction Results:\n", results)

print("\nModel Accuracy:")
print("R² Score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))


#Q.2. Write a python program to implement Linear SVM using UniversalBank.csv. 

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
