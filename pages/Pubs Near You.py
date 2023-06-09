import os
import streamlit as st
import numpy as np
import folium
import pandas as pd
from scipy.spatial import distance
from geopy.distance import geodesic
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static




filepath = os.path.abspath(os.path.join(os.getcwd(), "resources", "data", "uk_pubs.csv"))
df=pd.read_csv(filepath)

st.markdown("<h1 style='text-align: center; font-size: 24px;font-family: Georgia,serif;'>FIND PUBS NEAR YOU</h1>", unsafe_allow_html=True)


# Get user input for their latitude and longitude
user_lat = st.number_input("Enter your Latitude", value=51.5074)
user_lon = st.number_input("Enter your Longitude", value=-0.1278)

# Calculate the distance from the user to each pub using Euclidean distance
#df["Distance"] = df.apply(lambda row: geodesic((user_lat, user_lon), (row["latitude"], row["longitude"])).km, axis=1)
df["Distance"] = df.apply(lambda row: distance.euclidean((user_lat, user_lon), (row["latitude"], row["longitude"])), axis=1)



# Get the 5 nearest pubs
nearest_pubs = df.sort_values("Distance").head(5)

# Display the nearest pubs on a map
m = folium.Map(location=[user_lat, user_lon], zoom_start=13)
marker_cluster = MarkerCluster().add_to(m)
for index, row in nearest_pubs.iterrows():
    folium.Marker(location=[row["latitude"], row["longitude"]], popup=row["name"]).add_to(marker_cluster)
folium_static(m)
