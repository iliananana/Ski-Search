import pandas as pd

df_I25 = pd.DataFrame(
    {
    'date': ['3/29/23', '3/29/23', '3/29/23', '3/29/23', '3/29/23', '3/29/23'], 
    'location': ['I-25mm_10', 'I-25mm_20', 'I-25mm_30', 'I-25mm_40', 'I-25mm_50', 'I-25mm_60'],
    'direction': ['South', 'South', 'South', 'South', 'South', 'South',],
    'avg_speed': [70, 70, 50, 48, 41, 30],
    'delay': [0, 5, 12, 20, 22, 25] 
    }
)


df_I70 = pd.DataFrame(
    {
    'date': ['3/29/23', '3/29/23', '3/29/23', '3/29/23', '3/29/23', '3/29/23', '3/29/23', '3/29/23', '3/29/23', '3/29/23', '3/29/23', '3/29/23'], 
    'location': ['I-70mm_10', 'I-70mm_20', 'I-70mm_30', 'I-70mm_40', 'I-70mm_50', 'I-70mm_60', 'I-70mm_70', 'I-70mm_80', 'I-70mm_90', 'I-70mm_100', 'I-70mm_110', 'I-70mm_120'],
    'direction': ['West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West'],
    'avg_speed': [55, 49, 30, 32, 20, 20, 20, 30, 40, 40, 50, 50],
    'delay': [10, 14, 20, 24, 26, 26, 26, 22, 21, 15, 10, 5] 
    }
)

frames = [df_I25, df_I70]

traffic_data = pd.concat(frames).reset_index(drop=True)

traffic_data