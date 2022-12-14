# -*- coding: utf-8 -*-
"""UAS_2440003902

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cLFiSslexKX9wI-jJH0QRMcB-BtguLUi
"""

from numpy.random import uniform, normal, randint, rand
import numpy as np
import pandas as pd

def generate_dataset(seed):
    np.random.seed(seed)
    
    x = np.array([])
    y = np.array([])
    loop = randint(10,15)

    for i in range(loop):
        x = np.append(x, np.random.normal(randint(10), rand(), 20))
        y = np.append(y, np.random.normal(randint(10), rand(), 20))
        
    df = pd.DataFrame(data = {'x': x, 'y':y})
    df.to_csv('dataset.csv', index=False)

student_id = 2440003902

generate_dataset(student_id)

df = pd.read_csv ('/content/dataset.csv')
display(df)

import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.scatter(x=df.x, y=df.y, color='blue')
plt.show()

"""Diatas ini merupakan model scatter plot untuk visualisasi dari dataset yang diberikan.

Visualisasi data seperti ini mungkin belum cukup untuk kebutuhan cluster analysis. Oleh karena itu, selanjutnya akan dilakukan model visualisasi data dengan metode K-Means Clustering.
"""

from sklearn.cluster import KMeans

inertia = []
for cluster in range (1,10):
  km = KMeans(n_clusters=cluster)
  km.fit(df)
  inertia.append(km.inertia_)

plt.figure(figsize=(10,6))
plt.plot(range(1,10), inertia, 'og-')
plt.xlabel('Cluster')
plt.ylabel('Inertia')
plt.title('Elbow Method to Determine Number of Clusters')
plt.show()

"""Pada hasil elbow method ini, dapat terlihat sudut dari lengkungan 'elbow' yang terbentuk ada di angka 3. Sehingga, dapat disimpulkan bahwa jumlah cluster yang optimal sebanyak 3 cluster."""

km = KMeans(n_clusters=3)
km.fit(df)

plt.figure(figsize=(12,6))
sct = plt.scatter(x= df.iloc[:, 0], y=df.iloc[:, 1], c= km.labels_)
plt.title('K-Means Clustering Data Visualization')
plt.xlabel('X')
plt.ylabel('Y')

plt.legend(handles=sct.legend_elements()[0], labels=[1, 2, 3]);

"""Ini adalah hasil dari visualisasi clustering data menggunakan K-Means Clustering. Disini, cluster berjumlah 3 sesuai dengan Elbow Method yang telah dilakukan dan dibedakan menjadi 3 warna yang berbeda."""