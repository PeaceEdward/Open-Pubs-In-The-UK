import os
import streamlit as st
import numpy as np
import folium
from geopy.distance import geodesic
from folium.plugins import MarkerCluster

df = os.path.abspath(os.path.join(os.getcwd(), "resources", "data", "pubs.csv"))





st.markdown("# Pub Locations")

# Get user input for postal code or local authority
location_type = st.radio("Choose a location type", ["Postal Code", "Local Authority"])
if location_type == "Postal Code":
    location_input = st.text_input("Enter a Postal Code")
    pubs = df[df["postcode"] == location_input]
else:
    location_input = st.text_input("Enter a Local Authority")
    pubs = df[df["local_authority"] == location_input]

# Display pubs on a map
if len(pubs) > 0:
    # Get center of the map as the average of the latitudes and longitudes of the pubs
    center_lat = pubs["Latitude"].mean()
    center_lon = pubs["Longitude"].mean()
    # Create a Folium map centered on the location and add the pubs as markers
    m = folium.Map(location=[center_lat, center_lon], zoom_start=13)
    marker_cluster = MarkerCluster().add_to(m)
    for index, row in pubs.iterrows():
        folium.Marker(location=[row["Latitude"], row["Longitude"]], popup=row["Name"]).add_to(marker_cluster)
    st.write(m)
else:
    st.write("No pubs found in the specified location.")
