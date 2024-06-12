import numpy as np

def clamp(params_q: np.array, lower_bound: int, upper_bound: int) -> np.array:
    params_q[params_q < lower_bound] = lower_bound
    params_q[params_q > upper_bound] = upper_bound
    return params_q

def asymmetric_quantization(PARAMS: np.array, bits: int) -> tuple[np.array, float, int]:
    alpha = np.max(PARAMS)
    beta = np.min(PARAMS)
    scale = (alpha - beta) / (2**bits-1)
    zero = -1*np.round(beta / scale)
    lower_bound, upper_bound = 0, 2**bits-1
    quantized = clamp(np.round(PARAMS / scale + zero), lower_bound, upper_bound)
    return quantized, scale, zero

def asymmetric_dequantize(params_q: np.array, scale: float, zero: int) -> np.array:
    return (params_q - zero) * scale

def quantization_error(PARAMS: np.array, params_q: np.array):
    # calculate the MSE
    return np.mean((PARAMS - params_q)**2)*100

def relative_error(PARAMS: np.array, params_q: np.array):
    return (np.abs(PARAMS - params_q)/np.abs(PARAMS)) * 100

def mean_relative_error(PARAMS: np.array, params_q: np.array):
    return np.mean(relative_error(PARAMS, params_q))

def asymmetric_quantization_percentile(params: np.array, bits: int, percentile: float = 99.99) -> tuple[np.array, float, int]:
    # find the percentile value
    alpha = np.percentile(params, percentile)
    beta = np.percentile(params, 100-percentile)
    scale = (alpha - beta) / (2**bits-1)
    zero = -1*np.round(beta / scale)
    lower_bound, upper_bound = 0, 2**bits-1
    quantized = clamp(np.round(params / scale + zero), lower_bound, upper_bound)
    return quantized, scale, zero
