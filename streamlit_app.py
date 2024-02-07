import streamlit as st 
from langchain.llms import OpenAI

st.title("Quickstart Test Automation App")
         
openai_api _key = st.sidebar.text_input("OpenAI API Key")

def generate_response(input_text):
  11m = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(11m(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'Give me a use case and ask for test cases')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='4') 
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
