import streamlit as st
import pandas as pd
import requests 
from streamlit_lottie import st_lottie
import json 
from PIL import Image
import plotly.express as px  
from streamlit_option_menu import option_menu

def app():
    df=pd.read_excel('cleaned_data.xlsx')

    st.set_page_config(page_title="book helper", page_icon=':books:',layout='wide',initial_sidebar_state="expanded")
    st.title("back to school book cost estimator")

    #image
   # image= Image.open("images/red.jpg")
    # Resize with fixed height, maintaining aspect ratio
    #new_height = 50
    #new_width = image.width 
    #img_resized = image.resize((new_width, new_height))
    #st.image(img_resized)

    st.subheader("Hi! :wave: input your school and grade and i'll help you estimate the cost of your book list for the upcoming year")
    dict={'EB1 ':'EB1', '3SG':'SG', '3SV':'SV', '3SE':'SE', '3SEV':'S3', '3LH':'LH', '3SEGVH':'S3', 'PS1 ':'PS1','PS2 ':'PS2','EB3 ':'EB3', 'EB7 ':'EB7','EB8 ':'EB8', 'GS ':'PS3','GS':'PS3', 'EB6 ':'EB6', 'EB4 ':'EB4'}
    df['GRADE']=df["GRADE"].map(dict).fillna(df['GRADE'])

    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

    
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    # Utilisation : depuis un fichier local
    lottie= load_lottiefile("little prince hanging.json")



    with st.container():
        st.write()
        left_column, right_column= st.columns(2)
        with left_column: 
            grades =['PS1','PS2','PS3', 'EB1', 'EB2', 'EB3', 'EB4', 'EB5', 'EB6', 'EB7', 'EB8' , 'EB9', '1S','2S', 'S3', 'SG','SV','SE','LH']
            selected_grade = st.selectbox("Select Grade:", grades)
            st.markdown("K-:Antounieh khaldieh, Z-:Antounieh zgharta,      M-:'Charite,      F-:Frere,        N-:Nazareth,    C-:Carmalieh,        Q-:Al kalima school,        A-:St Georges Achache")
            schools=[ 'K-',     'Z-',          'M-',          'F-',          'N-',   'C-',          'Q-',          'A-']
            selected_school=st.selectbox('select school:',schools)
            #now show the dataframe having 
            filtered = df[(df['GRADE'] == selected_grade) & (df[selected_school]==selected_school)]
            

            st.subheader("Books for selected grade and school:")
            st.dataframe(filtered[['Description', 'MATIERE', 'PRICE$', 'PRICE LL', 'STK 24']])

            total_price = filtered['PRICE$'].sum()
            st.write(f"**Estimated Total Price ($):** ${total_price:.2f}")
            st.subheader(':recycle: if bought used:')
            recommended_used=['BOOK', 'BK','LIVRE','كتاب']
            used_classes=['EB6', 'EB7','EB8','EB9','1S','2S','S3','SG','SV','SE','LH']
            df_used=filtered.copy()
        if selected_grade in used_classes:
            df_used["PRICE$"]=df_used.apply( lambda row: row['PRICE$']*0.5 if row['نوع'] in recommended_used else row['PRICE$'], axis=1)
            usedprice= df_used['PRICE$'].sum()
            st.markdown("Main textbooks are recommended to be bought used to save resources. They cost half the price!")
            st.write(f"**Total:** ${usedprice:.2f}")
        else:
            st.write("buying used is only for grade six and above")
            usedprice=total_price
            st.write(f"**Total if following recommendation:** ${usedprice:.2f}")

    
        with right_column:
            st_lottie(lottie, height='200', key='coding')
             #st.set_page_config(page_title="GIF DEMO", layout="centered")
             #st.image("the-little-prince.gif")

app()



    
        
    
