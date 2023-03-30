import json
import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.onthesnow.com/colorado/skireport"

soup = BeautifulSoup(requests.get(url).content, "html.parser")

data = json.loads(soup.select_one("#__NEXT_DATA__").text)
resorts = data["props"]["pageProps"]["resorts"]["1"]["data"]
df = pd.DataFrame(resorts)
# print(df.to_markdown(index=False))
# print
df