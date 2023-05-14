import os
import openai
import streamlit as st
from dotenv import load_dotenv


from llama_index import download_loader
from llama_index.node_parser import SimpleNodeParser
from llama_index import GPTSimpleVectorIndex
from llama_index import LLMPredictor, GPTSimpleVectorIndex, PromptHelper, ServiceContext
from langchain import OpenAI


from llama_index import SimpleDirectoryReader

openai.api_key = st.secrets["OPENAI_API_KEY"]


st.sidebar.markdown("Developed by Zine-Eddine KHENE](https://twitter.com/ZineEddineKhene)", unsafe_allow_html=True)
st.sidebar.markdown("gpt-3.5-turbo")
st.sidebar.markdown("CHU Rennes")
st.sidebar.image("https://urologie-rennes.fr/wp-content/uploads/2020/12/logo-02ai.svg", use_column_width=True)
st.sidebar.header("Service d'urologie Rennes")


SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
loader = SimpleDirectoryReader('Test', recursive=True, exclude_hidden=True)
documents = loader.load_data()

# define LLM
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003",streaming=True))

max_input_size = 4096
num_output = 256
max_chunk_overlap = 20
prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

index = GPTSimpleVectorIndex.from_documents(
    documents, service_context=service_context
)

# Define a simple Streamlit app
st.title("Ask Uro_GPT")
query = st.text_input("What would you like to ask?", "")

if st.button("Submit"):
    response = index.query(query)
    st.write(response)
