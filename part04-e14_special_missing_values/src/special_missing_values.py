#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    data = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    data.replace(["New", "Re"],None, inplace=True)
    data['LW'] = pd.to_numeric(data['LW'], errors='coerce')
    drop = data.loc[data['Pos'].notna() & data['LW'].notna() & (data['Pos'] > data['LW'])]
    return drop

def main():
    special_missing_values()

if __name__ == "__main__":
    main()
