#Q.1.   Write a python program to implement multiple Linear Regression for a house price 
#dataset. Divide the dataset into training and testing data.  

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





  
#Q.2.  Use dataset crash.csv is an accident survivor’s dataset portal for USA hosted by 
#data.gov. The dataset contains passengers age and speed of vehicle (mph) at the time 
#of impact and fate of passengers (1 for survived and 0 for not survived) after a crash.  
#use logistic regression to decide if the age and speed can predict the survivability of the  
#passengers. 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    'Age': [18, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
    'Speed': [80, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15],
    'Fate': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 1=Survived, 0=Not Survived
}
df = pd.DataFrame(data)

print(" Sample Crash Dataset:\n", df, "\n")

X = df[['Age', 'Speed']]
y = df['Fate']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\n Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\n Classification Report:\n", classification_report(y_test, y_pred))

sample = pd.DataFrame({'Age':[30], 'Speed':[70]})
print("\nPredicted Fate (1=Survived, 0=Not Survived):", model.predict(sample)[0])

