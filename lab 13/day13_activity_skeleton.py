import os
import pandas as pd
import time
def clean_chunk(df):
	df = df.copy()
	if 'city' in df.columns:
		df['city'] = df['city'].astype(str).str.strip()
		df['city'] = df['city'].replace({'': pd.NA, 'nan': pd.NA})
	for col in ('age', 'income'):
		if col in df.columns:
			df[col] = pd.to_numeric(df[col], errors='coerce')
	df = df.replace({pd.NA: None})
	df = df.dropna(how='all')
	return df
def process_large_file(path_in, path_out, chunksize=10000):
	if os.path.exists(path_out):
		os.remove(path_out)
	start = time.time()
	total_in = 0
	total_out = 0
	for i, chunk in enumerate(pd.read_csv(path_in, chunksize=chunksize)):
		cleaned = clean_chunk(chunk)
		cleaned.to_csv(path_out, index=False, mode='w' if i == 0 else 'a', header=(i == 0))
		total_in += len(chunk)
		total_out += len(cleaned)
	elapsed = time.time() - start
	return {'input_rows': total_in, 'cleaned_rows': total_out, 'elapsed_seconds': elapsed}
if __name__ == '__main__':
	metrics = process_large_file('day13_large_users.csv', 'day13_large_users_cleaned.csv', chunksize=5000)
	print(metrics)
