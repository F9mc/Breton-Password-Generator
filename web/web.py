import streamlit as st
import sys
sys.path.insert(0,'../generator')
from generator import password_generator


def main():
    st.title("Generator de mot de passe breton")
    size = int(st.number_input("How many words ?"))
    separator = st.text_input(
        "Separator",
        placeholder="_",
    )
    st.write(f"Mot de passe : {password_generator(),size,separator}")	

if __name__ == "__main__":
    main()