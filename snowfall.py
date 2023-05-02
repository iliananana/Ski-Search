import json
import requests
import ast
import pandas as pd
from bs4 import BeautifulSoup

# For scraping snow data from On the Snow
url = "https://www.onthesnow.com/colorado/skireport"

soup = BeautifulSoup(requests.get(url).content, "html.parser")

data = json.loads(soup.select_one("#__NEXT_DATA__").text)
OTS_resorts = data["props"]["pageProps"]["resorts"]["1"]["data"]
OTS_df = pd.DataFrame(OTS_resorts)

# For out of season data from march 31st
march_df = pd.read_csv("Ski-Search/3-21-ikon-snowreport.csv")
march_resorts = march_df['title_short']
march_resorts_list = list(march_resorts)

snowfall_24hr = march_resorts_list
snowfall_24hr = march_df['snow']
snowfall_24hr = snowfall_24hr.apply(ast.literal_eval)
last24_values_df = snowfall_24hr.apply(lambda x: x['last24'])
last24_values_list = last24_values_df.tolist()


