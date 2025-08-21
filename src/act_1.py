import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sgl
from src.utils.grapher import continuous_plot, discrete_plot, combined_plot



def continuous_signals():
    frequency = 2
    amplitude = 1
    number_of_points = 10000
    time_initial = 0#-1
    time_final = 5
    time = np.linspace(time_initial, time_final, number_of_points)
    u_t = np.where(time >= 0, 1, 0)
        
    x1_t = amplitude * np.sin(2 * np.pi * frequency * time) #Sine
    x2_t = amplitude * np.exp(-2 * time) * u_t # Exp
    x3_t = amplitude * sgl.sawtooth(2 * np.pi * frequency * time, 0.5) #Tri
    x4_t = amplitude * sgl.square(2* np.pi * frequency * time) #Sqare
    
    signals = [x1_t,x2_t,x3_t,x4_t]
    return time, signals
   
def discrete_signals():
    frequency = 2
    amplitude = 1
    fs = 20
    ts = 1 / fs
    #number_of_points = 10000
    time_initial = -1
    time_final = 5
    
    samples = 100
    n = np.arange(samples)
    time_disc = n * ts
    
    
    ut_disc = np.where(time_disc >= 0, 1, 0)
    
    x1_tn = amplitude * np.sin(2 * np.pi * frequency * time_disc )
    x2_tn = amplitude * np.exp(-2 * time_disc) * ut_disc
    x3_tn = amplitude * sgl.sawtooth(2 * np.pi * frequency * time_disc, 0.5)
    x4_tn = amplitude * sgl.square(2 * np.pi * frequency * time_disc)
    n_signals = [x1_tn,x2_tn,x3_tn,x4_tn]
    
    return time_disc, n_signals
    

    
def plot_all_signals(time_cont, signals_cont, time_disc, signals_disc):
    titles = [
        'Sine Wave Signal',
        'Exponential Signal',
        'Triangular Signal',
        'Square Signal'
    ]
    xlabel_cont = 'Time [s]'
    xlabel_disc = 'Samples'
    ylabel = 'Amplitude'

    for i in range(4):
        # Señal continua
        continuous_plot(
            time_cont, signals_cont[i],
            title=f'Continuous Signal: {titles[i]}',
            graph_label='Continuous',
            x_label=xlabel_cont,
            y_label=ylabel
        )
        # Señal discreta
        discrete_plot(
            time_disc, signals_disc[i],
            title=f'Discrete Signal: {titles[i]}',
            graph_label='Discrete',
            x_label=xlabel_disc,
            y_label=ylabel
        )
        # Ambas señales juntas
        combined_plot(
            time_cont, signals_cont[i],
            time_disc, signals_disc[i],
            title=f'Continuous and Discrete Signal: {titles[i]}',
            cont_label='Continuous',
            disc_label='Discrete',
            x_label=xlabel_cont,
            y_label=ylabel
        )
