import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sgl
from src.utils.grapher import combined_plot

def continuous_sine(amplitude, frequency, phase, K):
    signal_xt = [0, 0] 
    for i in range(2):
        if K > 0:
            amplitude = frequency = 1
            phase = 0 
        number_of_points = 10000
        time_initial = 0
        time_final = 5
        time = np.linspace(time_initial, time_final, number_of_points)
        x_t = amplitude * np.sin((2 * np.pi * frequency * time) + phase)
        signal_xt[K] = x_t
        K=K+1
    K=0
    return signal_xt, time

def discrete_sine(amplitude, frequency, phase, K):
    signal_xtn = [0, 0] 
    for i in range(2):
        if K > 0:
            amplitude = frequency = 1
            phase = 0 
        fs = 20
        ts = 1 / fs
        samples = 100
        n = np.arange(samples)
        time_disc = n * ts
        x_tn = amplitude * np.sin((2 * np.pi * frequency * time_disc)+phase)
        signal_xtn[K] = x_tn
        K=K+1
    K=0
    return signal_xtn, time_disc
    
def signal_plotter(signal_xt, time, signal_xtn, time_disc):
    titles = "Sine Wave Signal"
    xlabel_cont = 'Time [s]'
    xlabel_disc = 'Samples'
    ylabel = 'Amplitude'
    
    for i in range(2):
        combined_plot(
            time, signal_xt[i],
            time_disc, signal_xtn[i],
            title=f'Continuous and Discrete Signal: {titles}',
            cont_label='Continuous',
            disc_label='Discrete',
            x_label=xlabel_cont,
            y_label=ylabel
        )
