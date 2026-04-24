import streamlit as st
st.title("Audio element", anchor = False)
st.divider()

audio = st.file_uploader("Enter your audio file",
                 type = ['mp3', 'wav', 'ogg'])

if audio:
    st.audio(audio)
