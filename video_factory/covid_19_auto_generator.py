import pandas as pd
import bar_chart_race as bcr
import requests
import matplotlib.pyplot as plt

# covid-19 real updated data
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'

# read data into DataFrame
df =pd.read_csv(url, sep=",")[["location", "date", "total_cases"]]

# remove World and International data
dff = df[df["location"]!="World"]
dff = dff[dff["location"]!="International"]

# fetch last date top 100 locations
max_date = dff["date"].max()
top_30= dff[dff["date"]==max_date].nlargest(30, 'total_cases')["location"].to_numpy()

# screen top 30 countries, no need to play the rest countries
dff = dff[dff["location"].isin(top_30)]

# pivot data
dff_ = pd.pivot_table(dff, values=["total_cases"] ,index=["date"], columns=["location"], dropna=False, fill_value=0)

# replace tuple column names into string
dff_.columns = [(k) for (j,k) in dff_.columns]

# save video mp4 file
bcr.bar_chart_race(dff_, 'covid_19.mp4', figsize=(10, 6), title=f"COVID-19 Total Cases by Country up to {max_date}", n_bars=15, filter_column_colors=True)
