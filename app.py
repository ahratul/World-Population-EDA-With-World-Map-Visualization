# Importing all essential liabraries
import numpy as np
import pandas as pd
import seaborn as sns
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import plotly.express as px
import missingno as msno
import streamlit as st

import warnings

warnings.filterwarnings('ignore')
data = pd.read_csv('world_population.csv')
data.describe().T.sort_values(ascending=0, by="mean").style.background_gradient(cmap="BuGn") \
    .bar(subset=["std"], color="red").bar(subset=["mean"], color="blue")
features = data.columns
for feature in features:
    print(f"{feature} ---> {data[feature].nunique()}")

data.isnull().sum()
msno.matrix(data)

data = pd.read_csv('world_population.csv')
data.head()
data.describe().T.sort_values(ascending=0, by="mean").style.background_gradient(cmap="BuGn") \
    .bar(subset=["std"], color="red").bar(subset=["mean"], color="blue")

# Getting all the unique values in each feature
features = data.columns
for feature in features:
    print(f"{feature} ---> {data[feature].nunique()}")

continent_data = data.groupby('Continent')[features].mean().sort_values(by="Density (per km²)", ascending=False)
continent_data.style.background_gradient(cmap="BuGn")
continent_data.sort_values(by='2022 Population', inplace=True)

population_features = ['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population',
                       '1990 Population', '1980 Population', '1970 Population']
population_features.reverse()

st.title('World-Population-EDA-With-World-Map-Visualization')
st.subheader('The data is from US Census Bureau. We are given the population of every countries from year 1970,1980,1990,2000,2010,2015,2020 and 2022. We are also given the Population Density, Area (km^2) of the country, Growth Rate, etc. We will perform EDA on the dataset and try to arrive on some interesting conclusions.')

st.markdown('2022 Population')
fig22 = px.choropleth(data,
                      locations='Country/Territory',
                      locationmode='country names',
                      color='2022 Population',  # we indicate the year we are interested in
                      hover_name='Country/Territory',
                      color_continuous_scale='Viridis'
                      )

st.write(fig22)

st.markdown('2020 Population')
fig20 = px.choropleth(data,
                      locations='Country/Territory',
                      locationmode='country names',
                      color='2020 Population',  # we indicate the year we are interested in
                      hover_name='Country/Territory',
                      color_continuous_scale='Viridis'
                      )
st.write(fig20)
# 2015 Population
st.markdown('2015 Population')
fig15 = px.choropleth(data,
                      locations='Country/Territory',
                      locationmode='country names',
                      color='2015 Population',  # we indicate the year we are interested in
                      hover_name='Country/Territory',
                      color_continuous_scale='Viridis'
                      )
st.write(fig15)
# 2010 Population
st.markdown('2010 Population')
fig10 = px.choropleth(data,
                      locations='Country/Territory',
                      locationmode='country names',
                      color='2010 Population',  # we indicate the year we are interested in
                      hover_name='Country/Territory',
                      color_continuous_scale='Viridis'
                      )
st.write(fig10)
# 2000 Population
st.markdown('2000 Population')
fig00 = px.choropleth(data,
                      locations='Country/Territory',
                      locationmode='country names',
                      color='2000 Population',  # we indicate the year we are interested in
                      hover_name='Country/Territory',
                      color_continuous_scale='Viridis'
                      )
st.write(fig00)
# 1990 Population
st.markdown('1990 Population')
fig90 = px.choropleth(data,
                      locations='Country/Territory',
                      locationmode='country names',
                      color='1990 Population',  # we indicate the year we are interested in
                      hover_name='Country/Territory',
                      color_continuous_scale='Viridis'
                      )
st.write(fig90)
# 1980 Population
st.markdown('1980 Population')
fig80 = px.choropleth(data,
                      locations='Country/Territory',
                      locationmode='country names',
                      color='1980 Population',  # we indicate the year we are interested in
                      hover_name='Country/Territory',
                      color_continuous_scale='Viridis'
                      )
st.write(fig80)

# World Population Percentage
st.markdown('World Population Percentage')
figwo = px.choropleth(data,
                      locations='Country/Territory',
                      locationmode='country names',
                      color='World Population Percentage',
                      hover_name='Country/Territory',
                      color_continuous_scale='Viridis'
                      )
st.write(figwo)

# Growth Rate
st.markdown('Growth Rate')
figgt = px.choropleth(data,
                      locations='Country/Territory',
                      locationmode='country names',
                      color='Growth Rate',
                      hover_name='Country/Territory',
                      color_continuous_scale='Viridis'
                      )
st.write(figgt)
