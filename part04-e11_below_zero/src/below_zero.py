#!/usr/bin/env python3

import pandas as pd

def below_zero():
    data = pd.read_csv("src/kumpula-weather-2017.csv")
    below_o = data.loc[(data["Air temperature (degC)"]<0), ["d"]]
    print(below_o.describe().loc["count"])
    return below_o.describe().loc["count"][0]

def main():
    day = below_zero()
    print(f"Number of days below zero: {day:.0f}")
# Number of days below zero: xx
    
if __name__ == "__main__":
    main()
