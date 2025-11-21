#SLIP 1 


#SLIP 1 , 22 , 26
#1.Use Apriori algorithm on groceries dataset to find which items are brought together. Use minimum support =0.25

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# -----------------------------
# Dataset (You can switch datasets here)
# -----------------------------

dataset = [
    ['Milk', 'Bread', 'Butter'],
    ['Bread', 'Butter', 'Eggs'],
    ['Milk', 'Bread', 'Butter', 'Eggs'],
    ['Milk', 'Bread'],
    ['Bread', 'Butter']
]

# -----------------------------
# ONE-HOT ENCODING
# -----------------------------

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

print("🛒 Groceries Dataset:\n")
print(df, "\n")

# -----------------------------
# APRIORI ALGORITHM
# -----------------------------

frequent_itemsets = apriori(df, min_support=0.25, use_colnames=True)

print("✅ Frequent Itemsets:\n")
print(frequent_itemsets, "\n")

# -----------------------------
# ASSOCIATION RULES
# -----------------------------

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

print("📊 Association Rules (Items bought together):\n")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
