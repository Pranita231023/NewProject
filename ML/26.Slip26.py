#Q.1. Create KNN model on Indian diabetes patient’s database and predict whether a new 
#patient is diabetic (1) or not (0). Find optimal value of K.                                        





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
