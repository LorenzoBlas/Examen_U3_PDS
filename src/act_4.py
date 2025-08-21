import numpy as np
from src.utils.grapher import discrete_plot, continuous_plot
V_FS = 5.0 

def run(bits):
    Calc_niveles= 2 ** bits
    Tamaño_Paso= V_FS / (2 ** bits - 1)
    Calc_Res_Por = 100 / (2 ** bits - 1)
    niveles = Calc_niveles
    tamano_paso = Tamaño_Paso
    resolucion_pct = Calc_Res_Por

    print(f"Número total de niveles: {niveles}")
    print(f"Tamaño del paso: {tamano_paso:.6f} V")
    print(f"Resolución porcentual: {resolucion_pct:.4f} %")

    # Generar entradas digitales de 0 a 2^N - 1
    entradas = np.arange(niveles)
    # Calcular salida analógica correspondiente
    salida_analogica = tamano_paso * entradas
    
    x_cont = np.linspace(0, niveles - 1, 1000)  # Más puntos para suavizar
    y_cont = x_cont * tamano_paso

    # Graficar salida analógica vs entrada digital
    discrete_plot(
        entradas, salida_analogica,
        title=f"Salida Analógica del DAC - {bits} bits",
        graph_label="Salida DAC",
        x_label="Entrada Digital",
        y_label="Voltaje de Salida (V)"
    )
    
    continuous_plot(
        x_cont, y_cont,
        title=f"Salida Digital del DAC - {bits} bits",
        graph_label="Salida DAC",
        x_label="Entrada Digital",
        y_label="Voltaje de Salida (V)"
    )
