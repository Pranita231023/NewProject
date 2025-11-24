#Q.1. Write a python program to implement Polynomial Linear Regression for  
#Boston Housing Dataset.            

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.DataFrame({
    'RM': [4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0],
    'PRICE': [15, 17.5, 20, 22, 25, 28.5, 30, 35]
})

X = df[['RM']]
y = df['PRICE']

poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)

plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.xlabel("RM")
plt.ylabel("PRICE")
plt.title("Polynomial Regression (Degree 3)")
plt.show()


#Q.2. Use K-means clustering model and classify the employees into various income groups 
#or clusters. Preprocess data if require (i.e. drop missing or null values). 

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = {
    'EmployeeID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [25, 27, 29, 32, 35, 40, 45, 48, 52, 58],
    'Income': [25000, 30000, 35000, 40000, 45000, 60000, 80000, 85000, 90000, 95000]
}
df = pd.DataFrame(data)
print(df)
# Drop missing/null values
df.dropna(inplace=True)

X = df[['Age', 'Income']]

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

print("📊 Employee Clusters:\n", df)

plt.scatter(df['Age'], df['Income'], c=df['Cluster'])
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('K-Means Clustering - Employee Income Groups')
plt.show()
