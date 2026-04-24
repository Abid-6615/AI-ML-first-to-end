import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

st.title("Professional Sentence Improver")
st.divider()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

user_input = st.text_area("Your sentence:", placeholder="Enter your prompt here")

if st.button("Improve Sentence"):
    if user_input.strip():
        with st.spinner("Thinking"):
            try:
                prompt = f"Improve this sentence professionally: '{user_input}'"
                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=prompt
                )
                st.subheader("Improved Version:")
                st.success(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a sentence!")
