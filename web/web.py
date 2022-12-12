import streamlit as st
import sys
sys.path.insert(0,'../Breton-Password-Generator/')
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
    st.write(f"Mot de passe : {password_generator(size,separator)}")	

if __name__ == "__main__":
    main()