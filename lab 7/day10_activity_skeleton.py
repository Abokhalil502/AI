import numpy as np
import pandas as pd
df = pd.read_csv('day10_outliers.csv')
def iqr_bounds(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return lower, upper
def detect_outliers_iqr(data):
    lower, upper = iqr_bounds(data)
    return (data < lower) | (data > upper)
def detect_outliers_zscore(data, threshold=3):
    mean = np.mean(data)
    std = np.std(data)
    z_scores = (data - mean) / std
    return np.abs(z_scores) > threshold
lower, upper = iqr_bounds(df['income'])
df['income_capped'] = np.clip(df['income'], lower, upper)
df['income_log'] = np.log1p(df['income'])
print("Original:")
print(f"Mean: {df['income'].mean():.2f}")
print(f"Std: {df['income'].std():.2f}")
print(f"Min: {df['income'].min():.2f}")
print(f"Max: {df['income'].max():.2f}")
print("\nIQR Capped:")
print(f"Mean: {df['income_capped'].mean():.2f}")
print(f"Std: {df['income_capped'].std():.2f}")
print(f"Min: {df['income_capped'].min():.2f}")
print(f"Max: {df['income_capped'].max():.2f}")
print("\nLog1p Transform:")
print(f"Mean: {df['income_log'].mean():.2f}")
print(f"Std: {df['income_log'].std():.2f}")
print(f"Min: {df['income_log'].min():.2f}")
print(f"Max: {df['income_log'].max():.2f}")
