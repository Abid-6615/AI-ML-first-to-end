import streamlit as st
st.title("Video element", anchor = False)
st.divider()

video = st.file_uploader("Enter your video file",
                         type = ['mp4', 'avi', 'mov'])

button = st.button("Play")

if button:
    if video:
        st.video(video)
        st.success("Video uploaded successfully!")
    else:
        st.error("Please upload a video file to play.")