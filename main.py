import sys
from src.examen_p1 import DFT
from src.examen_p2 import señal_ruido, señal_dft
from src.utils.grapher import discrete_plot, continuous_plot


def main(arg):
    if arg[1] == "examen_p1":
        fm = 0.5
        fc = 8.0
        m = 0.5
        peaks_freqs, peaks_magnitudes, resolution, f_pos, X_mag = DFT(fm, fc, m)
        discrete_plot(peaks_freqs, peaks_magnitudes, title="Picos espectrales", graph_label="Magnitud", x_label="Frecuencia [Hz]", y_label="Magnitud relativa")
        discrete_plot(f_pos, X_mag, title="Espectro de magnitud completo", graph_label="Magnitud", x_label="Frecuencia [Hz]", y_label="Magnitud normalizada")
        
    elif arg[1] == "examen_p2":
        fs = 256
        duracion = 6
        f1, f2 = 8, 20
        n, ts, x_n, x_ruido = señal_ruido(fs, duracion, f1, f2)
        f_pos, X_mag, resolution = señal_dft(x_n, fs)
        _, X_mag_ruido, _ = señal_dft(x_ruido, fs)
    
        continuous_plot(n * ts, x_n, title="Señal original en tiempo", graph_label="x[n]", x_label="Tiempo [s]", y_label="Amplitud") #Limpia
        discrete_plot(f_pos, X_mag, title="Espectro de magnitud señal original", graph_label="Magnitud", x_label="Frecuencia [Hz]", y_label="Magnitud normalizada") #DFT Limpia
        continuous_plot(n * ts, x_ruido, title="Señal con ruido en tiempo", graph_label="x_ruido[n]", x_label="Tiempo [s]", y_label="Amplitud") #Ruido
        discrete_plot(f_pos, X_mag_ruido, title="Espectro de magnitud señal con ruido", graph_label="Magnitud ruido", x_label="Frecuencia [Hz]", y_label="Magnitud normalizada") #DFT Ruio
    
if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Argumento fuera de los parametros tolerados")
        print("Pruebe con: examen_p1 o examen_p2")
        
