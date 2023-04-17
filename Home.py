import os
import streamlit as st
import numpy as np
import folium
from geopy.distance import geodesic
from folium.plugins import MarkerCluster



df = os.path.abspath(os.path.join(os.getcwd(), "resources", "data", "uk_pubs.csv"))

st.markdown("# Summary Statistics")
st.write("There are currently {} pubs in the dataset.".format(len(df)))
st.write("The average latitude is {} and the average longitude is {}.".format(df["Latitude"].mean(), df["Longitude"].mean()))
st.write("The pub with the longest name is '{}'.".format(df.loc[df["Name"].str.len().idxmax(), "Name"]))
