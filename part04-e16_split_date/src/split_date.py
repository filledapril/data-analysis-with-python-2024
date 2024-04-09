#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    # weekday_mapping = {
    # "ma": "Mon",
    # "ti": "Tue",
    # "ke": "Wed",
    # "to": "Thu",
    # "pe": "Fri",
    # "la": "Sat",
    # "su": "Sun"
    # }
    # month_mapping_numeric = {
    # "tammi": 1,
    # "helmi": 2,
    # "maalis": 3,
    # "huhti": 4,
    # "touko": 5,
    # "kesä": 6,
    # "heinä": 7,
    # "elo": 8,
    # "syys": 9,
    # "loka": 10,
    # "marras": 11,
    # "joulu": 12
    # }
    # data = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep="\;", engine='python')
    # data = data[["Päivämäärä"]]
    # data = data.dropna(axis=0, how="all").dropna(axis=1, how="all")
    # # Split the date string on spaces and expand it into separate columns
    # date_components = data["Päivämäärä"].str.split(expand=True)
    
    # # Assign the extracted components to new columns
    # data["Weekday"] = date_components[0].map(weekday_mapping)
    # data["Day"] = date_components[1].astype(int)
    # data["Month"] = date_components[2].map(month_mapping_numeric)
    # data["Year"] = date_components[3].astype(int)
    # # Extract hour from the fifth component (index 4) of the date string
    # data["Hour"] = date_components[4].str.split(":").str[0]
    # # Convert the hour column to float and handle missing values
    # data["Hour"] = data["Hour"].replace("", np.nan).astype(float)
    
    # # Drop the original "Päivämäärä" column
    # data = data.drop("Päivämäärä", axis=1)
    # print(data)

    # return data

    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    date = df["Päivämäärä"].str.split(expand=True)
    date[[4,5]] = date[4].str.split(":",expand=True)
    date = date.drop(5,axis=1)
    date = date.dropna()
    date = date.rename(columns={0:"Weekday",1:"Day",2:"Month",3:"Year",4:"Hour"})
    weekdayDic = {"ma":"Mon","ti":"Tue","ke":"Wed","to":"Thu","pe":"Fri","la":"Sat","su":"Sun"}
    monthDic = {"tammi":1,"helmi":2,"maalis":3,"huhti":4,"touko":5,"kesä":6,"heinä":7,"elo":8,
                "syys":9,"loka":10,"marras":11,"joulu":12}
    date['Weekday'] = date["Weekday"].map(weekdayDic)
    date['Month'] = date["Month"].map(monthDic).map(int)
    date[['Day','Year','Hour']] = date[['Day','Year','Hour']].astype(int)
    print(date)
    print(date.dtypes)
    return date

def main():
    split_date()
       
if __name__ == "__main__":
    main()
