#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    data = [{"State":"United Kingdom"},
        {"State":"Finland","Year of independence":1917,"President":"Niinistö"},
        {"State":"USA","Year of independence":1776,"President":"Trump"},
        {"State":"Sweden","Year of independence":1523},
        {"State":"Germany","President":"Steinmeier"},
        {"State":"Russia","Year of independence":1992,"President":"Putin"}]
    df = pd.DataFrame(data)
    df.set_index("State", inplace=True)
    return df
    
               
def main():
    missing_value_types()

if __name__ == "__main__":
    main()
