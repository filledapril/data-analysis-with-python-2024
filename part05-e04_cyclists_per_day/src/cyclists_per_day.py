#!/usr/bin/env python3

# import pandas as pd
# import matplotlib.pyplot as plt

# def split_date(df):
#     date = df["Päivämäärä"].str.split(expand=True)
#     date[[4,5]] = date[4].str.split(":",expand=True)
#     date = date.drop(5,axis=1)
#     date = date.dropna()
#     date = date.rename(columns={0:"Weekday",1:"Day",2:"Month",3:"Year",4:"Hour"})
#     date = date.drop(["Weekday", "Hour"], axis=1)
#     # weekdayDic = {"ma":"Mon","ti":"Tue","ke":"Wed","to":"Thu","pe":"Fri","la":"Sat","su":"Sun"}
#     monthDic = {"tammi":1,"helmi":2,"maalis":3,"huhti":4,"touko":5,"kesä":6,"heinä":7,"elo":8,
#                 "syys":9,"loka":10,"marras":11,"joulu":12}
#     # date['Weekday'] = date["Weekday"].map(weekdayDic)
#     date['Month'] = date["Month"].map(monthDic).map(int)
#     date[['Day','Year']] = date[['Day','Year']].astype(int)
#     print(date)
#     print(date.dtypes)
#     return date


# def cyclists_per_day():
#     data = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
#     # clean and parse the bicycle data set 
#     data = data.dropna(axis=1, how='all').dropna(axis=0, how='all')
#     date = split_date(data)
#     data = data.drop("Päivämäärä", axis=1)
#     data = pd.concat([date, data], axis=1)
#     grouped_data = data.groupby(["Year", "Month", "Day"]).sum().reset_index() 
#     print(grouped_data)
#     grouped_data = grouped_data.drop(columns=['Year', 'Month', 'Day'])
#     return grouped_data
    
# def main():
#     # Get the daily counts
#     daily_counts = cyclists_per_day()

#     # Plot the data
#     plt.figure(figsize=(10, 6))
#     for column in daily_counts.columns:
#         plt.plot(daily_counts.index, daily_counts[column], label=column)

#     # Add labels and title
#     plt.xlabel('Day')
#     plt.ylabel('Daily Counts')
#     plt.title('Daily Bicycle Counts')

#     # Add legend
#     plt.legend()

#     # Show the plot
#     plt.show()

import pandas as pd
import matplotlib.pyplot as plt

def split_date():
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
    date['Month'] = date["Month"].map(monthDic).astype(int)
    date[['Day','Year','Hour']] = date[['Day','Year','Hour']].astype(int)
    # print(date)
    # print(date.dtypes)
    return date,df

def split_date_continues():
    date,df = split_date()
    df.dropna(axis=0,how="all",inplace=True)
    df.dropna(axis=1,how="all",inplace=True)
    df.drop(["Päivämäärä"],axis=1,inplace=True)
    # print(df)
    result = pd.concat([date,df],axis=1)
    # result["Weekday"] = result["Weekday"].astype(object)
    #print(result)
    return result

def cyclists_per_day():
    df = split_date_continues()
    df.drop(['Weekday', 'Hour'],axis=1,inplace=True)
    result = df.groupby(['Year','Month','Day']).sum()
    return result
    
def main():
    data = cyclists_per_day().loc[(2017,8),:]
    print(data)
    data.plot()
    plt.show()
    return


if __name__ == '__main__':
    main()
