import pandas as pd
import numpy as np
import statistics
import os
import matplotlib.pyplot as plt

# Load daily percentiles file
data_df = pd.read_csv("/home/dchanci/Acuity/Data/Bad_days/daily_percentiles.csv")
data_df['MEASUREMENT_TAKEN_DTM'] = pd.to_datetime(data_df['MEASUREMENT_TAKEN_DTM']).dt.floor('d')

# Drop columns
data_df = data_df.drop(['MEASUREMENT_TAKEN_DTM'], axis=1)

for col in data_df.columns:

    avg_list = []
    plt.figure()

    for day in list(data_df[col]):

        try:
            y_axis = np.sort([float(x) for x in day.strip('][').split(', ')])
            avg_list.append(y_axis)
            plt.plot(y_axis)
            plt.xlabel("Index")
            plt.ylabel("Percentile")
            plt.title(col)
            plt.savefig(os.path.join('/home/dchanci/Acuity/Data/Bad_days/Plots_perc', col + '.png'))
        
        except:
            pass

    plt.figure()
    plt.plot(np.mean(np.array(avg_list), axis=0))
    plt.xlabel("Index")
    plt.ylabel("Percentile")
    plt.title(col + 'AVG')
    plt.savefig(os.path.join('/home/dchanci/Acuity/Data/Bad_days/Plots_perc', col + '_AVG' + '.png'))