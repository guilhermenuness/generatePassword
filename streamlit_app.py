import string, random
import streamlit as st

def generatePassword(len_pass : int = 8):
    options = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(0, len_pass):
        digit = random.choice(options)
        password += digit
    
    return password


st.title("Password generator")
len_pass = st.number_input(
    "Number of characters",
    min_value=8,
    value=8,
    help="Number of characters in your password"
)
button = st.button("Generate")
if button:
    st.write(generatePassword(len_pass=len_pass))