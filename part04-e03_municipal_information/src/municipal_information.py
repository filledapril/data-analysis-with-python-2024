#!/usr/bin/env python3

import pandas as pd

def main():
    data =  pd.read_csv("src/municipal.tsv", sep='\t')
    data.head()
    c = data.shape[1]
    r = len(data)

    print(f"Shape: {r}, {c}\nColumns:")
    for col in data.columns:
        print(col)

if __name__ == "__main__":
    main()
