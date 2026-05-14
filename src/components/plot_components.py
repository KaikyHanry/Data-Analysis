import streamlit as st

from src.services.chart_service import (
    create_signal_plot
)

def render_signal_group(
    x,
    signals,
    selected_signals,
    title,
    graph_id
):

    fig = create_signal_plot(
        x,
        signals,
        selected_signals,
        title
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # nome do arquivo
    file_name = st.text_input(
        "Nome do arquivo",
        value=f"grafico_{graph_id}",
        key=f"file_name_{graph_id}"
    )

    # exporta PNG
    img_bytes = fig.to_image(
        format="png"
    )

    st.download_button(
        label="Baixar gráfico PNG",
        data=img_bytes,
        file_name=f"{file_name}.png",
        mime="image/png",
        key=f"download_png_{graph_id}"
    )
