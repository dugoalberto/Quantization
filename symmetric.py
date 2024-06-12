import numpy as np


def clamp(params_q: np.array, lower_bound: int, upper_bound: int) -> np.array:
    params_q[params_q < lower_bound] = lower_bound
    params_q[params_q > upper_bound] = upper_bound
    return params_q


def symmetric_dequantize(params_q: np.array, scale: float) -> np.array:
    return params_q * scale


def symmetric_quantization(params: np.array, bits: int) -> tuple[np.array, float]:
    alpha = np.max(np.abs(params))
    scale = alpha / (2 ** (bits - 1) - 1)
    lower_bound = -2 ** (bits - 1)
    upper_bound = 2 ** (bits - 1) - 1
    quantized = clamp(np.round(params / scale), lower_bound, upper_bound)
    return quantized, scale


def quantization_error(PARAMS: np.array, params_q: np.array):
    # calculate the MSE
    return np.mean((PARAMS - params_q) ** 2) * 100


def relative_error(PARAMS: np.array, params_q: np.array):
    return (np.abs(PARAMS - params_q) / np.abs(PARAMS)) * 100
