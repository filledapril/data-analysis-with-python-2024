#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    data = pd.read_csv("src/municipal.tsv", sep="\t")
    data.set_index("Region 2018", inplace=True)
    new_df = data.loc["Akaa":"Äänekoski"]
    print(new_df)
    return new_df
    
def main():
    municipalities_of_finland()

    
    return
    
if __name__ == "__main__":
    main()
