import streamlit as st
import numpy as np

from src.services.chart_service import (
    create_signal_plot
)

from src.services.analysis_service import (
    calculate_metrics
)

def render_signal_group(
    x,
    signals,
    selected_signals,
    title,
    graph_id
):

    st.markdown(f"### {title}")

    t_min = float(np.min(x))
    t_max = float(np.max(x))

    # seleção da janela
    time_window = st.slider(
        "Janela de tempo",
        min_value=t_min,
        max_value=t_max,
        value=(t_min, t_max),
        key=f"time_window_{graph_id}"
    )

    t_start, t_end = time_window

    # máscara temporal
    mask = (x >= t_start) & (x <= t_end)

    # aplica janela
    x_window = x[mask]

    filtered_signals = {}

    for signal_name in selected_signals:

        filtered_signals[signal_name] = (
            signals[signal_name][mask]
        )

    auto_y = st.checkbox(
        "Eixo Y automático",
        value=True,
        key=f"auto_y_{graph_id}"
    )

    y_min, y_max = None, None

    if not auto_y:

        # calcula limites globais
        global_min = min(
            np.min(signal)
            for signal in filtered_signals.values()
        )

        global_max = max(
            np.max(signal)
            for signal in filtered_signals.values()
        )

        col1, col2 = st.columns(2)

        with col1:

            y_min = st.number_input(
                "Y mínimo",
                value=float(global_min),
                key=f"y_min_{graph_id}"
            )

        with col2:

            y_max = st.number_input(
                "Y máximo",
                value=float(global_max),
                key=f"y_max_{graph_id}"
            )

    # cria gráfico
    fig = create_signal_plot(
        x_window,
        filtered_signals,
        selected_signals,
        title,
        y_min,
        y_max
    )

    tab1, tab2 = st.tabs([
        "Gráfico",
        "Análise"
    ])

    with tab1:

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # EXPORTAÇÃO
        file_name = st.text_input(
            "Nome do arquivo",
            value=f"grafico_{graph_id}",
            key=f"file_name_{graph_id}"
        )

        img_bytes = fig.to_image(
            format="png"
        )

        st.download_button(
            label="Baixar PNG",
            data=img_bytes,
            file_name=f"{file_name}.png",
            mime="image/png",
            key=f"download_png_{graph_id}"
        )

    # ABA ANÁLISE
    with tab2:

        for signal_name in selected_signals:

            signal = signals[signal_name]

            metrics = calculate_metrics(signal)

            st.markdown(f"### {signal_name}")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Média",
                    f"{metrics['mean']:.4f}"
                )

                st.metric(
                    "Desvio padrão",
                    f"{metrics['std']:.4f}"
                )

            with col2:

                st.metric(
                    "Máximo",
                    f"{metrics['max']:.4f}"
                )

                st.metric(
                    "Mínimo",
                    f"{metrics['min']:.4f}"
                )

            with col3:

                st.metric(
                    "RMS",
                    f"{metrics['rms']:.4f}"
                )

                st.metric(
                    "Pico a Pico",
                    f"{metrics['peak_to_peak']:.4f}"
                )

        st.divider()