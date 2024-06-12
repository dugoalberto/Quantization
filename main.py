import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

from asymmetric import relative_error, asymmetric_dequantize, asymmetric_quantization_percentile, quantization_error
from symmetric import symmetric_quantization, symmetric_dequantize


""" symmetric """
def s2():
    (symmetric_q_2, symmetric_scale_2) = symmetric_quantization(PARAMS, 2)
    params_deq_symmetric_2 = symmetric_dequantize(symmetric_q_2, symmetric_scale_2)
    abs_error_symmetric_2 = relative_error(PARAMS, params_deq_symmetric_2)
    mean_error_symmetric_2 = quantization_error(PARAMS, params_deq_symmetric_2)
    return abs_error_symmetric_2, mean_error_symmetric_2
def s4():
    (symmetric_q_4, symmetric_scale_4) = symmetric_quantization(PARAMS, 4)
    params_deq_symmetric_4 = symmetric_dequantize(symmetric_q_4, symmetric_scale_4)
    abs_error_symmetric_4 = relative_error(PARAMS, params_deq_symmetric_4)
    mean_error_symmetric_4 = quantization_error(PARAMS, params_deq_symmetric_4)
    return abs_error_symmetric_4, mean_error_symmetric_4
def s8():
    (symmetric_q_8, symmetric_scale_8) = symmetric_quantization(PARAMS, 8)
    params_deq_symmetric_8 = symmetric_dequantize(symmetric_q_8, symmetric_scale_8)
    abs_error_symmetric_8 = relative_error(PARAMS, params_deq_symmetric_8)
    mean_error_symmetric_8 = quantization_error(PARAMS, params_deq_symmetric_8)
    return abs_error_symmetric_8, mean_error_symmetric_8
def s16():
    (symmetric_q_16, symmetric_scale_16) = symmetric_quantization(PARAMS, 16)
    params_deq_symmetric_16 = symmetric_dequantize(symmetric_q_16, symmetric_scale_16)
    abs_error_symmetric_16 = relative_error(PARAMS, params_deq_symmetric_16)
    mean_error_symmetric_16 = quantization_error(PARAMS, params_deq_symmetric_16)
    return abs_error_symmetric_16, mean_error_symmetric_16
def s32():
    (symmetric_q_32, symmetric_scale_32) = symmetric_quantization(PARAMS, 32)
    params_deq_symmetric_32 = symmetric_dequantize(symmetric_q_32, symmetric_scale_32)
    abs_error_symmetric_32 = relative_error(PARAMS, params_deq_symmetric_32)
    mean_error_symmetric_32 = quantization_error(PARAMS, params_deq_symmetric_32)
    return abs_error_symmetric_32, mean_error_symmetric_32

""" asymmetric"""
def a2():
    (asymmetric_q_2, asymmetric_scale_2, zero_2) = asymmetric_quantization_percentile(PARAMS, 2)
    params_deq_asymmetric_2 = asymmetric_dequantize(asymmetric_q_2, asymmetric_scale_2, zero_2)
    abs_error_asymmetric_2 = relative_error(PARAMS, params_deq_asymmetric_2)
    mean_error_asymmetric_2 = quantization_error(PARAMS, params_deq_asymmetric_2)
    return abs_error_asymmetric_2, mean_error_asymmetric_2
def a4():
    (asymmetric_q_4, asymmetric_scale_4, zero_4) = asymmetric_quantization_percentile(PARAMS, 4)
    params_deq_asymmetric_4 = asymmetric_dequantize(asymmetric_q_4, asymmetric_scale_4, zero_4)
    abs_error_asymmetric_4 = relative_error(PARAMS, params_deq_asymmetric_4)
    mean_error_asymmetric_4 = quantization_error(PARAMS, params_deq_asymmetric_4)
    return abs_error_asymmetric_4, mean_error_asymmetric_4
def a8():
    (asymmetric_q_8, asymmetric_scale_8, zero_8) = asymmetric_quantization_percentile(PARAMS, 8)
    params_deq_asymmetric_8 = asymmetric_dequantize(asymmetric_q_8, asymmetric_scale_8, zero_8)
    abs_error_asymmetric_8 = relative_error(PARAMS, params_deq_asymmetric_8)
    mean_error_asymmetric_8 = quantization_error(PARAMS, params_deq_asymmetric_8)
    return abs_error_asymmetric_8, mean_error_asymmetric_8
def a16():
    (asymmetric_q_16, asymmetric_scale_16, zero_16) = asymmetric_quantization_percentile(PARAMS, 16)
    params_deq_asymmetric_16 = asymmetric_dequantize(asymmetric_q_16, asymmetric_scale_16, zero_16)
    abs_error_asymmetric_16 = relative_error(PARAMS, params_deq_asymmetric_16)
    mean_error_asymmetric_16 = quantization_error(PARAMS, params_deq_asymmetric_16)
    return abs_error_asymmetric_16, mean_error_asymmetric_16
def a32():
    (asymmetric_q_32, asymmetric_scale_32, zero_32) = asymmetric_quantization_percentile(PARAMS, 32)
    params_deq_asymmetric_32 = asymmetric_dequantize(asymmetric_q_32, asymmetric_scale_32, zero_32)
    abs_error_asymmetric_32 = relative_error(PARAMS, params_deq_asymmetric_32)
    mean_error_asymmetric_32 = quantization_error(PARAMS, params_deq_asymmetric_32)
    return abs_error_asymmetric_32, mean_error_asymmetric_32

