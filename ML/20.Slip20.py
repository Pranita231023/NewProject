#Q.1. Implement Ridge Regression, Lasso regression model using boston_houses.csv and 
#take only ‘RM’ and ‘Price’ of the houses. divide the data as training and testing 
#data. Fit line using Ridge regression and to find price of a house if it contains 5 
#rooms. and compare results. 

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


#Q.2.  Write a python program to implement Decision Tree whether or not to play Tennis. 


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv("play_tennis.csv")  

le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])

X = df[['Outlook', 'Temperature', 'Humidity', 'Wind']]
y = df['Play']

model = DecisionTreeClassifier(criterion='entropy', random_state=0)
model.fit(X, y)

plt.figure(figsize=(10,6))
plot_tree(model, feature_names=['Outlook', 'Temperature', 'Humidity', 'Wind'],
          class_names=['No', 'Yes'], filled=True)
plt.show()

sample = [[0, 1, 0, 1]]   
prediction = model.predict(sample)

print("Play Tennis?:", "Yes" if prediction[0] == 1 else "No")
