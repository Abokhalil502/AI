"""
Day 11 Activity: Outlier Strategies
Tasks:
1) Load numeric data with outliers
2) Implement percentile capping (winsorization)
3) Implement removal strategy
4) Compare summary stats before/after
"""

import pandas as pd
import numpy as np

df = pd.read_csv('day11_income.csv')

def winsorize_series(s, lower_q, upper_q):
    lower_bound = s.quantile(lower_q)
    upper_bound = s.quantile(upper_q)
    return s.clip(lower=lower_bound, upper=upper_bound)

def remove_upper_tail(s, upper_q):
    upper_bound = s.quantile(upper_q)
    return s[s <= upper_bound]

print("Original Data Summary:")
print(df['income'].describe())
print("\n" + "="*50 + "\n")

winsorized = winsorize_series(df['income'], 0.05, 0.95)
print("Winsorized Data (5th-95th percentile):")
print(winsorized.describe())
print("\n" + "="*50 + "\n")

removed = remove_upper_tail(df['income'], 0.95)
print("Removed Upper Tail (95th percentile):")
print(removed.describe())
