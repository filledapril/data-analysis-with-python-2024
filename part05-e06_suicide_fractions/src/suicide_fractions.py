#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    data = pd.read_csv("src/who_suicide_statistics.csv")
    data.drop(['year','sex','age'],axis = 1,inplace=True)
    data['fraction'] = data['suicides_no'] / data['population']
    group = data.groupby('country')
    print(group.get_group("United States of America"))
    result = group['fraction'].mean()
    return result

# model solution
# def suicide_fractions():
#     df = pd.read_csv("src/who_suicide_statistics.csv")
#     df["Suicide fraction"] = df["suicides_no"] / df["population"]
#     result = df.groupby("country").mean()
#     return result["Suicide fraction"]

def main():
    suicide_fractions()

if __name__ == "__main__":
    main()
