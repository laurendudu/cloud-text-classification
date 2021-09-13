import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
headers = {"Authorization": f"Bearer api_sCckSmiuxDSOBIIdpXarxzeJEyQbWwRYVr"}

st.title('Hello World!')

form = st.form(key='my_form')
text = form.text_input(label='Enter some text')
submit_button = form.form_submit_button(label='Submit')

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({"inputs": text})


if submit_button:
    st.subheader('Data')
    st.write({"text": output})
