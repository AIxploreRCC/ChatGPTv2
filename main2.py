import streamlit as st

st.write("""
# My First App
Hello *world!*
""")


index_file = 'index.json'

index = GPTSimpleVectorIndex.load_from_disk(index_file)

query = st.text_input('Enter Your Query')
button = st.button(f'Response')

