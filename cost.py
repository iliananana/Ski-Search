import snowfall
from traffic import traffic_data
import ast

import pandas as pd
snow_df = pd.read_csv("Ski-Search/3-21-snowreport.csv")

def get_traffic_cost(location):
    location_df = traffic_data[traffic_data['location'] == location]
    delay = location_df['delay'].astype(int).iloc[0]

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
    df = snow_df[snow_df['title_short'] == resort]
    snowfall_24hr = df['snow'][0]
    snowfall_24hr = ast.literal_eval(snowfall_24hr)['last24']
    
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

def get_heuristic(x, y):
    if x in snowfall.df['title_short'].tolist():
        x_cost = get_snowfall_cost(x)
    else:
        x_cost = get_traffic_cost(x)
    
    if y in snowfall.df['title_short'].tolist():
        y_cost = get_snowfall_cost(y)
    else:
        y_cost = get_traffic_cost(y)
    
    return x_cost + y_cost


def get_cost(x):
    if x == 'Colorado State University':
        x_cost = 0
    elif x in snowfall.df['title_short'].tolist():
        x_cost = get_snowfall_cost(x)
    else:
        x_cost = get_traffic_cost(x)
    return x_cost

print('the heuristic of to Arapahoe Basin from I-70mm_10 is', get_heuristic('Arapahoe Basin', 'I-70mm_10'))
print('the cost of I-25mm_50 is', get_cost('I-25mm_50'))
print('the cost of Colorado State University is', get_cost('Colorado State University'))