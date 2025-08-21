import sys
from src.examen_p1 import DFT
from src.utils.grapher import discrete_plot, continuous_plot


def main(arg):
    if arg[1] == "examen_p1":
        fm = 0.5
        fc = 8.0
        m = 0.5
        peaks_freqs, peaks_magnitudes, resolution, f_pos, X_mag = DFT(fm, fc, m)

        discrete_plot(peaks_freqs, peaks_magnitudes, title="Picos espectrales", graph_label="Magnitud", x_label="Frecuencia [Hz]", y_label="Magnitud relativa")
        discrete_plot(f_pos, X_mag, title="Espectro de magnitud completo", graph_label="Magnitud", x_label="Frecuencia [Hz]", y_label="Magnitud normalizada")
       
if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Argumento fuera de los parametros tolerados")
        print("Pruebe con: examen_p1")
        
