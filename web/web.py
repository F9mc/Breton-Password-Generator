import streamlit as st
import os
from dotenv import load_dotenv
import sys

load_dotenv()

PATH=os.path.dirname(os.path.abspath(__file__)) + "/"

sys.path.insert(0,PATH+"../")
from generator import password_generator

def main():
    st.title("Generator de mot de passe breton")
    size = st.number_input(
        label="How many words ?",
        min_value=2,
        max_value=30,
        step=1,
        value=3,
        format="%d"
    )

    separator = st.text_input(
        label="Separator",
        value="_",
        placeholder="_",
    )

    numbers = st.checkbox("Numbers")

    capitalize = st.checkbox("Capitalize")

    st.write(f"Mot de passe : {password_generator(size,separator,numbers,capitalize)}")	

if __name__ == "__main__":
    main()