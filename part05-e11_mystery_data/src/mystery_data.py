#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    data = pd.read_csv("src/mystery_data.tsv", sep="\t")
    # Selecting all columns except the last one
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    model=LinearRegression(fit_intercept=False)
    model.fit(X, y)
    return model.coef_

def main():
    coefficients = mystery_data()
    print("Coefficient of X1 is", coefficients[0])
    print("Coefficient of X2 is", coefficients[1])
    print("Coefficient of X3 is", coefficients[2])
    print("Coefficient of X4 is", coefficients[3])
    print("Coefficient of X5 is", coefficients[4])
    
if __name__ == "__main__":
    main()
