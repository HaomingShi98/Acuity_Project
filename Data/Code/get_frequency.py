import pandas as pd
import numpy as np
import os

# Load vital signs file
data_df = pd.read_csv("/home/dchanci/Acuity/Data/Vital_Signs.csv")
data_df['MEASUREMENT_TAKEN_DTM'] = pd.to_datetime(data_df['MEASUREMENT_TAKEN_DTM']).dt.floor('d')

# Drop columns
data_df = data_df.drop(['KIDS_VISIT_ID'], axis=1)

# Convert to booleans based on Nan
bool_df = pd.notna(data_df)
bool_df['MEASUREMENT_TAKEN_DTM'] = data_df['MEASUREMENT_TAKEN_DTM']

# Find daily frequency
bool_df = bool_df.groupby('MEASUREMENT_TAKEN_DTM').sum()

# Save file
bool_df.to_csv("/home/dchanci/Acuity/Data/Processed/daily_freqs.csv", index=True,)

