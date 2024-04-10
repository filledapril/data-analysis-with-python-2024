#!/usr/bin/env python3

import scipy
import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score


# def find_permutation(n_clusters, real_labels, labels):
#     permutation=[]
#     for i in range(n_clusters):
#         idx = labels == i
#         # Choose the most common label among data points in the cluster
#         new_label=scipy.stats.mode(real_labels[idx])[0][0]
#         permutation.append(new_label)
#     return permutation

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        print("idx shape:", idx.shape)
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

def plant_clustering():
    data = load_iris()
    X, y = data.data, data.target
    model = KMeans(3, n_init=10, random_state=0)
    model.fit(X)
    permutation = find_permutation(3, y, model.labels_)
    y_pred_mapped = [permutation[label] for label in model.labels_]  # Map cluster labels to true labels
    acc = accuracy_score(y, y_pred_mapped)
    return acc

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()

