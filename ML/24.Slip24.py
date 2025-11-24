#Q.1. Write a python program to Implement Decision Tree classifier model on Data which is 
#extracted from images that were taken from genuine and forged banknote-like 
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

# Create and train Decision Tree model
model = DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


#Q.2. Write a python program to implement linear SVM using UniversalBank.csv.

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
