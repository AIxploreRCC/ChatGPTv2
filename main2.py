import streamlit as st

st.write("""
# My First App
Hello *world!*
""")


index_file = 'index.json'



query = st.text_input('Enter Your Query')
button = st.button(f'Response')

