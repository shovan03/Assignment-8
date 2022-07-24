import streamlit as st

st.write("""
# Addition of two numbers
""")

def user_input():
    number_1 = st.number_input("First Number")
    number_2 = st.number_input("Second Number")

    return number_1 + number_2
