# Resolución de Ecuaciones Diferenciales de Orden n

Este proyecto es una herramienta interactiva para calcular la solución general de ecuaciones diferenciales lineales homogéneas de segundo orden con coeficientes constantes. El programa incluye una interfaz gráfica para ingresar los coeficientes de la ecuación y muestra paso a paso el proceso de resolución.

## Características
1. **Ecuación característica**: Muestra la ecuación característica asociada.
2. **Cálculo de raíces**: Resuelve las raíces de la ecuación característica.
3. **Soluciones independientes**: Muestra las soluciones linealmente independientes.
4. **Solución general**: Genera la solución general con constantes arbitrarias.

## Requisitos
Este proyecto utiliza la biblioteca `sympy` y la interfaz gráfica se desarrolla con `tkinter`, que viene preinstalado en Python. 

## USO
**main.py** funciona con ecuaciones diferenciales de orden n (aún contiene uno 
que otro error).

**main2.py** funciona con ecuaciones diferenciales de orden 2 (ya funciona correctamente).

### Instalación de `sympy`
Si no tienes `sympy` instalado, puedes instalarlo con el siguiente comando:

```bash
pip install sympy
