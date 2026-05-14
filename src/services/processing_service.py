import numpy as np

from src.services.case_registry import CASE_CONFIGS

def process_data(df, selected_number):

    # vetor 1D
    y = df["value"].values

    signal_map = CASE_CONFIGS.get(selected_number)

    if signal_map is None:
        raise ValueError("CASE inválido")

    signals = {}

    for signal_name, (start, end) in signal_map.items():

        signals[signal_name] = y[start:end]

    # eixo temporal
    x = np.linspace(
        0,
        1,
        num=len(next(iter(signals.values())))
    )

    return {
        "signals": signals,
        "time": x
    }