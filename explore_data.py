import pandas as pd

df = pd.read_csv("data_crime.csv")
print(f"loaded {len(df)} rows")
print(df.head())

df["outcome_status"] = df["outcome_status"].fillna("unknown")
df["persistent_id"] = df["persistent_id"].fillna("unknown")

print(df.isnull().sum())
df.to_csv("data_crime.csv",index=False)

