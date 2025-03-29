# Build a website with python
# cmd - streamlit run streamlit_app.py
# pip freeze > requirements.txt

import time
import streamlit as st
import numpy as np
import pandas as pd

# Website config
st.set_page_config(
   page_title="Hello World",
   page_icon="🍕",
   layout="centered",
   initial_sidebar_state="expanded",
   menu_items={}
)

# Website title
st.title('My first website built by python!')

# Time progress bar
bar = st.progress(0)
for i in range(100):
    bar.progress(i + 1, f'In progress... {i+1} %')
    time.sleep(0.05)

bar.progress(100, 'Completed！')

# Ramdon chart
chart_data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# Random map location
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [22.3, 114.1],
    columns=['lat', 'lon'])
st.map(map_data)

# Button
if st.button('Click me!'):
    st.text("Smile!😄")

# Chat agent
with st.chat_message("user"): 
    st.write("Hi 👋, I am Chat Bot 🤖 , who are you?")

st.chat_input("Say something...")




