#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    data = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    grouped_data = data.groupby("Publisher")["WoC"].sum()
    best_publisher = grouped_data.idxmax()
    singles_by_best_publisher = data[data["Publisher"] == best_publisher]
    return singles_by_best_publisher

def main():
    best_record_company()
    

if __name__ == "__main__":
    main()
