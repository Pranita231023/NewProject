#Q.1. Write a python program to implement simple Linear Regression for predicting house   
#price. First find all null values in a given dataset and remove them.     

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 1: Load dataset from CSV file
# (Make sure your CSV file is in the same folder as this script)
df = pd.read_csv("house_data.csv")

print("Original Dataset:\n", df)

# Step 2: Check and remove null (missing) values
print("\nNull values in each column:\n", df.isnull().sum())
df = df.dropna()
print("\nDataset after removing null values:\n", df)

# Step 3: Prepare data
X = df[['Area']]   # Independent variable
y = df['Price']    # Dependent variable

# Step 4: Create and train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Step 5: Predict prices
df['Predicted_Price'] = model.predict(X)
print("\nPredicted Prices:\n", df)

# Step 6: Plot actual vs predicted prices
plt.scatter(df['Area'], df['Price'], color='blue', label='Actual Price')
plt.plot(df['Area'], df['Predicted_Price'], color='red', label='Predicted Price')
plt.xlabel("Area (sq ft)")
plt.ylabel("Price")
plt.title("Simple Linear Regression: House Price Prediction")
plt.legend()
plt.show()






#Q.2. The data set refers to clients of a wholesale distributor. It includes the annual  
#spending in monetary units on diverse product categories. Using data Wholesale  
#customer dataset compute agglomerative clustering to find out annual spending  
#clients in the same region. 

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Sample data (you can replace with pd.read_csv("Wholesale_customers_data.csv"))
df = pd.DataFrame({
    'Region':[1,1,2,2,3,3],
    'Fresh':[12669,7057,6353,13265,22615,9413],
    'Milk':[9656,9810,8808,1196,5410,8259],
    'Grocery':[7561,9568,7684,4221,7198,5126],
    'Frozen':[214,1762,2405,6404,3915,666],
    'Detergents_Paper':[2674,3293,3516,507,955,1795],
    'Delicassen':[1338,1776,7844,1788,2526,1451]
})


df = pd.DataFrame(data)
print("📊 Dataset:\n", df, "\n")

# Features & scaling
X = StandardScaler().fit_transform(df.iloc[:,1:])

# Agglomerative Clustering
df['Cluster'] = AgglomerativeClustering(n_clusters=3, linkage='ward').fit_predict(X)
print("✅ Cluster Labels Assigned to Each Client:")

print(df[['Region','Cluster']])

# Dendrogram
plt.figure(figsize=(6,4))
dendrogram(linkage(X, method='ward'))
plt.title('Agglomerative Clustering Dendrogram')
plt.show()
