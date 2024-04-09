#!/usr/bin/env python3

import pandas as pd
import numpy as np
import re


def cleaning_data():
    word_to_int = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    def convert_season_to_int(season_word):
        try:
            return word_to_int[season_word]
        except KeyError:
            return season_word
    cleaned_data = pd.DataFrame()
    data = pd.read_csv("src/presidents.tsv", sep="\t")
    print(data)
    cleaned_data["President"] = data["President"].apply(lambda x: ' '.join([name.strip() for name in x.split(",")[::-1]]))
    cleaned_data["Start"] = data["Start"].str.extract(r'(\d{4})').astype(int)
    cleaned_data["Last"] = data["Last"].str.extract(r'(\d{4})').astype(float)
    cleaned_data["Seasons"] = data["Seasons"].apply(lambda x: convert_season_to_int(x)).astype(int)
    cleaned_data["Vice-president"] = data["Vice-president"].apply(lambda x: ' '.join([word.strip().capitalize() for word in x.split(",")[::-1]])).apply(lambda x: ' '.join([word.strip().capitalize() for word in x.split(" ")]))
    cleaned_data = cleaned_data.replace('', np.nan)

    return cleaned_data

def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()
