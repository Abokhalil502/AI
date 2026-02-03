"""
Day 12 Activity: String & Date Cleaning
Tasks:
1) Clean city strings (strip, lower, remove punctuation)
2) Map synonyms to canonical values
3) Parse mixed-format timestamps and localize to UTC
"""

import pandas as pd
import string

df = pd.read_csv('day12_users.csv')

city_mapping = {
    'nyc': 'new york',
    'san francisco': 'san francisco'
}

def standardize_city(df):
    df['city_clean'] = df['city'].str.strip().str.lower()
    df['city_clean'] = df['city_clean'].str.translate(str.maketrans('', '', string.punctuation))
    df['city_clean'] = df['city_clean'].map(lambda x: city_mapping.get(x, x))
    return df

def parse_and_localize(df):
    def parse_timestamp(ts):
        if pd.isna(ts) or ts == 'not a date':
            return pd.NaT
        formats = ['%Y-%m-%d %H:%M', '%m/%d/%Y %H:%M', '%Y/%m/%d']
        for fmt in formats:
            try:
                return pd.to_datetime(ts, format=fmt)
            except:
                continue
        return pd.NaT
    
    df['signup_time_utc'] = df['signup_time'].apply(parse_timestamp)
    return df

df = standardize_city(df)
df = parse_and_localize(df)

print(df[['city', 'city_clean']])
print("\n")
print(df[['signup_time', 'signup_time_utc']])
