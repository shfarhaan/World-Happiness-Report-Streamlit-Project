import streamlit as st
import pandas as pd
import numpy as np

DATA_URL = (
    "F:\OneDrive Files\Data Science Resources\Project Files\Working with Streamlit\World_Happiness_Report_2020"
)

st.title("World Happiness Report in 2020")
st.markdown("This application is a Streamlit Dashboard " + 
" that can be used to see and analyze Mental Well Being of People in 2020! 😊🌎")

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows = nrows, parse_analytics = [['Country name', 'Ladder score']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], implace = True)
