import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("dye.csv")

X = df.drop(columns=['class'])

kmeans = KMeans(n_clusters=3, max_iter=20, random_state=405)
result = kmeans.fit(X)

cluster_df = pd.DataFrame({'class': result.labels_})
cluster_df.to_csv("cluster3_py.csv", index=False)

plt.scatter(result.cluster_centers_[:, 0], result.cluster_centers_[:, 1], color='gray')
plt.xlabel('d1')
plt.ylabel('c1')
plt.title('Cluster Centers')
plt.xlim(0, 50)
plt.ylim(0, 1)
plt.show()
