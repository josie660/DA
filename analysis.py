import streamlit as st
import pickle 
from pathlib import Path
import streamlit_authenticator as stauth
import pandas as pd
import plotly.express as px
import numpy as np



def app():
    st.set_page_config(
    
    initial_sidebar_state="expanded"
        )

    df=pd.read_excel('cleaned_data.xlsx')

    names=['marie jose marroun', 'mabelle marroun', 'reina marroun', 'rita akkary', 'perla']
    usernames=['mariejose', 'mabelle','reina', 'rita','perla']

    file_path=Path(__file__).parent/'hashed_pw.pkl'
    with file_path.open('rb') as file:
      hashed_passwords= pickle.load(file)

    authenticator= stauth.Authenticate(names, usernames, hashed_passwords, 'sales_dashboard','abcdef', cookie_expiry_days=0)

    name, authentication_status, username= authenticator.login("login", "main")

    if authentication_status==False:
        st.error("username or password is incorrect please try again")

    if authentication_status==None:
        st.warning("please insert username and password ")
    if authentication_status:


        publisher = st.sidebar.multiselect("Select the publishing house:", options=df["دار النشر"].unique())
        book_type = st.sidebar.multiselect("Select the type of book:", options=df["نوع"].unique())
        subject = st.sidebar.multiselect("Select the subject:", options=df["MATIERE"].unique())
        book = st.sidebar.multiselect("Select the book:", options=df["Description"].unique()) 


        df_selected = df.copy()
        if publisher:
            df_selected = df_selected[df_selected["دار النشر"].isin(publisher)]

        if book_type:
            df_selected = df_selected[df_selected["نوع"].isin(book_type)]

        if subject:
            df_selected = df_selected[df_selected["MATIERE"].isin(subject)]

        if book:
            df_selected = df_selected[df_selected["Description"].isin(book)]

        st.dataframe(df_selected)
        st.title(":bar_chart: Dashboard")
        st.markdown("##")

        average_price = df_selected['PRICE$'].mean()

        option = st.selectbox(label="Select:", options=[ 'horizontal','pie'])

        avg_price = df_selected.groupby('MATIERE')['PRICE$'].mean().sort_values(ascending=False).reset_index()
        avg_price = avg_price.rename(columns={'PRICE$': 'average_price'})

        if option == 'horizontal':
             fig = px.bar(
             avg_price,
             x="average_price",
             y="MATIERE",
             orientation="h"
             )
             fig.update_traces(marker=dict(color="#FF3333"))
             st.plotly_chart(fig)
             
             
        if option=='pie':
           ig = px.pie(
          avg_price,
          names='MATIERE',
          values='average_price',
          title='Average Price Distribution by Subject',color_discrete_sequence=px.colors.qualitative.Set3
          )
           st.plotly_chart(ig)



        with st.container():
            st.write()
            left_column, right_column= st.columns(2)
            with left_column: 
                 avgperpub = df_selected.groupby('دار النشر')['PRICE$'].mean().sort_values(ascending=False).reset_index()
                 avgperpub = avgperpub.rename(columns={'PRICE$': 'average_price','دار النشر':'publisher'})
                 fig = px.bar(
                  avgperpub,
                   x='publisher',
                   y='average_price',
                   orientation='v'
                    )
                 st.plotly_chart(fig)
            with right_column:
                fig2=px.scatter( df_selected, x='PRICE$', y='STK 24')
                fig2.update_traces(line=dict(color="#FF3333"))
                st.plotly_chart(fig2)
        



            





