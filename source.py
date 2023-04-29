import os
import openai
import streamlit as st
openai.api_key = st.secrets['key']

from llama_index import download_loader
from llama_index.node_parser import SimpleNodeParser
from llama_index import GPTSimpleVectorIndex
from llama_index import LLMPredictor, GPTSimpleVectorIndex, PromptHelper, ServiceContext
from langchain import OpenAI


index_file = 'index.json'

@st.cache
def load_data(nrows):
    download = github_session.get(url).content
    data = './Test'
    return data

data= load_data(1000)

# load the .txt data and convert it into an index
from llama_index import SimpleDirectoryReader

SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
loader = SimpleDirectoryReader('data', recursive=True, exclude_hidden=True)
documents = loader.load_data()
