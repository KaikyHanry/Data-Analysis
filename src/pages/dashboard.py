import streamlit as st

from src.services.data_service import load_data
from src.services.processing_service import process_data

from src.components.plot_components import (
    render_signal_group
)

def show_dashboard():

    st.title("Análise de Sinais")

    uploaded_file = st.file_uploader(
        "Envie o CSV",
        type=["csv"]
    )

    if uploaded_file:

        df = load_data(uploaded_file)

        selected_case = st.selectbox(
            "Escolha o CASE",
            range(1, 13)
        )

        result = process_data(
            df,
            selected_case
        )

        signals = result["signals"]
        x = result["time"]

        st.subheader("Configuração dos Gráficos")

        num_graphs = st.number_input(
            "Quantidade de gráficos",
            min_value=1,
            max_value=6,
            value=1
        )

        for i in range(num_graphs):

            st.markdown(f"## Gráfico {i+1}")

            selected_signals = st.multiselect(
                f"Escolha os sinais do gráfico {i+1}",
                list(signals.keys()),
                key=f"graph_{i}"
            )

            if selected_signals:

                render_signal_group(
                    x,
                    signals,
                    selected_signals,
                    title=f"Gráfico {i+1}",
                    graph_id=i
                )