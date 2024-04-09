#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)
    slope = model.coef_[0]
    intercept = model.intercept_
    return slope, intercept
    
def main():
    # Slope: 1.0
    # Intercept: 1.16666666667
    np.random.seed(0)
    n=20   # Number of data points
    x=np.linspace(0, 10, n)
    y=x*2 + 1 + 1*np.random.randn(n)
    slope, intercept = fit_line(x, y)
    print("Slope:", slope)
    print("Intercept:", intercept)

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'o', label='Original Data')
    xfit = np.linspace(0, 10, 100)
    yfit = slope * xfit + intercept
    plt.plot(xfit, yfit, color='black', label='Fitted Line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Linear Regression')
    plt.grid(True)
    plt.show()


# medel solution
# def fit_line(x, y):
#     reg = LinearRegression()
#     X = x.reshape((-1, 1))
#     reg.fit(X, y)
#     return reg.coef_[0], reg.intercept_
    
# def main():
#     x = np.array([1, 2, 3])
#     y = np.array([1, 2.5, 3]) + 1
#     slope, intercept = fit_line(x, y)
#     print("Slope:", slope)
#     print("Intercept:", intercept)
#     plt.scatter(x, y)
#     x1 = np.linspace(min(x)-1, max(x)+1, 10)
#     plt.plot(x1, x1*slope + intercept, 'red')
#     plt.show()
    
if __name__ == "__main__":
    main()
