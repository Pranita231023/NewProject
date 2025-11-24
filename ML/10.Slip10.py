#Q.1. Write a python program to transform data with Principal Component Analysis (PCA).      
#Use iris dataset.                                                                                                   

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pandas as pd

iris = load_iris()
X = iris.data
y = iris.target

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

df = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
df['Target'] = y

print(df.head())



#Q.2. Write a Python program to prepare Scatter Plot for Iris Dataset. Convert Categorical   
#values in to numeric. 

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(df)

df['species'] = iris.target

df['species_name'] = df['species'].map({0: 'rose', 1: 'jasmine', 2: 'lotus'})

df['species_numeric'] = df['species_name'].astype('category').cat.codes

print(df.head())

plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=df['species_numeric'])
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Scatter Plot for Iris Dataset")
plt.show()
