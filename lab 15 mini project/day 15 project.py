import pandas as pd
import numpy as np
from datetime import datetime
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
df = pd.read_csv('day 15 project dataset.csv')
numeric_cols = ['age', 'salary', 'quantity', 'total_amount', 'discount_percent',
                'customer_score', 'transaction_count']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
status_mapping = {'ACTIVE': True, 'SUSPENDED': False, 'PENDING': False,
                  'INACTIVE': False, 'UNKNOWN': False}
df['account_status'] = df['account_status'].map(status_mapping).astype('boolean')
date_cols = ['registration_date', 'last_login_date', 'order_date_time']
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce', utc=True)
cat_cols = ['city', 'country', 'subscription_tier', 'payment_method',
            'product_category', 'browser_type', 'device_type']
for col in cat_cols:
    df[col] = df[col].astype('category')
for col in ['age', 'salary', 'customer_score']:
    df[col] = df[col].fillna(df[col].median())
df['transaction_count'] = df['transaction_count'].fillna(0)
df['total_amount'] = df['total_amount'].fillna(0)
df['quantity'] = df['quantity'].fillna(0)
for col in cat_cols:
    df[col] = df[col].cat.add_categories(['Missing']).fillna('Missing')
df['account_status'] = df['account_status'].fillna(False)
far_past = pd.Timestamp('1900-01-01', tz='UTC')
for col in date_cols:
    df[col] = df[col].fillna(far_past)
for col in ['age', 'salary', 'total_amount', 'customer_score', 'transaction_count']:
    lower = df[col].quantile(0.01)
    upper = df[col].quantile(0.99)
    df[col] = np.where(df[col] < lower, lower, df[col])
    df[col] = np.where(df[col] > upper, upper, df[col])
df['city'] = df['city'].str.strip().str.title()
df['country'] = df['country'].str.strip().str.upper()
df['customer_name'] = df['customer_name'].str.strip().str.title()
for col in date_cols:
    if df[col].dt.tz is None:
        df[col] = df[col].dt.tz_localize('UTC')
df['phone_number'] = df['phone_number'].astype(str).str.replace(r'[^\d\+\-]', '', regex=True)
df['email_address'] = df['email_address'].str.lower().str.strip()
numeric_summary = df[numeric_cols].describe()
logger.info(f"Numeric summary stats:\n{numeric_summary}")
for col in cat_cols:
    dist = df[col].value_counts()
    logger.info(f"Category distribution for {col}:\n{dist.head(10)}")
for col in date_cols:
    logger.info(f"{col} timezone: {df[col].dt.tz}")
critical_cols = ['user_id', 'customer_name', 'age', 'salary', 'account_status']
missing_critical = df[critical_cols].isnull().sum()
logger.info(f"Missing values in critical columns:\n{missing_critical}")
dtype_check = df.dtypes
logger.info(f"Final dtypes:\n{dtype_check}")