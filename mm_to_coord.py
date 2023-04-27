import snowfall
import pandas as pd

resorts = {'resorts': snowfall.march_resorts_list}

resort_coords = pd.DataFrame(resorts)

resort_coords_list = [(39.6425, -105.8717),
                (39.6042, -106.5165),                
                (39.4817, -106.0384),                
                (39.5022, -106.1512),                
                (39.9386, -105.5828),                
                (39.6056, -105.9544),                
                (39.6809, -105.8975),                
                (39.6403, -106.3742),                
                (39.8885, -105.7631)]

resort_coords["coordinates"] = resort_coords_list