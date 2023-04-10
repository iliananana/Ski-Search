import pandas as pd

df_I25 = pd.DataFrame(
    {
    'date': ['3/29/23', '3/29/23', '3/29/23', '3/29/23', '3/29/23', '3/29/23'], 
    'time': ['06:00AM', '06:30AM', '07:00AM', '07:30AM', '08:00AM', '08:30AM'],
    'location': ['I-25', 'I-25', 'I-25', 'I-25', 'I-25', 'I-25'],
    'direction': ['South', 'South', 'South', 'South', 'South', 'South',],
    'avg_speed': [70, 70, 50, 48, 41, 30],
    'delay': [0, 5, 12, 20, 22, 25] 
    }
)


df_I70 = pd.DataFrame(
    {
    'date': ['3/29/23', '3/29/23', '3/29/23', '3/29/23', '3/29/23', '3/29/23'], 
    'time': ['06:00AM', '06:30AM', '07:00AM', '07:30AM', '08:00AM', '08:30AM'],
    'location': ['I-70', 'I-70', 'I-70', 'I-70', 'I-70', 'I-70'],
    'direction': ['West', 'West', 'West', 'West', 'West', 'West'],
    'avg_speed': [55, 49, 30, 32, 20, 20],
    'delay': [10, 14, 20, 24, 26, 26] 
    }
)

frames = [df_I25, df_I70]

traffic_data = pd.concat(frames).reset_index(drop=True)

traffic_data