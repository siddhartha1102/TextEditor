import streamlit as st
filename = st.text_input('Filename',)
text_contents=st.text_area("Write content", value="", height=300, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None,  placeholder=None, disabled=False)
st.download_button('Download text file', text_contents,file_name=filename+".txt")

