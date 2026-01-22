import pandas as pd
df = pd.read_csv('day09_schema_raw.csv')

def normalize_schema(df):
    df = df.copy()
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['income'] = df['income'].str.replace('$', '').str.replace(',', '').astype(float)
    df['signup'] = pd.to_datetime(df['signup'], errors='coerce')
    return df

df = normalize_schema(df)
print(df.isna().sum())
