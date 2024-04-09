#!/usr/bin/env python3

import pandas as pd

def top_bands():
    bands_df = pd.read_csv("src/bands.tsv", sep="\t")
    # print(bands_df)
    top40_df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    # print(top40_df)
    # Convert 'Band' column in bands_df to uppercase
    bands_df['Band'] = bands_df['Band'].str.upper()
    # Convert 'Artist' column in top40_df to uppercase
    top40_df['Artist'] = top40_df['Artist'].str.upper()
    merged_df = pd.merge(bands_df, top40_df, left_on=["Band"], right_on=["Artist"])
    return merged_df

def main():
    merge_data = top_bands()
    print(merge_data)

if __name__ == "__main__":
    main()
