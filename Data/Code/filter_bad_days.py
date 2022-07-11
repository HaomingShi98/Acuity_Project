"""
Filters the vital signs for the bad days only.
"""

import pandas as pd
import numpy as np
import os

days_list = ['2021-01-07', '2021-02-19', '2021-03-02', '2021-05-14', '2021-06-11', '2020-08-02', '2020-08-04', '2020-08-28', '2020-11-02', '2020-11-25', '2020-12-09']

"""
No observations for 2021-05-14
"""

# Load vital signs file
data_df = pd.read_csv("/home/dchanci/Acuity/Data/Vital_Signs.csv")
data_df['MEASUREMENT_TAKEN_DTM'] = pd.to_datetime(data_df['MEASUREMENT_TAKEN_DTM']).dt.floor('d')

# Filter dates
data_df = data_df[data_df["MEASUREMENT_TAKEN_DTM"].isin(days_list)]

# Save file
data_df.to_csv("/home/dchanci/Acuity/Data/Bad_days/Vital_Signs_filtered.csv", index=False,)