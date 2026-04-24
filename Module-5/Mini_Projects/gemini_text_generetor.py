import streamlit as st
st.title("Text Generator",  
         anchor=False)
st.divider()

from google import genai

import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

user_prompt = st.text_input("Enter your prompt here:",
                            value=None,
                            placeholder="What you want to know?")

button = st.button("Generate text")

if button:
    if user_prompt:
        with st.spinner("Thinking"):
            try:
                response = client.models.generate_content(
                    model = "gemini-3-flash-preview",
                    contents = user_prompt
                )
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred {e}")
    else:
        st.warning("Please enter a prompt first")