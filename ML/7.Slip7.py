#Q.1. Fit the simple linear regression model to Salary_positions.csv data. Predict the salary 
#of level 11 and level 12 employees. 

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_positions.csv")

X = df[['Level']]
y = df['Salary']

model = LinearRegression()
model.fit(X, y)

df['Predicted_Salary'] = model.predict(X)
print(df)

salary_11 = model.predict([[11]])
salary_12 = model.predict([[12]])
print("Predicted salary for Level 11 =", salary_11[0])
print("Predicted salary for Level 12 =", salary_12[0])

plt.scatter(df['Level'], df['Salary'], color='blue', label='Actual Salary')
plt.plot(df['Level'],df['Predicted_Salary'], color='red', label='Regression Line')
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Salary Prediction using Simple Linear Regression")
plt.legend()
plt.show()



#Q.2. Write a python program to implement Naive Bayes on weather forecast dataset. 

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

# Step 1: Create sample weather dataset
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

# Step 2: Convert categorical data into numeric values
le = LabelEncoder()
for col in dataset.columns:
    dataset[col] = le.fit_transform(dataset[col])

# Step 3: Split dataset into features (X) and target (y)
X = dataset.drop('Play', axis=1)
y = dataset['Play']

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Step 5: Train Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate model
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nPrediction for new weather condition (Sunny, Cool, High, Strong):", "Play" if prediction[0]==1 else "Don't Play")
