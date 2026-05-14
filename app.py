import streamlit as st

from src.components.sidebar import render_sidebar

from src.pages.dashboard import show_dashboard
from src.pages.analysis import show_analysis
from src.pages.prediction import show_prediction

st.set_page_config(
    page_title="Data Analysis",
    layout="wide"
)

page = render_sidebar()

if page == "Dashboard":
    show_dashboard()

elif page == "Análise":
    show_analysis()

elif page == "Predição":
    show_prediction()
