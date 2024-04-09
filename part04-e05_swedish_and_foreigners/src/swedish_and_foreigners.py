#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    data = pd.read_csv("src/municipal.tsv", sep="\t")
    data.set_index("Region 2018", inplace=True)
    municipalities_df = data.loc["Akaa":"Äänekoski"]
    print(municipalities_df)
    s_f_df = municipalities_df[(municipalities_df["Share of Swedish-speakers of the population, %"] > 5.0) & 
                                (municipalities_df["Share of foreign citizens of the population, %"] > 5.0)]
    print(s_f_df)
    return s_f_df[["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]

def main():
    swedish_and_foreigners()

if __name__ == "__main__":
    main()
