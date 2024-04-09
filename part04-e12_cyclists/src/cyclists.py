#!/usr/bin/env python3

import pandas as pd

def cyclists():
    data = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", delimiter=";")
    data = data.dropna(axis=0, how="all").dropna(axis=1, how="all")
    return data



def main():
    cyclists()
    
if __name__ == "__main__":
    main()
