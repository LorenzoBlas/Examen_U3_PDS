# Proyecto de Señales Continuas y Discretas

---

## Tabla de Contenidos

1. [Descripción](#descripción)  
2. [Tecnologías](#tecnologías)  
3. [Funcionamiento](#funcionamiento)  
4. [Instalación](#instalación)  
5. [Uso](#uso)  
6. [Estructura del Proyecto](#estructura-del-proyecto)  
7. [Agradecimientos](#agradecimientos)  

---

## Descripción

Este proyecto genera y grafica señales continuas y discretas de cuatro tipos: senoidal, exponencial, triangular y cuadrada. Permite visualizar cada señal por separado y también compararlas superpuestas para facilitar su análisis.

---

## Tecnologías

- Python 3.10.9  
- NumPy == 2.2.6
- Matplotlib == 3.10.3
- SciPy == 1.15.3  

---

## Funcionamiento

El código genera señales continuas y discretas con parámetros definidos (frecuencia, amplitud, tiempo/muestras). Luego, utiliza funciones de graficado para mostrar las señales continuas, discretas y ambas juntas en gráficos separados.

---

## Instalación

1. Clonar este repositorio: "git clone https://github.com/LorenzoBlas/Act_1_PDS.git"
2. Instalar dependencias: pip install -r requeriments.txt


---

## Uso

Ejecutar el script principal para generar y visualizar las señales:  

python3.exe main.py act_i donde i sea el numero de la actividad a ejecutar.

Se mostrarán las gráficas de las señales continuas, discretas y combinadas, una por una para cada tipo de señal.

---
## Estructura del Proyecto
```
project-root/
├── src/
│ ├── utils/
│ │ └── grapher.py
│ ├── main.py
├── README.md
├── requirements.txt
```
---

## Agradecimientos

Gracias a la comunidad de Python y a los autores de las librerías NumPy, Matplotlib y SciPy por sus herramientas fundamentales para este proyecto y a mi gato que lo quiero mucho.
