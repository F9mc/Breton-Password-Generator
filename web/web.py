from tkinter import X, Button
from zxcvbn import zxcvbn
import streamlit as st
import os
from dotenv import load_dotenv
import sys

load_dotenv()

PATH=os.path.dirname(os.path.abspath(__file__)) + "/"

sys.path.insert(0,PATH+"../")
from generator import password_generator

def get_score(password):
    return f"{(zxcvbn(password)['score'] / 4) * 100}%"

def main():
    st.set_page_config(
        page_title="Bzh Pwd Generator",
        page_icon="🔑",
        initial_sidebar_state="expanded"
    )
    container1 = st.container()
    container2 = st.container()
    col1, col2 = container2.columns(2)
    size = container1.number_input(
        label="How many words ?",
        min_value=2,
        max_value=30,
        step=1,
        value=3,
        format="%d"
    )

    separator = container1.text_input(
        label="Separator",
        value="_",
        placeholder="_",
    )

    with col1:
        numbers = st.checkbox("Numbers")
        capitalize = st.checkbox("Capitalize")
        password = password_generator(size,separator,numbers,capitalize)
        st.write(f"Mot de passe : {password}")
        st.write(f"Strength: {get_score(password)}")
    with col2:
        if st.button("New password"):
            password = password_generator(size,separator,numbers,capitalize)

if __name__ == "__main__":
    main()