# Segmentation script template (auto-generated)
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

df = pd.read_csv('../data/marketing_data.csv')
features = ['Income', 'Teenhome', 'Recency', 'MntWines']
df_f = df[features].fillna(0)
scaler = StandardScaler()
X = scaler.fit_transform(df_f)

# Example: choose k after running Elbow/Silhouette
k = 4
km = KMeans(n_clusters=k, random_state=42, n_init=10)
labels = km.fit_predict(X)
df['Cluster'] = labels
print(df.groupby('Cluster')[features].mean())

pca = PCA(n_components=2, random_state=42)
X2 = pca.fit_transform(X)
plt.scatter(X2[:,0], X2[:,1], c=labels, cmap='tab10', s=30)
plt.savefig('../images/cluster_plot_script.png', bbox_inches='tight')
