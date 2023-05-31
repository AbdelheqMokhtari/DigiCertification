import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

# Step 1: Load the CSV file
data = pd.read_csv('image_features.csv')

# Step 2: Preprocess the data (if needed)
# ...

# Step 3: Apply K-means clustering
kmeans = KMeans(n_clusters=8, random_state=42)
kmeans.fit(data)

# Step 4: Obtain cluster labels
cluster_labels = kmeans.labels_

# Step 5: Evaluate the clustering
true_labels = [...]  # True labels for the images (ground truth)
ari = adjusted_rand_score(true_labels, cluster_labels)
print(f"Adjusted Rand Index: {ari}")

# Step 6: Assign class labels
# ...

