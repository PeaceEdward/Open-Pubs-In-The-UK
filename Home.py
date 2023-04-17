import os
import streamlit as st
import numpy as np
import pandas as pd
import folium
from geopy.distance import geodesic
from folium.plugins import MarkerCluster



filepath = os.path.abspath(os.path.join(os.getcwd(), "resources", "data", "uk_pubs.csv"))
df=pd.read_csv(filepath)

st.markdown("# Summary Statistics")
st.write("There are currently {} pubs in the dataset.".format(len(df)))
st.write("The average latitude is {} and the average longitude is {}.".format(df["latitude"].mean(), df["longitude"].mean()))
st.write("The pub with the longest name is '{}'.".format(df.loc[df["name"].str.len().idxmax(), "name"]))
