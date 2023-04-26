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

mile_markers = traffic_data.loc[:, ['location']]

mile_markers["coordinates"] = [(40.5853, -105.0844), # Fort Collins1
                     (40.3978, -105.0746), # Loveland2
                     (40.3111, -105.0779), # Berthoud3
                     (40.1672, -105.1019), # Longmont4
                     (40.0149, -105.2705), # Boulder5
                     (39.7555, -105.2211), # Golden6
                     (39.7416, -105.5136), # Idaho Springs7
                     (39.7042, -105.6969), # Georgetown8
                     (39.5734, -106.0941), # Frisco9
                     (39.6403, -106.3742), # Vail10
                     (39.6442, -106.5947), # Avon 11
                     (39.6519, -106.8151), # Eagle 12
                     (39.6456, -106.9536), # Canyon 14
                     (39.6558, -107.038),  # Glenwood 15
                     (39.5505, -107.3248), # Carbondale 16
                     (39.4022, -107.2176), # Basalt17
                     (39.3636, -107.0312), # Dotsero
                     (39.1911, -106.8188)]# Aspen
mile_markers