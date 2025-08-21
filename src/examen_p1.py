import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sgl

from src.utils.grapher import combined_plot

def DFT(fm, fc, m):
    fs = 50
    ts = 1 / fs
    
    number_of_points = 10000
    time_initial = 0
    time_final = 5
    t = np.linspace(time_initial, time_final, number_of_points)
    N = int(time_final*fs)
    n = np.arange(N) #N muestras
    
    x_t = (1+m* np.cos(2*np.pi*fm*t) )*np.sin(2*np.pi*fc*t) #Continua
    x_n = (1+m* np.cos(2*np.pi*fm*(n/fs)) )*np.sin(2*np.pi*fc*(n/fs)) #disscreta
    
    X = np.fft.fft(x_n)
    frequency = np.fft.fftfreq(N, ts)
                                            
    half_N = N // 2
    f_pos = frequency[:half_N]
    X_pos = X[:half_N]
    X_mag = np.abs(X_pos)/N
    resolution = fs/N

    peaks_indices = np.argpartition(X_mag, -5)[-5:]
    peaks_freqs = f_pos[peaks_indices]
    peaks_magnitudes = X_mag[peaks_indices]

    p_order = np.argsort(peaks_freqs)
    peaks_freqs = peaks_freqs[p_order]
    peaks_magnitudes = peaks_magnitudes[p_order]

    return peaks_freqs, peaks_magnitudes, resolution, f_pos, X_mag;
