import snowfall
from traffic import traffic_data

import pandas as pd

def get_traffic_cost(location, time):
    location_df = traffic_data[traffic_data['location'] == location]
    df = location_df[location_df['time'] == time]

    delay = df['delay'].astype(int).iloc[0]

    if delay < 5:
        return 0
    elif delay < 15:
        return 4
    elif delay < 30:
        return 12
    elif delay < 60:
        return 20
    elif delay < 90:
        return 30
    else:
        return 50

def get_snowfall_cost(resort):
    df = snowfall.df[snowfall.df['title_short'] == resort]
    snowfall_24hr = df['snow'].tolist()[0]['last24']
    
    if snowfall_24hr == 0:
        return 50
    elif snowfall_24hr < 2:
        return 20
    elif snowfall_24hr < 4:
        return 10
    elif snowfall_24hr < 6:
        return 5
    elif snowfall_24hr < 10:
        return 2
    else:
        return 0

print("the cost of going down I-70 at 7:00AM is", get_traffic_cost("I-70", "07:00AM"))
print("the cost of going to Arapahoe Basin is", get_snowfall_cost("Arapahoe Basin"))