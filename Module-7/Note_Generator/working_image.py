import streamlit as st
from google import genai
from PIL import Image
import os
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

my_api_key = os.getenv("GENIMI_API_KEY")

client = genai.Client(api_key=my_api_key)

images = st.file_uploader("Upload the photos of your note",
                              type=['jpg', 'jpeg', 'png'],
                              accept_multiple_files=True)

if images:
    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)


    prompt = """Summarize the picture in note formate at max 150 words
                make sure to add necessary markdown to differentiate diffrent section"""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= [pil_images, prompt]
    )
    st.text(response.text)