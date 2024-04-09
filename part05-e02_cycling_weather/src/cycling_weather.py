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

def cycling_weather():
    cyc_data = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    weath_data = pd.read_csv("src/kumpula-weather-2017.csv", sep=",")
    cyc_data_cleaned = cyc_data.dropna(axis=1, how='all').dropna(axis=0, how='all')
    date = split_date(cyc_data_cleaned)
    data_cleaned = cyc_data_cleaned.drop("Päivämäärä", axis=1)
    cyc_data = pd.concat([date, data_cleaned], axis=1)
    # Merge the processed cycling data set (from the previous exercise) and weather data set along the columns year, month, and day.
    merged_data = pd.merge(cyc_data, weath_data, left_on=["Year", "Month", "Day"], right_on=["Year", "m", "d"])
    merged_data = merged_data.drop(columns=['m', 'd', 'Time', 'Time zone'])
    print(merged_data)
    return merged_data

def main():
    cycling_weather()

if __name__ == "__main__":
    main()
