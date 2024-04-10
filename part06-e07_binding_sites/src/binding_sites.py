#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import euclidean_distances
from matplotlib import pyplot as plt

# import seaborn as sns
# sns.set(color_codes=True)
# import scipy.spatial as sp
# import scipy.cluster.hierarchy as hc

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # print("idx shape:", idx.shape)
        print("real_labels[idx]:", real_labels[idx])
        mode_result = scipy.stats.mode(real_labels[idx])
        print("Mode result:", mode_result)
        print("Type of mode result:", type(mode_result))
        # Choose the most common label among data points in the cluster
        if np.isscalar(mode_result.mode):
            new_label = mode_result.mode  # Mode is scalar, directly use it
        else:
            new_label = mode_result.mode[0]  # Accessing the mode value
        permutation.append(new_label)
    return permutation

def toint(x):
    toint_dict = {"A": 0, "C": 1, "G": 2, "T": 3}
    return toint_dict.get(x, -1) 

def get_features_and_labels(filename):
    data = pd.read_csv(filename, sep='\t')
    feature_matrix = []  # Initialize empty feature matrix
    for sequence in data['X']:
        feature_sequence = [toint(nucleotide) for nucleotide in sequence]  # Convert each nucleotide to integer
        feature_matrix.append(feature_sequence) # Add the feature sequence to feature matrix
    feature_matrix = np.array(feature_matrix)
    label_vector = data['y'].values  # Extract label vector
    return feature_matrix, label_vector

# def plot(distances, method='average', affinity='euclidean'):
#     mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
#     g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
#     g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
#     plt.show()

def cluster_euclidean(filename):
    X, y = get_features_and_labels(filename)
    model = AgglomerativeClustering(linkage='average', affinity='euclidean', n_clusters=2)
    model.fit(X)
    permutation = find_permutation(2, y, model.labels_)
    new_labels = [ permutation[label] for label in model.labels_]
    acc = accuracy_score(y, new_labels)
    return acc

def cluster_hamming(filename):
    X, y = get_features_and_labels(filename)
    distance_matrix = pairwise_distances(X, metric='hamming')
    clustering = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='average').fit(distance_matrix)
    permutation = find_permutation(2, y, clustering.labels_)
    y_pred_mapped = [permutation[lable] for lable in clustering.labels_]
    acc = accuracy_score(y, y_pred_mapped)
    # plot(distance_matrix)

    return acc


def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
