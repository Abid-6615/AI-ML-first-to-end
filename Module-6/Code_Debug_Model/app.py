import streamlit as st
from PIL import Image
import os
from google import genai
from api_calling import issue_generator, solution_generator

st.title("Code Debugger")
st.divider()

with st.sidebar:
    # images
    st.header("Control")
    images = st.file_uploader("Upload your images (limit 5 images)",
                              type=['jpeg', 'jpg', 'png'],
                              accept_multiple_files=True)

    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    if pil_images:
        if len(images) > 5 :
            st.warning("Max upload limit is 5")
        else:
            col = st.columns(len(images))
            for i, img in enumerate (images):
                with col[i]:
                    st.image(img)


    
    # select box           
    select_box = st.selectbox("Select an option",
                              ("Hints", "Solution with code"),
                              index=None)
    

    # button
    pressed = st.button("Debug Code",
                        type="primary")
    

if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not select_box:
        st.error("You must select an option")

    if images and select_box:

        # issue
        with st.container(border=True):
            st.subheader("The Issue")
            with st.spinner("Thinking..."):
                generate_issue = issue_generator(pil_images)
                st.markdown(generate_issue)

        # solution
        with st.container(border=True):
            st.subheader("The Solution")
            with st.spinner("Analysis..."):
                generate_solution = solution_generator(pil_images, select_box)
                st.markdown(generate_solution)

