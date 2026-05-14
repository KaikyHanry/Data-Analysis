import plotly.graph_objects as go

def create_signal_plot(
    x,
    signals,
    selected_signals,
    title="Sinais"
):

    fig = go.Figure()

    for signal_name in selected_signals:

        fig.add_trace(
            go.Scatter(
                x=x,
                y=signals[signal_name],
                mode="lines",
                name=signal_name
            )
        )

    fig.update_layout(
        title=title,
        xaxis_title="Tempo",
        yaxis_title="Amplitude",
        hovermode="x unified",
        template="plotly_dark",
        height=500
    )

    return fig