import pandas as pd
import numpy as np
students = [
    {"Student_ID": 1, "Name": "Ali",    "Math": 85, "Science": 90, "English": 78, "Attendance": 95},
    {"Student_ID": 2, "Name": "Sara",   "Math": 88, "Science": None, "English": 82, "Attendance": 92},
    {"Student_ID": 3, "Name": "Omar",   "Math": 70, "Science": 75, "English": None, "Attendance": 88},
    {"Student_ID": 4, "Name": "Lina",   "Math": None, "Science": 85, "English": 80, "Attendance": None},
    {"Student_ID": 5, "Name": "Hassan", "Math": 90, "Science": 92, "English": 89, "Attendance": 97},
    {"Student_ID": 6, "Name": "Noura",  "Math": 78, "Science": None, "English": 75, "Attendance": 90},
    {"Student_ID": 7, "Name": "Yousef", "Math": None, "Science": 70, "English": 68, "Attendance": 85},
    {"Student_ID": 8, "Name": "Maha",   "Math": 95, "Science": 98, "English": None, "Attendance": 99}
]
df = pd.DataFrame(students)

mean_values = df[['Math', 'Science', 'English', 'Attendance']].mean()
median_values = df[['Math', 'Science', 'English', 'Attendance']].median()
mode_values = df[['Math', 'Science', 'English', 'Attendance']].mode().iloc[0]

df_filled = df.copy()
for column in ['Math', 'Science', 'English', 'Attendance']:
    df_filled[column] = df_filled[column].fillna(df_filled[column].mean())

mean_filled = df_filled[['Math', 'Science', 'English', 'Attendance']].mean()
median_filled = df_filled[['Math', 'Science', 'English', 'Attendance']].median()
mode_filled = df_filled[['Math', 'Science', 'English', 'Attendance']].mode().iloc[0]

print(mean_values)
print(median_values)
print(mode_values)
print(mean_filled)
print(median_filled)
print(mode_filled)
