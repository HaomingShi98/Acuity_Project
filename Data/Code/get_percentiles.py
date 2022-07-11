import pandas as pd
import numpy as np
import statistics
import os

# Load vital signs file
data_df = pd.read_csv("/home/dchanci/Acuity/Data/Bad_days/Vital_Signs_filtered.csv")
data_df['MEASUREMENT_TAKEN_DTM'] = pd.to_datetime(data_df['MEASUREMENT_TAKEN_DTM']).dt.floor('d')

# Drop columns
data_df = data_df.drop(['KIDS_VISIT_ID', 'PAIN_SCALE', 'PAIN_INTENSITY_RATING', 'CRS_LOC_TYPE', 'OXYGEN_MODE'], axis=1)

# List of days
days_list = list(set(list(data_df['MEASUREMENT_TAKEN_DTM'])))

# Initialize list
full_list = []

# Loop through days
for day in days_list:

    row_list = [day]
    data = data_df[data_df['MEASUREMENT_TAKEN_DTM'] == day].drop(['MEASUREMENT_TAKEN_DTM'], axis=1)

    # Compute percentiles
    for col in data.columns:
        try:
            row_list.append([float(x) for x in statistics.quantiles(data.loc[pd.notna(data[col]), col], n=100, method='inclusive')])
        except:
            row_list.append([])
    full_list.append(row_list)

# Create final dataframe
per_df = df = pd.DataFrame(full_list)
per_df.columns = data_df.columns
per_df = per_df.sort_values(by=['MEASUREMENT_TAKEN_DTM'])

# Save file
per_df.to_csv("/home/dchanci/Acuity/Data/Bad_days/daily_percentiles.csv", index=False,)