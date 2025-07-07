from sklearn.cluster import KMeans
import numpy as np

data = np.array([[1,2],[2,3],[3,4],[8,9],[9,10]])

KMeans = KMeans(n_clusters=2, random_state=0)
KMeans.fit(data)

print('Cluster Centers:', KMeans.cluster_centers_)
print('Predicted Labels:', KMeans.labels_)