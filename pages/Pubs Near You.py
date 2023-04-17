import os
import streamlit as st
import numpy as np
import folium
from geopy.distance import geodesic
from folium.plugins import MarkerCluster



df = os.path.abspath(os.path.join(os.getcwd(), "resources", "data", "pubs.csv"))
st.markdown("# Find the nearest Pub")

# Get user input for their latitude and longitude
user_lat = st.number_input("Enter your Latitude", value=51.5074)
user_lon = st.number_input("Enter your Longitude", value=-0.1278)

# Calculate the distance from the user to each pub using Euclidean distance
df["Distance"] = df.apply(lambda row: geodesic((user_lat, user_lon), (row["latitude"], row["longitude"])).km, axis=1)

# Get the 5 nearest pubs
nearest_pubs = df.sort_values("Distance").head(5)

# Display the nearest pubs on a map
m = folium.Map(location=[user_lat, user_lon], zoom_start=13)
marker_cluster = MarkerCluster().add_to(m)
for index, row in nearest_pubs.iterrows():
    folium.Marker(location=[row["latitude"], row["longitude"]], popup=row["name"]).add_to(marker_cluster)
st.write(m)
