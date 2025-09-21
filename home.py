import streamlit as st
import pandas as pd
import requests 
from streamlit_lottie import st_lottie
import json 
from PIL import Image
import plotly.express as px  
from streamlit_option_menu import option_menu
import importlib 
st.set_page_config(
 
    initial_sidebar_state="expanded"
)
st.sidebar.write("")

df=pd.read_excel('cleaned_data.xlsx')

nav=option_menu( menu_title=None, options=["Home","Lists", "Analysis", "Contact"], orientation ='horizontal', 
                styles={ "container": {"padding": "5px", "background-color":"#f5e3c0"},
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "5px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#8eae61"}})

if nav == "Home":
    st.set_page_config(page_title="GIF Demo", layout="centered")
    st.image("petit-prince-dessin-annime.gif", width=2000)

    search = st.text_input("Search for a book:")

    if search:
        search_clean = search.lower().strip()
        mask = df["Description"].str.lower().str.strip().str.contains(search_clean, na=False)

        filtered = df[mask]

        if not filtered.empty:
         st.dataframe(filtered)
        else:
         st.write("Book not found")


elif nav == "Lists":
    page = importlib.import_module("booklists")
    page.app()
   

elif nav == "Contact":
    page = importlib.import_module("contactpage")
    page.app()
    
elif nav == "Analysis": 
    page = importlib.import_module("analysis")
    page.app()
    



