import pandas as pd
import numpy as np

data = {
    'ID': list(range(1, 101)),
    'Value': [
        42.3, 17.8, 156.2, 8.9, 234.7, 73.4, 5.1, 312.6, 29.5, 106.8,
        48.2, 189.3, 14.7, 267.4, 92.1, 33.6, 178.9, 61.4, 7.2, 298.5,
        124.7, 39.8, 201.6, 55.9, 12.4, 245.3, 87.6, 22.1, 167.8, 103.5,
        68.9, 289.2, 45.7, 176.3, 54.2, 198.4, 36.9, 223.1, 79.8, 115.6,
        27.4, 256.8, 63.1, 143.9, 41.5, 192.7, 96.4, 19.2, 271.9, 83.3,
        58.6, 207.4, 31.8, 134.7, 71.9, 239.6, 49.3, 182.5, 104.8, 16.5,
        287.3, 92.7, 37.4, 165.9, 66.2, 214.8, 53.1, 128.6, 44.9, 199.7,
        78.5, 152.4, 23.8, 263.5, 61.8, 112.4, 34.7, 188.6, 97.3, 14.2,
        279.1, 85.4, 51.6, 173.2, 69.8, 227.9, 42.8, 136.5, 58.3, 194.7,
        76.9, 148.2, 29.1, 252.4, 64.7, 119.3, 38.6, 181.9, 94.5, 21.7
    ],
    'Category': [
        'A', 'B', 'C', 'A', 'C', 'B', 'A', 'C', 'B', 'A',
        'B', 'C', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C',
        'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C', 'B',
        'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A',
        'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B',
        'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C',
        'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A',
        'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B',
        'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C',
        'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'
    ]
}

df = pd.DataFrame(data)

original_mean = df['Value'].mean()
original_std = df['Value'].std()

df['Standardized'] = (df['Value'] - original_mean) / original_std
df['Standardized_Back'] = df['Standardized'] * original_std + original_mean

min_val = df['Value'].min()
max_val = df['Value'].max()
df['MinMax'] = (df['Value'] - min_val) / (max_val - min_val)
df['MinMax_Back'] = df['MinMax'] * (max_val - min_val) + min_val

q1 = df['Value'].quantile(0.25)
q3 = df['Value'].quantile(0.75)
iqr = q3 - q1
median = df['Value'].median()
df['Robust'] = (df['Value'] - median) / iqr
df['Robust_Back'] = df['Robust'] * iqr + median

print(df.head(10))
print(f"\nOriginal mean: {original_mean:.2f}")
print(f"Standardized back mean: {df['Standardized_Back'].mean():.2f}")
print(f"MinMax back mean: {df['MinMax_Back'].mean():.2f}")
print(f"Robust back mean: {df['Robust_Back'].mean():.2f}")