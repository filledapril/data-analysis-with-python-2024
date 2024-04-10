#!/usr/bin/env python3
import scipy
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score

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

def nonconvex_clusters():
    data = pd.read_csv("src/data.tsv", sep="\t") 
    X, y = data[['X1','X2']], data['y']
    k, cl_size = np.arange(0.05, 0.2, 0.05), len(np.unique(y))
    eps, Score, Clusters, Outliers = [], [], [], []
    for i in k:
        model = DBSCAN(eps=i)
        model.fit(X)

        mask = model.labels_ == -1
        lbl = len(np.unique(model.labels_[~mask]))

        eps.append(i), Clusters.append(lbl), Outliers.append(sum(mask))

        if lbl != cl_size:
            Score.append(np.nan)
        else:
            permutation = find_permutation(cl_size, y, model.labels_)
            new_labels = np.array([ permutation[label] for label in model.labels_])
            acc = accuracy_score(y[~mask], new_labels[~mask])
            Score.append(acc)

    arr = np.array([eps, Score, Clusters, Outliers]).T
    return pd.DataFrame(arr, columns = ['eps', 'Score', 'Clusters', 'Outliers'])


# model solution
# def nonconvex_clusters():
#     df = pd.read_csv("src/data.tsv", sep="\t")
#     X = df.loc[:, "X1":"X2"].values
#     y = df.y.values
#     result = []
#     for e in np.arange(0.05, 0.2, 0.05):
#         model=DBSCAN(e)
#         model.fit(X)
#         idx = model.labels_ == -1
#         outliers = np.sum(idx)
#         clusters = max(model.labels_) + 1
#         if clusters == 2:
#             permutation = find_permutation(y, model.labels_)
#             acc = accuracy_score(y[~idx], [ permutation[label] for label in model.labels_[~idx]])
#         else:
#             acc = np.nan
#         result.append([e, acc, clusters, outliers])
#     df2 = pd.DataFrame(np.array(result))
#     df2.columns = ["eps", "Score", "Clusters", "Outliers"]
#     return df2
def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
