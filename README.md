██╗      ██████╗ ███╗   ██╗██████╗  ██████╗ ███╗   ██╗
██║     ██╔═══██╗████╗  ██║██╔══██╗██╔═══██╗████╗  ██║
██║     ██║   ██║██╔██╗ ██║██║  ██║██║   ██║██╔██╗ ██║
██║     ██║   ██║██║╚██╗██║██║  ██║██║   ██║██║╚██╗██║
███████╗╚██████╔╝██║ ╚████║██████╔╝╚██████╔╝██║ ╚████║
╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝

 ██████╗██████╗ ██╗███╗   ███╗███████╗
██╔════╝██╔══██╗██║████╗ ████║██╔════╝
██║     ██████╔╝██║██╔████╔██║█████╗  
██║     ██╔══██╗██║██║╚██╔╝██║██╔══╝  
╚██████╗██║  ██║██║██║ ╚═╝ ██║███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝

██████╗ ██████╗ ███████╗██████╗ ██╗ ██████╗████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔══██╗██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝██████╔╝█████╗  ██║  ██║██║██║        ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██╗██╔══╝  ██║  ██║██║██║        ██║   ██║   ██║██╔══██╗
██║     ██║  ██║███████╗██████╔╝██║╚██████╗   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

## 📌 Overview
A data science web application that analyses real London crime data from the UK Police API, visualises crime trends across the city, and uses machine learning to predict future crime rates. Built entirely in Python.

## 🛠️ Tech Stack
- **Python** — core programming language
- **Pandas** — data cleaning and analysis
- **Scikit-learn** — machine learning (Linear Regression)
- **Streamlit** — interactive web dashboard
- **Matplotlib/Plotly** — data visualisation
- **UK Police API** — real government crime data

## 🔍 Features
- ✅ Fetches real-time crime data from the UK Police open data API
- ✅ Cleans and processes raw data using Pandas
- ✅ Interactive crime map of London showing exact crime locations
- ✅ Bar chart visualising crime categories across the city
- ✅ ML model predicting next month's expected crime rate
- ✅ Clean, interactive web dashboard built with Streamlit



## 📁 Project Structure
```
crime-predictor/
├── load_data.py       # Fetches crime data from UK Police API
├── explore_data.py    # Cleans and analyses the data
├── predict.py         # ML model for crime prediction
├── dashbord.py        # Streamlit web dashboard
└── data_crime.csv     # Processed crime dataset
```

## 📊 Data Source
Real crime data sourced from the **UK Police open data API** — [data.police.uk](https://data.police.uk). Covers crimes reported in Central London (Westminster area) for January 2024, totalling **6,791 recorded crimes**.

## 💡 Key Insights
- **Theft from the person** is the most common crime with 2,546 incidents
- The majority of crimes are concentrated in **Central London / Westminster**
- The ML model uses Linear Regression to forecast future crime trends
