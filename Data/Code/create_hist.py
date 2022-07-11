import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Load vital signs file
data_df = pd.read_csv("/home/dchanci/Acuity/Data/Bad_days/Vital_Signs_filtered.csv")
data_df['MEASUREMENT_TAKEN_DTM'] = pd.to_datetime(data_df['MEASUREMENT_TAKEN_DTM']).dt.year

years = list(set(list(data_df['MEASUREMENT_TAKEN_DTM'])))

for year in years:
    data = data_df[data_df['MEASUREMENT_TAKEN_DTM'] == year].drop(['KIDS_VISIT_ID', 'MEASUREMENT_TAKEN_DTM', 'PAIN_SCALE', 'PAIN_INTENSITY_RATING', 'CRS_LOC_TYPE', 'OXYGEN_MODE'], axis=1)
    
    for col in data.columns:
        values = np.sort(list(data.loc[pd.notna(data[col]), col]))

        plt.figure()
        plt.hist(values, bins='auto', rwidth=0.9, color='lightsteelblue')
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.title(col)
        plt.savefig(os.path.join('/home/dchanci/Acuity/Data/Bad_days/Histograms', str(year), col + '.png'))
    