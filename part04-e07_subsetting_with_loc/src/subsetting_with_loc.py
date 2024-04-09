#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    data = pd.read_csv("src/municipal.tsv", sep="\t")
    data.set_index("Region 2018", inplace=True)
    return data.loc['Akaa':'Äänekoski', ["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]


def main():
    print(subsetting_with_loc())
    return

if __name__ == "__main__":
    main()
