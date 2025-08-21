# Proyecto: Análisis de Señales mediante Transformada Discreta de Fourier (DFT)

Este proyecto contiene dos actividades (exámenes) para aplicar técnicas de procesamiento digital de señales usando la DFT en Python. Cada examen se centra en un análisis espectral diferente y en aspectos específicos del procesamiento de señales.

---

## Examen 1 - Señal Modulada y Análisis Espectral

### Objetivos
- Generar una señal modulada en amplitud (AM) con parámetros dados.
- Aplicar la DFT para extraer información espectral de la señal muestreada.
- Identificar los picos espectrales, estimar sus frecuencias y amplitudes relativas.
- Calcular y entender la resolución en frecuencia basada en la frecuencia de muestreo y número de muestras.

### Parámetros principales
- Frecuencia moduladora \(f_m = 0.5\) Hz
- Frecuencia portadora \(f_c = 8\) Hz
- Índice de modulación \(m = 0.5\)
- Frecuencia de muestreo \(f_s = 50\) Hz
- Duración de la señal: 5 segundos

### Uso
- Ejecutar el archivo `examen_p1.py`.
- Se generarán las gráficas de la señal muestreada y su espectro.
- El programa identifica y muestra los principales picos en el espectro.

---

## Examen 2 - Análisis Espectral de Señal con Ruido

### Objetivos
- Generar una señal discreta compuesta por dos senoidales.
- Añadir ruido gaussiano blanco para observar su efecto en el dominio temporal y espectral.
- Calcular la DFT de la señal limpia y ruidosa.
- Identificar picos espectrales presentes y analizar cómo el ruido afecta el espectro.
- Calcular y analizar la resolución espectral.

### Parámetros principales
- Frecuencia de muestreo \(f_s = 256\) Hz
- Duración: 6 segundos (\(N = 1536\) muestras)
- Frecuencias senoidales \(f_1 = 8\) Hz, \(f_2 = 20\) Hz
- Amplitud del ruido: 0.3 (relativa)

### Uso
- Ejecutar el archivo `examen_p2.py`.
- Se muestran las gráficas de las señales limpias y con ruido junto con sus espectros.
- Se comparan visualmente y analíticamente los efectos del ruido.

---

## Requisitos comunes

- Python 3.x instalado.
- Librerías: `numpy`, `matplotlib`.
- Módulo `grapher.py` disponible para graficación (funciones: `continuous_plot`, `discrete_plot`, `combined_plot`).

## Cómo ejecutar

1. Clonar o descargar el proyecto completo localmente.
2. Asegurarse que Python 3 y las librerías estén instaladas (ejemplo con pip):

