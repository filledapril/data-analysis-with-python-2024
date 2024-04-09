#!/usr/bin/env python3

import pandas as pd

def split_date(df):
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


def split_date_continues():
    # read the bicycle data set
    data = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    # clean the data set of columns/rows that contain only missing values
    data_cleaned = data.dropna(axis=1, how='all')
    data_cleaned = data.dropna(axis=0, how='all')
    # drops the Päivämäärä column and replaces it with its splitted components as before
    date = split_date(data_cleaned)
    data_cleaned = data_cleaned.drop("Päivämäärä", axis=1)
    data = pd.concat([date, data_cleaned], axis=1)
    return data.iloc[:, :25]

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
