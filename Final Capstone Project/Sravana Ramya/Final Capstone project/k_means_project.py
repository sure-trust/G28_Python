# -*- coding: utf-8 -*-
"""k-means Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rmdtgMdl3QFZYxYdLhi4eyWu5E5tSkGY
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("/content/WA_Fn-UseC_-Telco-Customer-Churn.csv")

data.head()

data.info()

data.shape

print(data.isnull().sum())

data.drop("customerID",axis=1 , inplace = True)

data.dropna(inplace=True)

data.info()

Object_type=[]
for column in data.columns:
  if data[column].dtype=="object":
   Object_type.append(column)

from sklearn.preprocessing import OrdinalEncoder

oe=OrdinalEncoder().fit(data[Object_type])

sns.scatterplot(x='tenure', y='MonthlyCharges', data=data)
plt.title('Scatter Plot of tenure vs Monthly Charges')

from sklearn.cluster import KMeans

x =  data[["tenure","MonthlyCharges"]]

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x21_standardized = scaler.fit_transform(x)

inertia = []
for i in range(1,11):
  kmeans = KMeans(n_clusters=i).fit(x)
  inertia.append(kmeans.inertia_)

min(inertia), max(inertia)

plt.plot(range(1,11), inertia, "-*")

kmeans = KMeans(n_clusters=5)
kmeans.fit(x)

ypred = kmeans.predict(x)

x.iloc[ypred == 0, 0].shape == x.iloc[ypred == 0, 1].shape

centroids = kmeans.cluster_centers_

plt.scatter(x.loc[ypred == 0,"tenure"], x.loc[ypred==0, "MonthlyCharges"], c = "g", label = "Cluster 1" )
plt.scatter(x.loc[ypred == 1,"tenure"], x.loc[ypred==1, "MonthlyCharges"], c = "r",label = "Cluster 2" )
plt.scatter(x.loc[ypred == 2,"tenure"], x.loc[ypred==2, "MonthlyCharges"], c = "y" ,label = "Cluster 3")
plt.scatter(x.loc[ypred == 3,"tenure"], x.loc[ypred==3, "MonthlyCharges"], c = "r" ,label = "Cluster 4")
plt.scatter(x.loc[ypred == 4,"tenure"], x.loc[ypred==4, "MonthlyCharges"], c = "pink" ,label = "Cluster 5")
plt.scatter(centroids[:,0],centroids[:,1], c= "black", s=200, label = "Centroids" )
plt.xlabel("tenure")
plt.ylabel("MonthlyCharges")
plt.title("Clustering")

