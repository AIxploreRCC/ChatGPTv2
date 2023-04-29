import os
import openai
import streamlit as st
openai.api_key = st.secrets['key']

from llama_index import download_loader
from llama_index.node_parser import SimpleNodeParser
from llama_index import GPTSimpleVectorIndex
from llama_index import LLMPredictor, GPTSimpleVectorIndex, PromptHelper, ServiceContext
from langchain import OpenAI

data = 'Test'
index_file = 'index.json'

from llama_index import SimpleDirectoryReader

# load the .txt data and convert it into an index
documents_txt = SimpleDirectoryReader('EAU-Guidelines-on-Renal-Cell-Carcinoma-2023.pdf').load_data()

from llama_index import SimpleDirectoryReader

SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
loader = SimpleDirectoryReader('EAU-Guidelines-on-Renal-Cell-Carcinoma-2023.pdf', recursive=True, exclude_hidden=True)
documents = loader.load_data()
