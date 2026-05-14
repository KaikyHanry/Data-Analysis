import streamlit as st

def render_sidebar():
    st.sidebar.title("Menu")

    option = st.sidebar.radio(
        "Selecione uma página:",
        ("Dashboard", "Análise", "Predição")
    )
    return option