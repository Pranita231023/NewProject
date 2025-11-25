#Q.1. Create KNN model on Indian diabetes patient’s database and predict whether a new 
#patient is diabetic (1) or not (0). Find optimal value of K.                                        

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.DataFrame({
 'Preg':[6,1,8,1,0,5,3,10],
 'Glucose':[148,85,183,89,137,116,78,115],
 'BP':[72,66,64,66,40,74,50,70],
 'BMI':[33.6,26.6,23.3,28.1,43.1,25.6,31.0,35.3],
 'Age':[50,31,32,21,33,30,26,29],
 'Outcome':[1,0,1,0,1,0,0,1]
})

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

Xtr, Xte, Ytr, Yte = train_test_split(X, y, test_size=0.25)
best_k = max(range(1,4), key=lambda k:
    KNeighborsClassifier(k).fit(Xtr,Ytr).score(Xte,Yte))

print("Best K =", best_k)
model = KNeighborsClassifier(best_k).fit(Xtr, Ytr)
print("Prediction:", model.predict([[5,120,70,32,35]])[0])




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
print("\nAssociation Rules:\n",rules)
