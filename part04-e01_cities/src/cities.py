#!/usr/bin/env python3

import pandas as pd

def cities():
    df = pd.DataFrame([[643272, 715.48], [279044, 528.03], [231853, 689.59], [223027, 240.35], [201810, 3817.52]], columns=["Population", "Total area"], index=["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"])
    print(df)
    return df
def main():
    cities()
    
if __name__ == "__main__":
    main()
