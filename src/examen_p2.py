import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sgl

def señal_ruido(fs=256, duracion=6, f1=8, f2=20, ruido_amp=0.3):
    N = int(fs*duracion)
    ts = 1 / fs
    n = np.arange(N)
    x_n = np.sin(2*np.pi*f1*n*ts) + (0.5*np.sin(2*np.pi*f2*n*ts))
    ruido = ruido_amp*np.random.normal(0, 1, N)
    x_ruido = x_n+ruido
    return n, ts, x_n, x_ruido

def señal_dft(x_n, fs):
    N = len(x_n)
    ts = 1 / fs
    X = np.fft.fft(x_n)
    freq = np.fft.fftfreq(N, ts)
    half_N = N // 2
    f_pos = freq[:half_N]
    X_pos = X[:half_N]
    X_mag = np.abs(X_pos) / N
    resolution = fs / N
    return f_pos, X_mag, resolution
