import os
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import altair as alt



filepath = os.path.abspath(os.path.join(os.getcwd(), "resources", "data", "uk_pubs.csv"))
image_path=os.path.abspath(os.path.join(os.getcwd(), "resources", "data", "pexels-chan-walrus-941864.jpg"))

df=pd.read_csv(filepath)


st.markdown("<h1 style='text-align: center; font-size: 24px;font-family: Georgia,serif;'>OPEN PUBS IN THE UK</h1>", unsafe_allow_html=True)

image= Image.open(image_path)
st.image(image, use_column_width= True)

# st.write('<style> .subheader{ max-width: 100%; display: flex; text-align: center;font-family: Georgia,serif; font-size: 24px; }</style>', unsafe_allow_html=True)
st.write('<style> \
            h1, h2, h3, h4, h5, h6 {font-family: Georgia, serif;} \
            .caption, .subheader, .markdown {font-family: Georgia, serif; font-size: 24px !important;} \
          </style>', unsafe_allow_html=True)

st.markdown("Pubs are establishments that serve alcoholic beverages,such as beer, wine, and spirits,along with snacks and other simple meals. They are a popular social gathering places and fun hangout spots for you, your friends and family with a lively atmosphere.")
st.markdown('This app helps you browse and explore pubs and clubs in the United Kingdom and find those nearest to you.')
st.markdown("#### Data Summary")

st.markdown('###### Sample data')
st.dataframe(df.head(5))

count_la = df['local_authority'].value_counts().to_frame().reset_index()
count_la.columns = ['local_authority', 'count']
count_df=count_la[:10]

st.markdown('###### Local Authority with the most pubs')

chart = alt.Chart(count_df).mark_bar(strokeOpacity=0, color='#d25151').encode(
    x='count:Q',
    y=alt.Y('local_authority:N', sort='-x')
).properties(
    width=500,
    height=400
).configure_mark(
    opacity=0.7,
    strokeWidth=0
)            
            
           

# display the chart in Streamlit
st.altair_chart(chart)

st.markdown('###### Pubs with the most branches')


count_name = df['name'].value_counts().to_frame().reset_index()
count_name.columns = ['name', 'count']
count_name_df=count_name[:10]

chart1 = alt.Chart(count_name_df).mark_bar(strokeOpacity=0, color='#d25151').encode(
    x='count:Q',
    y=alt.Y('name:N', sort='-x')
).properties(
    width=500,
    height=400
).configure_mark(
    opacity=0.7,
    strokeWidth=0
)            
st.altair_chart(chart1)


st.markdown('###### Summary statistics')

st.write("There are currently {} pubs in the dataset.".format(len(df)))
st.write("The local authority with least number of pubs is West Lothian with only 2 pubs)
