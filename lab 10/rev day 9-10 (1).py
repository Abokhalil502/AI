import pandas as pd
import numpy as np
normal_sales = np.array([450.2, 520.7, 510.3, 480.9, 530.1, 490.8, 470.5, 495.2, 
                        501.8, 512.4, 488.3, 475.6, 523.9, 505.7, 498.4, 510.2, 
                        485.9, 495.3, 520.8, 507.6, 480.1, 530.5, 489.7, 475.3,
                        515.4, 502.9, 525.6, 495.1, 508.7, 480.4])
high_outliers = np.array([850.2, 920.5, 1100.8, 780.9, 950.3])
low_outliers = np.array([120.5, 80.3, 95.7, 150.2, 110.8])
sales_data = np.concatenate([normal_sales, high_outliers, low_outliers])
sales_df = pd.DataFrame({'daily_sales': sales_data})
Q1 = sales_df['daily_sales'].quantile(0.25)
Q3 = sales_df['daily_sales'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = sales_df[(sales_df['daily_sales'] < lower) | (sales_df['daily_sales'] > upper)]
clean = sales_df[(sales_df['daily_sales'] >= lower) & (sales_df['daily_sales'] <= upper)]
print("Outliers:", outliers['daily_sales'].values)
print("Clean data:", len(clean))