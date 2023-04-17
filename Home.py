import os
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns


filepath = os.path.abspath(os.path.join(os.getcwd(), "resources", "data", "uk_pubs.csv"))
df=pd.read_csv(filepath)

st.title('OPEN PUBS IN THE UNITED KINGDOM')

st.text("Pubs are establishments that serve alcoholic beverages, such as beer, wine, and spirits,\n along with snacks and other simple meals.\n Pubs are a popular social gathering place in the UK and are deeply ingrained in British culture. \n They are fun hangout spots for you, your friends and family with a lively atmosphere.")

st.markdown("# Summary Statistics")
st.write("There are currently {} pubs in the dataset.".format(len(df)))
