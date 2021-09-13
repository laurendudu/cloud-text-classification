import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
headers = {"Authorization": f"Bearer api_sCckSmiuxDSOBIIdpXarxzeJEyQbWwRYVr"}

st.title('Text Classification')

form = st.form(key='my_form')
text = form.text_input(label='Enter some text')
submit_button = form.form_submit_button(label='Submit')

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({"inputs": text})


if submit_button:
    st.subheader('Sentiment Analysis')
    
    if type(output) == type({}):        
        st.write({"Error": 'The model is loading, please try again in 30 seconds.'})
    else:
        st.write({"NEGATIVE": output[0][0]['score']})
        st.write({"POSITIVE": output[0][1]['score']})
