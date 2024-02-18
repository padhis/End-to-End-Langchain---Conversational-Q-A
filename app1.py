import streamlit as st
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
import os

load_dotenv()

st.set_page_config(page_title = 'Conversational Q&A Chatbot')
st.title("Hey, let's chat")

chat = ChatOpenAI(temperature = 0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [SystemMessage(content = 'You are a comedian AI assistant')]

#Define a function to get responses 
def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content = question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content = answer.content))
    return answer.content


input = st.text_input('Input: ', key = 'input')
response = get_chatmodel_response(input)

submit = st.button('Ask the question')

if submit:
    st.subheader('The Response')
    st.write(response)