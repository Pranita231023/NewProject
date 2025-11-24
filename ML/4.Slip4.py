#Q.1. Write a python program to implement k-means algorithm on a mall_customers dataset.  

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [19, 35, 26, 27, 32, 40, 23, 30, 31, 22],
    'Annual_Income': [15, 35, 75, 40, 20, 60, 70, 25, 55, 80],
    'Spending_Score': [39, 81, 6, 77, 40, 20, 80, 35, 66, 85]
}

df = pd.DataFrame(data)
print("Sample Mall Customers Dataset:",df)

X = df[['Annual_Income', 'Spending_Score']]

kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)
print("\nClustered Data:",df)

plt.scatter(df['Annual_Income'], df['Spending_Score'], c=df['Cluster'])
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (0–100)")
plt.title("K-Means Clustering on Mall Customers Dataset")
plt.show()




#Q.2. Write a python program to Implement Simple Linear Regression for predicting house price.

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

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
