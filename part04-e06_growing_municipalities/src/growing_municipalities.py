#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    all_count = len(df)
    increase_count = len(df[df["Population change from the previous year, %"] > 0])
    return increase_count / all_count

def main():
    data = pd.read_csv("src/municipal.tsv", sep="\t")
    data.set_index("Region 2018", inplace=True)
    municipalities_df = data.loc["Akaa":"Äänekoski"]
    percentage = growing_municipalities(municipalities_df)
    print(f"Proportion of growing municipalities: {percentage:.1f}%")

if __name__ == "__main__":
    main()
