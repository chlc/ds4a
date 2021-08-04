from datetime import datetime
from pandas.core.indexes.datetimes import date_range
import streamlit as st
import pandas as pd
import datetime as dt
import numpy as np

#testing streamlit 
#st.title('This is the title')

#st.sidebar.title('Options')

#importing datas
df = pd.read_csv('say_so_daily_shazams.csv')
df['shazam_date'] = pd.to_datetime(df['shazam_date'])
#streamlit testing df
#st.dataframe(df)

#streamlit entering select box
option = st.sidebar.selectbox(
    "Which dashboard?", ("nlp", "shazam", "spotify"), 1)

st.header(option)

if option == 'nlp':
    st.subheader('Vader Sentiment Analysis Results')

if option == 'shazam':
    st.subheader('Song Virality via Shazam')
    st.dataframe(df)
    

if option == 'spotify':
    st.subheader('Spotify Chart Popularity')