# Para ecuaciones diferenciales homogeneas de orden 2

import sympy as sp
from tkinter import Tk, Label, Entry, Button, StringVar, Text, Frame

def calcular_solucion():
    try:
        # Leer constantes
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Definir la ecuación característica
        r = sp.symbols('r')
        ecuacion_caracteristica = a * r**2 + b * r + c

        # Calcular raíces
        raices = sp.solve(ecuacion_caracteristica, r)

        # Identificar las soluciones
        if len(raices) == 1:  # Raíz doble
            sol1 = sp.exp(raices[0] * sp.Symbol('x'))
            sol2 = sp.Symbol('x') * sol1
        elif sp.im(raices[0]) == 0:  # Raíces reales distintas
            sol1 = sp.exp(raices[0] * sp.Symbol('x'))
            sol2 = sp.exp(raices[1] * sp.Symbol('x'))
        else:  # Raíces complejas
            alpha, beta = sp.re(raices[0]), sp.im(raices[0])
            sol1 = sp.exp(alpha * sp.Symbol('x')) * sp.cos(beta * sp.Symbol('x'))
            sol2 = sp.exp(alpha * sp.Symbol('x')) * sp.sin(beta * sp.Symbol('x'))

        # Solución general
        c1, c2 = sp.symbols('C1 C2')
        solucion_general = c1 * sol1 + c2 * sol2

        # Mostrar resultados
        resultado_texto.set(f"""Ecuación característica: {ecuacion_caracteristica}
Raíces: {raices}
Soluciones independientes: {sol1}, {sol2}
Solución general: {solucion_general}
""")
    except Exception as e:
        resultado_texto.set(f"Error: {str(e)}")

# Crear interfaz
root = Tk()
root.title("Ecuación Diferencial de Segundo Orden")

Label(root, text="Constantes de la ecuación ay'' + by' + cy = 0").pack()

frame_inputs = Frame(root)
frame_inputs.pack()

Label(frame_inputs, text="a: ").grid(row=0, column=0)
entry_a = Entry(frame_inputs)
entry_a.grid(row=0, column=1)

Label(frame_inputs, text="b: ").grid(row=1, column=0)
entry_b = Entry(frame_inputs)
entry_b.grid(row=1, column=1)

Label(frame_inputs, text="c: ").grid(row=2, column=0)
entry_c = Entry(frame_inputs)
entry_c.grid(row=2, column=1)

Button(root, text="Calcular", command=calcular_solucion).pack()

resultado_texto = StringVar()
resultado_label = Label(root, textvariable=resultado_texto, justify="left")
resultado_label.pack()

root.mainloop()
