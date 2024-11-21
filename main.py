# Para ecuaciones diferenciales homogeneas de orden n

import sympy as sp
from tkinter import Tk, Label, Entry, Button, StringVar, Frame

def calcular_solucion():
    try:
        # Leer el orden n
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError("El orden debe ser un entero positivo.")

        # Leer los coeficientes
        coeficientes = [float(entries[i].get()) for i in range(n + 1)]

        # Definir la ecuación característica
        r = sp.symbols('r')
        ecuacion_caracteristica = sum(coef * r**(n - i) for i, coef in enumerate(coeficientes))

        # Calcular raíces
        raices = sp.solve(ecuacion_caracteristica, r)

        # Generar soluciones independientes
        x = sp.Symbol('x')
        soluciones_independientes = []
        for raiz in raices:
            if sp.im(raiz) == 0:  # Raíz real
                multiplicidad = raices.count(raiz)
                for k in range(multiplicidad):
                    soluciones_independientes.append(x**k * sp.exp(raiz * x))
            else:  # Raíz compleja
                alpha, beta = sp.re(raiz), sp.im(raiz)
                soluciones_independientes.extend([
                    sp.exp(alpha * x) * sp.cos(beta * x),
                    sp.exp(alpha * x) * sp.sin(beta * x)
                ])

        # Solución general
        constantes = sp.symbols(f'C1:C{len(soluciones_independientes) + 1}')
        solucion_general = sum(c * sol for c, sol in zip(constantes, soluciones_independientes))

        # Mostrar resultados
        resultado_texto.set(f"""Ecuación característica: {ecuacion_caracteristica}
Raíces: {raices}
Soluciones independientes: {', '.join(map(str, soluciones_independientes))}
Solución general: {solucion_general}
""")
    except Exception as e:
        resultado_texto.set(f"Error: {str(e)}")

# Crear interfaz
root = Tk()
root.title("Ecuación Diferencial de Orden n")

Label(root, text="Orden de la ecuación diferencial (n):").pack()
entry_n = Entry(root)
entry_n.pack()

frame_inputs = Frame(root)
frame_inputs.pack()

entries = []

def generar_campos():
    for widget in frame_inputs.winfo_children():
        widget.destroy()
    n = int(entry_n.get())
    for i in range(n + 1):
        Label(frame_inputs, text=f"Coeficiente a{i}:").grid(row=i, column=0)
        entry = Entry(frame_inputs)
        entry.grid(row=i, column=1)
        entries.append(entry)

Button(root, text="Generar campos", command=generar_campos).pack()

Button(root, text="Calcular", command=calcular_solucion).pack()

resultado_texto = StringVar()
Label(root, textvariable=resultado_texto, justify="left").pack()

root.mainloop()
