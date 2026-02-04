import pandas as pd
import numpy as np
df = pd.read_csv("day14_users_raw.csv")
def clean_types(df):
    out = df.copy()
    out["age"] = pd.to_numeric(out["age"], errors="coerce")
    out["income"] = pd.to_numeric(out["income"], errors="coerce")
    return out
def clean_missing(df):
    out = df.copy()
    out["age"] = out["age"].fillna(out["age"].median())
    out["income"] = out["income"].fillna(out["income"].median())
    if "gender" in out.columns:
        out["gender"] = out["gender"].fillna(out["gender"].mode()[0])
    return out
def handle_outliers(df):
    out = df.copy()
    for col in ["age", "income"]:
        Q1 = out[col].quantile(0.25)
        Q3 = out[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        out[col] = out[col].clip(lower, upper)
    return out
def clean_strings_and_dates(df):
    out = df.copy()
    for col in out.select_dtypes(include="object").columns:
        out[col] = out[col].str.strip().str.lower()
    if "signup_time" in out.columns:
        out["signup_time"] = pd.to_datetime(out["signup_time"], errors="coerce")
    return out
def validate_cleaned(df):
    assert df["age"].min() >= 0
    assert df["income"].min() >= 0
def clean_data(df):
    df = clean_types(df)
    df = clean_missing(df)
    df = handle_outliers(df)
    df = clean_strings_and_dates(df)
    validate_cleaned(df)
    return df
cleaned_df = clean_data(df)
