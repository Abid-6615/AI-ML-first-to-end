import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

clinet = genai.Client(api_key=api_key)


# issue generator
def issue_generator(images):
    prompt = """Find the issues form the picture max 150 words. 
            make sure to add necessary markdown to differentiate diffrent section"""
    response = clinet.models.generate_content(
        model=("gemini-3-flash-preview"),
        contents=(images, prompt)
    )
    return response.text

# solution generator
def solution_generator(images, select_box):
    if select_box == "Hints":
        instruction = "Give only solution hints for the issues found in the image. Do not provide full code. Keep it under 300 words."
    else:
        instruction = "Provide a complete and optimized code solution to fix the issues shown in the image. Include brief comments in the code."

    prompt = f"""
    You are an expert software debugger. 
    Task: {instruction}
    
    Format: Use clear Markdown with proper headings. Use bold text for key points.
    """
    response = clinet.models.generate_content(
        model=("gemini-3-flash-preview"),
        contents=(images, prompt)
    )
    return response.text
