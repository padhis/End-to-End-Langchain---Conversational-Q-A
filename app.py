#Conversational Q&A Chatbot
from langchain.llms import OpenAI
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

import os

def get_response_openai(question):
    llm = OpenAI(openai_api_key = os.environ["OPENAI_API_KEY"] ,model_name = 'text-davinci-003', temperature = 0.7)
    response = llm(question)
    return response

input = st.text_input('input: ', key = 'input')
response = get_response_openai(input)

submit = st.button('Ask the question')

if submit:
    st.subheader('The Response is: ')
    st.write(response)