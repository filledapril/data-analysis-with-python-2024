#!/usr/bin/env python3
import numpy as np
import pandas as pd

def last_week():
        data = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    
        # Drop rows where 'LW' is "New" or "Re"
        data.drop(data[(data['LW'] == "New") | (data['LW'] == "Re")].index, inplace=True)
        
        # Decrement 'WoC' by 1
        data["WoC"] -= 1
        
        # Convert 'LW' to integer
        data["LW"] = data["LW"].astype(float)
        
        # Replace 'Peak Pos' with NaN where current position is the peak and it increased this week
        data.loc[(data['Peak Pos'] == data["Pos"]) & (data['Pos'] < data['LW']), 'Peak Pos'] = np.nan
        
        # Sort by 'LW'
        data = data.sort_values(by=['LW'])
        
        # Set index to 'LW'
        data.index = data["LW"]
        
        # Reindex to fill missing rows
        data = data.reindex(range(1, 41)) 
        
        # Set 'Pos' column to index
        data["Pos"] = data.index
        
        # Set 'LW' to NaN
        data["LW"] = np.nan
        
        print(data)
    
        return data

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
