#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    data = pd.read_csv("src/mystery_data.tsv", sep="\t")
    X = data.iloc[:, :-1]  # Selecting all columns except the last one (features)
    y = data.iloc[:, -1]   # Selecting the last column as the target variable
    
    r_squared_scores = []

    # Part 1: R2-score with all features
    model = linear_model.LinearRegression(fit_intercept=True)  # Include the intercept
    model.fit(X, y)
    r_squared_scores.append(model.score(X, y))

    # Part 2: R2-score with each single feature
    for col in X.columns:
        model = linear_model.LinearRegression(fit_intercept=True)  # Include the intercept
        model.fit(X[[col]], y)
        r_squared_scores.append(model.score(X[[col]], y))

    return r_squared_scores

def main():
    r_squared_scores = coefficient_of_determination()
    print("R2-score with feature(s) X:", r_squared_scores[0])
    for i, score in enumerate(r_squared_scores[1:], start=1):
        print(f"R2-score with feature(s) X{i}:", score)

# model sulution
# def main():
#     scores = coefficient_of_determination()
 
#     z = scores[1:]
#     for i in range(4):
#         print(sum(z[i:i+2]))
        
#     titles = "X X1 X2 X3 X4 X5".split()
#     for title, score in zip(titles, scores):
#         print(f"R2-score with feature(s) {title}: {score:.2f}")

if __name__ == "__main__":
    main()
