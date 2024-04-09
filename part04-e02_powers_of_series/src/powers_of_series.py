#!/usr/bin/env python3
import numpy as np
import pandas as pd
import random

def powers_of_series(s, k):
    if s.empty:
        df = pd.DataFrame(index=s.index, columns=range(1, k+1))
    df = pd.DataFrame(s, index = list(s.index), columns = [1])
    for i in range(1, k+1):
        df[i] = s.values ** i
        print(s)
    print (df)
    return df  
def main():
    # s = pd.Series(random.sample(range(10), np.random.randint(1, 5)))
    s = pd.Series([5, 0, -1, 6], index=list("abcd"))
    # k = np.random.randint(1, 10)
    k = 5
    powers_of_series(s, k)
    
if __name__ == "__main__":
    main()
