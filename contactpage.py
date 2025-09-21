  
import streamlit as st
import pandas as pd
import requests 
from streamlit_lottie import st_lottie
import json 
from PIL import Image
import plotly.express as px  

def app():

    df=pd.read_excel('cleaned_data.xlsx')

    def load_css (filename):
        with open(filename) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    load_css("style.css")
    with st.container():
            st.write("---")
            st.subheader("get in touch with us! you can send us orders or messages via email")
            contact_form="""
            <input type="hidden" name="_captcha" value="false">
            <form action="https://formsubmit.co/mariejosemarroun@gmail.com" method="POST">
        <input type="text" name="name" placeholder="your name" required>
        <input type="email" name="email" placeholder="your email" required>
        <textarea name='message' placeholder="write us a message!" required></textarea>
        <button type="submit" style="background-color:#8eae61; color:white; padding:10px 20px; border:none; border-radius:8px; cursor:pointer;">Send</button>
       
        </form>
            """
            left_column, right_column= st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st.empty()

