#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def explained_variance():
    data = pd.read_csv("src/data.tsv", sep="\t")
    variances = data.var()
    model = PCA()
    model.fit(data)
    explained_variances = model.explained_variance_
    return variances, explained_variances

# The variances are: ?.??? ?.??? ...
# The explained variances after PCA are:
def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))
    # Print variances
    print("The variances are:", " ".join([f"{var:.3f}" for var in v]))
    # Print explained variances after PCA
    print("The explained variances after PCA are:", " ".join([f"{ev:.3f}" for ev in ev]))
    plt.plot(np.arange(1,len(ev)+1), np.cumsum(ev))
    plt.show()

# model solution
# def explained_variance():
#     df=pd.read_csv("src/data.tsv", sep="\t")
#     variance = df.var(axis=0).values
#     pca = PCA(10)
#     pca.fit(df)
#     return variance, pca.explained_variance_
 
# def main():
#     v, ev = explained_variance()
#     print(sum(v), sum(ev))
#     print("The variances are:", " ".join([f"{x:.3f}" for x in v]))
#     print("The explained variances after PCA are:", " ".join([f"{x:.3f}" for x in ev]))
#     plt.plot(np.arange(1,11), np.cumsum(ev));
#     plt.show()

if __name__ == "__main__":
    main()
