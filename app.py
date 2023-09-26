import streamlit as st

user_input = st.text_input("Enter your name:")
st.write("Hello,", user_input)

age = st.slider("Select your age:", 0, 100, 25) # (Min, Max, Start)
st.write("You are", age, "years old.")

if st.button("Click me 🐣"):
    st.write("Peeka-Boo 👻") #  '+ user_input'

num1 = st.text_input("Enter the first number:")
num2 = st.text_input("Enter the second number:")
operation = st.radio("Select an operation:", ("Add", "Subtract", "Multiply", "Divide"))

if st.button("Calculate"):
    if operation == "Add":
        result = float(num1) + float(num2)
    elif operation == "Subtract":
        result = float(num1) - float(num2)
    elif operation == "Multiply":
        result = float(num1) * float(num2)
    elif operation == "Divide":
        result = float(num1) / float(num2)
    st.write("Result:", result)

