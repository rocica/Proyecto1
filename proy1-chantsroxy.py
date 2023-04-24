import matplotlib.pyplot as plt
import tkinter as tk


def dibujar_cuadrado():
    # Definir los vértices del cuadrado
    vertices = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]

    # Extraer las coordenadas x e y de los vértices
    xs = [vertice[0] for vertice in vertices]
    ys = [vertice[1] for vertice in vertices]

    # Graficar el cuadrado
    plt.plot(xs, ys)


def dibujar_triangulo():
    # Definir los vértices del triángulo
    vertices = [(0, 0), (1, 0), (0.5, 0.5), (0, 0)]

    # Extraer las coordenadas x e y de los vértices
    xs = [vertice[0] for vertice in vertices]
    ys = [vertice[1] for vertice in vertices]

    # Graficar el triángulo
    plt.plot(xs, ys)


def dibujar_figura(figura):
    if figura == "Cuadrado":
        dibujar_cuadrado()
    elif figura == "Triángulo":
        dibujar_triangulo()

    # Establecer la relación de aspecto en 'igual' para asegurar una forma cuadrada
    plt.axis('equal')
    # Mostrar la gráfica
    plt.show()


# Crear la ventana de tkinter
root = tk.Tk()
root.title("Dibujante de Figuras")

# Establecer el color de fondo en rosa claro
root.configure(bg="#FFD9EB")

# Crear una etiqueta para la selección de figura
etiqueta_figura = tk.Label(root, text="Seleccionar Figura:")
etiqueta_figura.pack()

# Crear botones para la selección de figura con color fucsia
boton_cuadrado = tk.Button(
    root, text="Cuadrado", command=lambda: dibujar_figura("Cuadrado"), fg="fuchsia")
boton_cuadrado.pack()
boton_triangulo = tk.Button(
    root, text="Triángulo", command=lambda: dibujar_figura("Triángulo"), fg="fuchsia")
boton_triangulo.pack()

# Iniciar el tkinter
root.mainloop()
