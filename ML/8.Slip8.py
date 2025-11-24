#Q.1. Write a python program to categorize the given news text into one of the available 20 
#categories of news groups, using multinomial Naïve Bayes machine learning model.

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = fetch_20newsgroups(subset='train')

cv = CountVectorizer(stop_words='english')
X = cv.fit_transform(data.data)

model = MultinomialNB()
model.fit(X, data.target)

news = ["NASA launched a new satellite to study the atmosphere of Mars."]
X_new = cv.transform(news)
pred = model.predict(X_new)

print("News Text:", news[0])
print("Predicted Category:", data.target_names[pred[0]])





#Q.2. Write a python program to implement Decision Tree whether or not to play Tennis. 

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
