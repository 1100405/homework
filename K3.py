import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

df = pd.read_csv("dye.csv")
df_group = df.groupby('class')

df_centers = pd.DataFrame()

for name, group in df_group:
    shuffled_group = group.sample(frac=1, random_state=405)
    first_50_rows = shuffled_group.head(50)
    
    X = first_50_rows.drop(columns=['class'])

    kmeans = KMeans(n_clusters=2, max_iter=20, random_state=405)
    result = kmeans.fit(X)
    
    df_temp = pd.DataFrame({
        'd1': result.cluster_centers_[:, 0],
        'c1': result.cluster_centers_[:, 1],
        'd2': result.cluster_centers_[:, 2],
        'c2': result.cluster_centers_[:, 3],
        'd3': result.cluster_centers_[:, 4],
        'c3': result.cluster_centers_[:, 5]
    })
    df_centers = pd.concat([df_centers, df_temp], ignore_index=True)

print(df_centers)