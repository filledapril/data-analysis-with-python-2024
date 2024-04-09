#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model

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


def cycling_weather_continues(station):
    data1 = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';').dropna(how='all', axis=1).dropna(how='all', axis=0)
    data2 = pd.read_csv('src/kumpula-weather-2017.csv', sep=',')
    dat1 = split_date(data1)
    dat1 = pd.concat([dat1, data1.iloc[:, 1:]], axis=1)
    dat1 = dat1.groupby(['Year','Month', 'Day']).sum()
    dat = pd.merge(dat1, data2, left_on=['Day', 'Month', 'Year'], right_on=['d', 'm', 'Year'], how='inner')
    dat = dat.drop(['d', 'm', 'Time', 'Time zone', 'Hour'], axis=1)
    res = dat.fillna(method='ffill')
    x1, x2, x3, y = res['Precipitation amount (mm)'], res['Snow depth (cm)'], res['Air temperature (degC)'], res[station]
    X = pd.concat([x1, x2, x3], axis=1)
    model_X = linear_model.LinearRegression(fit_intercept=True).fit(X, y)
    r = model_X.score(X, y)
    return ((model_X.coef_), r)

# model solution
# def cycling_weather_continues(station):
#     df = cycling_weather()
#     df = df.fillna(method='ffill')
#     X = df[['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
#     y = df[station]
#     reg = LinearRegression()
#     reg.fit(X, y)
#     score = reg.score(X, y)
#     return reg.coef_, score


def main():
    station = 'Baana'  # Example station
    coefficients, score = cycling_weather_continues(station)

    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coefficients[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coefficients[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coefficients[2]:.1f}")
    print(f"Score: {score:.2f}")

if __name__ == "__main__":
    main()
