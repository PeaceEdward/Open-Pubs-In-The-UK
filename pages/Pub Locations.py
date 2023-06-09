import os
import streamlit as st
import pandas as pd
import folium
from geopy.distance import geodesic
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

filepath = os.path.abspath(os.path.join(os.getcwd(), "resources", "data", "uk_pubs.csv"))

df=pd.read_csv(filepath)


st.markdown("<h1 style='text-align: center; font-size: 24px;font-family: Georgia,serif;'>PUB LOCATIONS</h1>", unsafe_allow_html=True)


# Get user input for postal code or local authority
location_type = st.radio("Choose a location type", ["Postal Code", "Local Authority"])
if location_type == "Postal Code":
    location_input = st.selectbox("Select a Postal Code", df['postcode'].unique())
    pubs = df[df["postcode"] == location_input]
else:
    location_input = st.selectbox("Select a Local Authority",df['local_authority'].unique())
    pubs = df[df["local_authority"] == location_input]

# Display pubs on a map
if len(pubs) > 0:
    # Get center of the map as the average of the latitudes and longitudes of the pubs
    center_lat = pubs["latitude"].mean()
    center_lon = pubs["longitude"].mean()
    # Create a Folium map centered on the location and add the pubs as markers
    m = folium.Map(location=[center_lat, center_lon], zoom_start=13)
    marker_cluster = MarkerCluster().add_to(m)
    for index, row in pubs.iterrows():
        folium.Marker(location=[row["latitude"], row["longitude"]], popup=row["name"]).add_to(marker_cluster)    
    folium_static(m)
else:
    st.write("No pubs found in the specified location.")
