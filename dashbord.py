import streamlit as st
import pandas as pd
import ast


st.title("London Crime Dashbord")
df = pd.read_csv("data_crime.csv")

st.metric("total crimes", len(df))
crime_counts = df["category"].value_counts()
st.bar_chart(crime_counts)
print(df["location"].head())

df["lat"] =df["location"].apply(lambda x: float(ast.literal_eval(x)["latitude"]))
df["lon"] =df["location"].apply(lambda x: float(ast.literal_eval(x)["longitude"]))
st.map(df, latitude="lat", longitude="lon", zoom=10)

#print(df["lat"].head())
#print(df["lon"].head())