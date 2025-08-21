import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sgl
from src.utils.grapher import continuous_plot

def continuous_sin(frequency):

    amplitude = 1
    number_of_points = 10000
    time_initial = 0
    time_final = 5
    time = np.linspace(time_initial, time_final, number_of_points)
    x_t = amplitude * np.sin(2 * np.pi * frequency * time)
    return x_t, time


def sine_plotter(sine_signal,frequency,time):
    title = f"Continuous Signal: Sine Wave Signal {frequency} of frequency"
    xlabel_cont = 'Time [s]'
    ylabel = 'Amplitude'
    continuous_plot(
            time, sine_signal,
            title=f'{title}',
            graph_label='Continuous',
            x_label=xlabel_cont,
            y_label=ylabel
            )
