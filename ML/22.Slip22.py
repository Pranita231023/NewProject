#Q.1. Write a python program to implement simple Linear Regression for predicting house price.                                                                                                                     

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# (Make sure your CSV file is in the same folder as this script)
df = pd.read_csv("house_data.csv")

print("Original Dataset:\n", df)

print("\nNull values in each column:\n", df.isnull().sum())
df = df.dropna()
print("\nDataset after removing null values:\n", df)

X = df[['Area']]   # Independent variable
y = df['Price']    # Dependent variable

model = LinearRegression()
model.fit(X, y)

df['Predicted_Price'] = model.predict(X)
print("\nPredicted Prices:\n", df)

plt.scatter(df['Area'], df['Price'], color='blue', label='Actual Price')
plt.plot(df['Area'], df['Predicted_Price'], color='red', label='Predicted Price')
plt.xlabel("Area (sq ft)")
plt.ylabel("Price")
plt.title("Simple Linear Regression: House Price Prediction")
plt.legend()
plt.show()


#Q.2. Use Apriori algorithm on groceries dataset to find which items are brought together. 
#Use minimum support =0.25 

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

groceries = [
    ['milk', 'bread', 'butter'],
    ['bread', 'butter'],
    ['milk', 'bread'],
    ['milk', 'bread', 'butter'],
    ['bread', 'butter']
]

te = TransactionEncoder()
data = te.fit(groceries).transform(groceries)
df = pd.DataFrame(data, columns=te.columns_)

print("Transaction Data:\n")
print(df)

frequent = apriori(df, min_support=0.25, use_colnames=True)
print("\nFrequent Itemsets:\n",frequent)

rules = association_rules(frequent, metric="confidence", min_threshold=0.5)
print("\nAssociation Rules:\n")
print(rules[['antecedents', 'consequents', 'support', 'confidence']])
