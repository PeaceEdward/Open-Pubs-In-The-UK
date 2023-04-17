import os
import streamlit as st
import numpy as np
import pandas as pd


filepath = os.path.abspath(os.path.join(os.getcwd(), "resources", "data", "uk_pubs.csv"))
df=pd.read_csv(filepath)

#st.header('OPEN PUBS IN THE UNITED KINGDOM')


st.markdown("<h1 style='text-align: center; font-size: 36px;'>OPEN PUBS IN THE UK</h1>", unsafe_allow_html=True)


st.write('<style> .subheader{ max-width: 100%; }</style>', unsafe_allow_html=True)
st.subheader("Pubs are establishments that serve alcoholic beverages,such as beer, wine, and spirits,along with snacks and other simple meals.They are a popular social gathering places and fun hangout spots for you, your friends and family with a lively atmosphere.")
st.subheader('This app helps you browse and explore pubs in the United Kingdom and find those nearest to you.')
st.markdown("# Summary Statistics")
st.write("There are currently {} pubs in the dataset.".format(len(df)))
