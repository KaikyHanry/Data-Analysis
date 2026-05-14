import pandas as pd
import streamlit as st

@st.cache_data
def load_data(uploaded_file):

    try:

        # lê apenas uma coluna
        df = pd.read_csv(
            uploaded_file,
            header=None,
            skiprows=1
        )

        # renomeia coluna
        df.columns = ["value"]

        # converte para float
        df["value"] = pd.to_numeric(
            df["value"],
            errors="coerce"
        )

        # remove inválidos
        df = df.dropna()

        return df

    except Exception as e:

        st.error(f"Erro ao carregar CSV: {e}")

        return None