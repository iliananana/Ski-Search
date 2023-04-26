import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

# For scraping snow data from On the Snow
url = "https://www.onthesnow.com/colorado/skireport"

soup = BeautifulSoup(requests.get(url).content, "html.parser")

data = json.loads(soup.select_one("#__NEXT_DATA__").text)
OTS_resorts = data["props"]["pageProps"]["resorts"]["1"]["data"]
OTS_df = pd.DataFrame(OTS_resorts)

# For out of season data from march 31st
march_df = pd.read_csv("Ski-Search/3-21-snowreport.csv")
march_resorts = march_df['title_short']
march_resorts_list = list(march_resorts)