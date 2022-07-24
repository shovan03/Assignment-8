import streamlit as st

st.write("""
# Addition of two numbers
""")

number_1 = st.number_input("First Number")
number_2 = st.number_input("Second Number")

sum = number_1 + number_2

st.write(f"The sum is: {sum}")
