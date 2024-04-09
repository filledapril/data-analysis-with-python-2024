#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

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

def commute():
    data = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    cleaned_data = data.dropna(axis=1, how='all').dropna(axis=0, how='all')
    date = split_date(cleaned_data)
    cleaned_data = cleaned_data.drop("Päivämäärä", axis=1)
    cleaned_data["Date"] = pd.to_datetime(date[['Year', 'Month', 'Day', 'Hour']])
    cleaned_data = cleaned_data.set_index("Date")
    august_data = cleaned_data.loc['2017-08']
    weekday_sum = august_data.groupby(august_data.index.weekday).sum()
    weekday_sum["Weekday"] = weekday_sum.index.map({0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7})
    weekday_sum = weekday_sum.set_index("Weekday")
    print(weekday_sum)
    return weekday_sum
    
def main():
    data = commute()
    data.plot()
    weekdays = "x mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(weekdays)
    plt.show()


if __name__ == "__main__":
    main()
