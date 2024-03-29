import streamlit as st 
from langchain.llms import OpenAI

st.title("Quickstart for AI in Tamm app 🦅 ")
         
openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form0'):
  text = st.text_area('Enter text:', 'Give me a user story to analyze it')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠️') 
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)

with st.form('my_form1'):
  text = st.text_area('Enter text:', 'Give me a use case and ask for test cases')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠️') 
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)


st.title("Create a test automation for the above scenarios /please copy the TCs you need to automate/")

with st.form('my_form2'):
  text = st.text_area('Enter text:', 'type the use case and ask for test script')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠️') 
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
