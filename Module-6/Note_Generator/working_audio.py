from gtts import gTTS
import streamlit as st
import io

text = ("Hello, Welcome to my project.")

speech = gTTS(text, lang = 'en', slow = False)
speech.save("welcome.mp3")

audio_buffer = io.BytesIO()
speech.write_to_fp(audio_buffer)

st.audio(audio_buffer)