def tot_mean_asymetric():
    abs_error_asymmetric_2, mean_error_asymmetric_2 = a2()
    abs_error_asymmetric_4, mean_error_asymmetric_4 = a4()
    abs_error_asymmetric_8, mean_error_asymmetric_8 = a8()
    abs_error_asymmetric_16, mean_error_asymmetric_16 = a16()
    abs_error_asymmetric_32, mean_error_asymmetric_32 = a32()
    return [mean_error_asymmetric_2, mean_error_asymmetric_4, mean_error_asymmetric_8, mean_error_asymmetric_16, mean_error_asymmetric_32]
def tot_abs_asymetric():
    abs_error_asymmetric_2, mean_error_asymmetric_2 = a2()
    abs_error_asymmetric_2 = np.mean(abs_error_asymmetric_2)
    abs_error_asymmetric_4, mean_error_asymmetric_4 = a4()
    abs_error_asymmetric_4 = np.mean(abs_error_asymmetric_4)
    abs_error_asymmetric_8, mean_error_asymmetric_8 = a8()
    abs_error_asymmetric_8 = np.mean(abs_error_asymmetric_8)
    abs_error_asymmetric_16, mean_error_asymmetric_16 = a16()
    abs_error_asymmetric_16 = np.mean(abs_error_asymmetric_16)
    abs_error_asymmetric_32, mean_error_asymmetric_32 = a32()
    abs_error_asymmetric_32 = np.mean(abs_error_asymmetric_32)
    return [abs_error_asymmetric_2, abs_error_asymmetric_4, abs_error_asymmetric_8, abs_error_asymmetric_16, abs_error_asymmetric_32]
def tot_mean_symmetric():
    abs_error_symmetric_2, mean_error_symmetric_2 = s2()
    abs_error_symmetric_4, mean_error_symmetric_4 = s4()
    abs_error_symmetric_8, mean_error_symmetric_8 = s8()
    abs_error_symmetric_16, mean_error_symmetric_16 = s16()
    abs_error_symmetric_32, mean_error_symmetric_32 = s32()
    return [mean_error_symmetric_2, mean_error_symmetric_4, mean_error_symmetric_8, mean_error_symmetric_16, mean_error_symmetric_32]
def tot_abs_symmetric():
    abs_error_symmetric_2, mean_error_symmetric_2 = s2()
    abs_error_symmetric_2 = np.mean(abs_error_symmetric_2)
    abs_error_symmetric_4, mean_error_symmetric_4 = s4()
    abs_error_symmetric_4 = np.mean(abs_error_symmetric_4)
    abs_error_symmetric_8, mean_error_symmetric_8 = s8()
    abs_error_symmetric_8 = np.mean(abs_error_symmetric_8)
    abs_error_symmetric_16, mean_error_symmetric_16 = s16()
    abs_error_symmetric_16 = np.mean(abs_error_symmetric_16)
    abs_error_symmetric_32, mean_error_symmetric_32 = s32()
    abs_error_symmetric_32 = np.mean(abs_error_symmetric_32)
    return [abs_error_symmetric_2, abs_error_symmetric_4, abs_error_symmetric_8, abs_error_symmetric_16, abs_error_symmetric_32]
SIZE = 1000
#read the PARAMS from the file.txt
PARAMS = []
with open("data/params.txt", "r") as f:
    for line in f:
        PARAMS.append(float(line.strip()))
PARAMS = np.array(PARAMS)

abs_error_symmetric2, mean_error_asymmetric2 = s2()
abs_error_symmetric4, mean_error_asymmetric4 = s4()
abs_error_symmetric8, mean_error_asymmetric8 = s8()
abs_error_symmetric16, mean_error_asymmetric16 = s16()


"""
colors = ["#ffffcc", "#a1dab4", "#41b6c4", "#2c7fb8", "#253494"]
my_cmap = ListedColormap(colors, name="my_cmap")
plt.subplot(1, 4, 1)
plt.xlabel("Numero dell'esempio")
plt.ylabel("Percentuale errore relativo")
plt.scatter(np.arange(SIZE), abs_error_symmetric2, c=abs_error_symmetric2, cmap='plasma_r')
plt.title("Errore relativo simmetrico 2bit")
plt.plot()
# Crea il secondo grafico
plt.subplot(1, 4, 2)
plt.xlabel("Numero dell'esempio")
plt.scatter(np.arange(SIZE), abs_error_symmetric4, c=abs_error_symmetric4, cmap='plasma_r')
plt.title("Errore relativo simmetrico 4bit")
plt.plot()
plt.subplot(1, 4, 3)
plt.xlabel("Numero dell'esempio")
plt.scatter(np.arange(SIZE), abs_error_symmetric8, c=abs_error_symmetric8, cmap='plasma_r')
plt.title("Errore relativo simmetrico 8bit")
plt.plot()
plt.subplot(1, 4, 4)
plt.xlabel("Numero dell'esempio")
plt.scatter(np.arange(SIZE), abs_error_symmetric16, c=abs_error_symmetric16, cmap='plasma_r')
plt.title("Errore relativo simmetrico 16bit")
plt.plot()
"""
plt.subplot(1, 2, 1)
plt.xlabel("Bit di quantizzazione")
plt.ylabel("Errore medio")
plt.title("Errore relativo medio Asimmetrico")
error_percentile_asy = tot_mean_asymetric()
print(type(error_percentile_asy))
plt.plot([2, 4, 8, 16, 32], error_percentile_asy,'o-', color="darkred")
plt.xticks([2, 4, 8, 16, 32])

plt.subplot(1, 2, 2)
plt.xlabel("Bit di quantizzazione")
plt.ylabel("Errore medio")
plt.title("Errore relativo medio Simmetrico")
error_percentile_sy = tot_mean_symmetric()
plt.plot([2, 4, 8, 16, 32], error_percentile_sy, 'o-', color="darkred")
plt.xticks([2, 4, 8, 16, 32])
plt.show()

