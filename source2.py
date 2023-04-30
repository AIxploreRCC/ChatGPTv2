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

st.set_page_config(page_title="Chat with ZinoGPT")
st.title("Chat with ZinoGPT")
st.sidebar.markdown("Developed by Zine-Eddine KHENE](https://twitter.com/ZineEddineKhene)", unsafe_allow_html=True)
st.sidebar.markdown("gpt-3.5-turbo")
st.sidebar.markdown("Not optimised")
st.sidebar.markdown("May run out of OpenAI credits")

SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
loader = SimpleDirectoryReader('Test', recursive=True, exclude_hidden=True)
documents = loader.load_data()

# define LLM
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003"))

max_input_size = 4096
num_output = 256
max_chunk_overlap = 20
prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

index = GPTSimpleVectorIndex.from_documents(
    documents, service_context=service_context
)

# Save your index to a index.json file
index.save_to_disk('index.json')
# Load the index from your saved index.json file
index = GPTSimpleVectorIndex.load_from_disk('index.json', llm_predictor=llm_predictor)



# Define a simple Streamlit app
st.title("Ask Zino_GPT")
query = st.text_input("What would you like to ask?", "")

if st.button("Submit"):
    response = index.query(query)
    st.write(response)
