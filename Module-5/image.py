import streamlit as st
st.title("Image element", anchor = False)
st.divider()

image = st.file_uploader("Upload your image", 
                 type = ['jpg', 'jpeg', 'png'],
                 accept_multiple_files = True,)

if image:
    col = st.columns(len(image))

    for i, img in enumerate(image):
        with col[i]:
            st.image(img)
        