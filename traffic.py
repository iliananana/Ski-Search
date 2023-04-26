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

mile_markers["coordinates"] = [(440.574142, -105.083542), # Fort Collins1
                     (40.524524, -104.990723), # Timnath - 8.7
                     (40.400984, -104.993505), # Johnstown
                     (40.278231, -104.980678), # Berthoud
                     (40.152524, -104.979294), # weld county
                     (40.027856, -104.980411), # broom field
                     (39.903807, -104.990085), # north glen  
                     (39.800740, -105.030046), # Berkley 
                     (39.745779, -105.151682), # Apple wood west
                     (39.707060, -105.279514), # mnt vernon
                     (39.730882, -105.425882), # clear creek county
                     (39.757728, -105.567318), #  idaho springs
                     (39.717682, -105.696525), #  georgetown
                     (39.699918, -105.837528),  #  # clear creek county
                     (39.673378, -105.969523), #  summit county
                     (39.591038, -106.100264), # frisco
                     (39.502069, -106.165791), # copper
                     (39.613744, -106.279037)]# vail