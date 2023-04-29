import os
import openai
import streamlit as st
openai.api_key = st.secrets['key']

from llama_index import download_loader
from llama_index.node_parser import SimpleNodeParser
from llama_index import GPTSimpleVectorIndex
from llama_index import LLMPredictor, GPTSimpleVectorIndex, PromptHelper, ServiceContext
from langchain import OpenAI

doc_path = 'EAU-Guidelines-on-Renal-Cell-Carcinoma-2023.pdf'
index_file = 'index.json'

if 'response' not in st.session_state:
    st.session_state.response = ''

def send_click():
    st.session_state.response  = index.query(st.session_state.prompt)

index = None
st.title("Yeyu's Doc Chatbot")

sidebar_placeholder = st.sidebar.container()
uploaded_file = st.file_uploader("Choose a file")
