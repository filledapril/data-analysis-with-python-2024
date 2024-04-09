#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    data = pd.read_csv("src/kumpula-weather-2017.csv")
    july = data.loc[(data.m == 7), ["Air temperature (degC)"]]
    return july.mean()[0]

def main():
    t = average_temperature()
    print(f"Average temperature in July: {t:.1f}")

if __name__ == "__main__":
    main()
