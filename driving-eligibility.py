import streamlit as st
st.title ("Driving Eligibility App")
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120)
if st.button("Check Eligibility"):
    if age >= 18:
        st.success(f"Congratulations {name}, you are eligible to drive!")
    else:
        st.error(f"Sorry {name}, you are not eligible to drive yet.")