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

@st.cache_resource
def load_indexes():
    """load the pipeline object for preprocessing and the ml model"""

# load index files

index_file = load('index.json')
data = load('EAU-Guidelines-on-Renal-Cell-Carcinoma-2023.pdf')

   

