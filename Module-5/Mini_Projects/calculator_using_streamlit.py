import streamlit as st

st.title("Calculator", anchor=False)
st.divider()

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number:", 
                           value=None, 
                           placeholder="Put valid number")

with col2:
    num2 = st.number_input("Enter second number:", 
                           value=None, 
                           placeholder="Put valid number")

operator = st.selectbox("Select an operator", 
                        ("+", "-", "*", "/"), 
                        index=None)

button = st.button("Calculate")

if button:
    if num1 is None or num2 is None or operator is None:
        st.warning("Please provide both numbers and select an operator.")
    else:
        try:
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2

            st.success(f"The result of {num1} {operator} {num2} is: **{result}**")

        except ZeroDivisionError:
            st.error("Error: Division by zero is not allowed.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")