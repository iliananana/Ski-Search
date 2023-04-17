import snowfall
from traffic import traffic_data

import pandas as pd

ski_resorts = snowfall.df['title_short'].tolist()

def get_traffic_cost(location):
    location_df = traffic_data[traffic_data['location'] == location]
    delay = location_df['delay'].astype(int).iloc[0]

    crash = False
    cost = 0

    if (location == 'I-70mm_50'):
        crash = True
        cost += 100

    if delay < 5:
        cost += 0
    elif delay < 15:
        cost += 4
    elif delay < 30:
        cost += 12
    elif delay < 60:
        cost += 20
    elif delay < 90:
        cost += 30
    else:
        cost += 50
    
    return cost

def get_snowfall_cost(resort):
    df = snowfall.df[snowfall.df['title_short'] == resort]
    snowfall_24hr = df['snow'].tolist()[0]['last24']

    cost = 0
    
    if snowfall_24hr == 0:
        cost += 50
    elif snowfall_24hr < 2:
        cost += 20
    elif snowfall_24hr < 4:
        cost += 10
    elif snowfall_24hr < 6:
        cost += 5
    elif snowfall_24hr < 10:
        cost += 2
    else:
        cost += 0
    
    return cost

def get_heuristic(x, y):
    if x in ski_resorts:
        x_cost = get_snowfall_cost(x)
    else:
        x_cost = get_traffic_cost(x)
    
    if y in ski_resorts:
        y_cost = get_snowfall_cost(y)
    else:
        y_cost = get_traffic_cost(y)
    
    return x_cost + y_cost


def get_cost(x):
    if x == 'Colorado State University':
        x_cost = 0
    elif x in ski_resorts:
        x_cost = get_snowfall_cost(x)
    else:
        x_cost = get_traffic_cost(x)
    return x_cost

print('the heuristic of to Arapahoe Basin from I-70mm_10 is', get_heuristic('Arapahoe Basin', 'I-70mm_10'))
print('the cost of I-25mm_50 is', get_cost('I-25mm_50'))
print('the cost of Colorado State University is', get_cost('Colorado State University'))