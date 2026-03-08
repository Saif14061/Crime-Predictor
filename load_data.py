import requests
import pandas as pd
print("Application Started")

url = "https://data.police.uk/api/crimes-street/all-crime?lat=51.5074&lng=-0.1278&date=2024-01"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
row_count = len(df)
print(f"loaded {row_count} crimes")

df.to_csv('data_crime.csv', index=False)
print("Data Saved")