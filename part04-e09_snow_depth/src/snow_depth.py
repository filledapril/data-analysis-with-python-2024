#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    data = pd.read_csv("src/kumpula-weather-2017.csv")
    dc = data.describe()
    return dc.loc['max'].loc['Snow depth (cm)']

def main():
    sd = snow_depth()
    print(f"Max snow depth: {sd}")



if __name__ == "__main__":
    main()
