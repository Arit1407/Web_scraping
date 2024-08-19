import streamlit as st
import pandas as pd 
import requests
from bs4 import BeautifulSoup

st.markdown(
    """
    <style>
    body {
        background-image: url('https://wallpapercave.com/wp/wp3416331.jpg');  /* Replace with your image URL */
        background-size: cover;  /* Cover the entire page */
        background-position: center;
        color: #333333;  /* Text color for readability */
    }
    .stApp {
        background-image: url('https://wallpapercave.com/wp/wp3416331.jpg');
        background-size: cover;
        background-position: center;
    }
    </style>
    """, 
    unsafe_allow_html=True
)


st.title("Quotes to Brighten Your Day 😄 ")

st.image("quote.jpg",width=500)

tag = st.selectbox('Choose a topic',['']+['love','humor','life','books','friendship','inspirational'])

generate = st.button("Generate CSV")

if tag:

    url = f"https://quotes.toscrape.com/tag/{tag}/"

    res = requests.get(url)

    content = BeautifulSoup(res.content,'html.parser')

    quotes = content.find_all('div',class_='quote')

    quote_file=[]

    for quote in quotes:
        text = quote.find('span',class_='text').text
        author = quote.find('small',class_='author').text
        link = quote.find('a')
        st.success(text)
        st.markdown(f"<a href=https://quotes.toscrape.com{link['href']}>{author} </a>",unsafe_allow_html=True)

        quote_file.append([text,author,link['href']])

    if generate:
        try:
            df=pd.DataFrame(quote_file)
            df.to_csv("quotes.csv",index=False,header=['Quote','Author','Link'],encoding='cp1252')
        except:
            st.write('Error saving csv file ')
