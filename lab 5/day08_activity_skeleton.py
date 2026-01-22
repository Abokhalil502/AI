import pandas as pd

df = pd.read_csv('day08_events.csv')

df = df.drop_duplicates()

df = df.drop_duplicates(subset=['user', 'day', 'product'])

user_agg = df.groupby('user').agg(
    event_count=('user', 'size'),
    ever_clicked=('clicked', 'max')
).reset_index()

print(user_agg)
