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
    
    index_document = GPTSimpleVectorIndex.load_from_disk('index_file.json')

    return index_video

def main():


    # load indices
    index_document = load_indexes()

    st.header('Custom-Made Chatbots')

    # select the data to write queries for
    st.write("Select the data that your chatbot should be trained with:")
    data = st.selectbox('Data', ('.txt file (My favorite fruits)', 'Youtube Video (Vanilla Cake Recipe)', 'Wikipedia Article (Apple)'))

    # use the index based on the selected data
    data == '.txt file (My favorite fruits)':
        st.image('fruit.png')
        index = index_document
  

    # query the selected index
    query = st.text_input('Enter Your Query')
    button = st.button(f'Response')
