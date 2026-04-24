import streamlit as st
st.title("Input data", anchor = False)
st.divider()

name = st.text_input("Enter your name:", placeholder="Enter your name")
print(type(name))

age = st.number_input("Enter your age:", value=None, placeholder="Enter your age")
print(type(age))

pressed = st.button("Submit")
if pressed:
    st.write(f"Your name is {name} and your age is {age}")

pssword = st.text_input("Enter your password:", type="password", placeholder="Enter your password")
st.write(f"Your password is {pssword}")

selected = st.selectbox("Choose your Profession:", ("Student", "Employee", "Businessman"), index=None)
st.write(f"You selected {selected}")