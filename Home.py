import os
import streamlit as st
import numpy as np
import pandas as pd


filepath = os.path.abspath(os.path.join(os.getcwd(), "resources", "data", "uk_pubs.csv"))
df=pd.read_csv(filepath)

st.subtitle('OPEN PUBS IN THE UNITED KINGDOM')

st.write('<style> .caption{ max-width: 100%; }</style>', unsafe_allow_html=True)
st.caption("Pubs are establishments that serve alcoholic beverages,such as beer, wine, and spirits,\n along with snacks and other simple meals.\n They are a popular social gathering places and fun hangout spots for you, your friends and family with a lively atmosphere.")
st.caption('This app helps you browse and explore pubs in the United Kingdom and find those nearest to you.)
st.markdown("# Summary Statistics")
st.write("There are currently {} pubs in the dataset.".format(len(df)))
