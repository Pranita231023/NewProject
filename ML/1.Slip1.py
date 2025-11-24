#1. Use Apriori algorithm on groceries dataset to find which items are brought together. 
#Use minimum support =0.25    

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Create simple groceries data
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





#2. Write a Python program to prepare Scatter Plot for Iris Dataset. Convert Categorical 
#values in numeric format for a dataset. 

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Step 1: Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(df)

# Add species column (categorical)
df['species'] = iris.target

# Convert numeric species to category names
df['species_name'] = df['species'].map({0: 'rose', 1: 'jasmine', 2: 'lotus'})

# Convert categorical species_name to numeric again
df['species_numeric'] = df['species_name'].astype('category').cat.codes

print(df.head())

# Step 2: Create scatter plot
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=df['species_numeric'])
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Scatter Plot for Iris Dataset")
plt.show()


