import numpy as np

def calculate_metrics(signal):

    return {

        "mean": np.mean(signal),
        "std": np.std(signal),
        "max": np.max(signal),
        "min": np.min(signal),
        "rms": np.sqrt(np.mean(signal ** 2)),
        "peak_to_peak": np.ptp(signal)
    }