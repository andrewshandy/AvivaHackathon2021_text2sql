import streamlit as st
import requests
from flask import json


st.write("This is sample string")
text = st.text_input('input string to convert')

dict = {'text': text}


ans = requests.post('http://953a066ec0cd.ngrok.io' , json.dumps(dict)) # link must be changed each time the Flask server starts

data = ans.json()
st.write(data['sql'])
