import matplotlib.pyplot as plt
import tkinter as tk


def dibujar_cuadrado():
    vertices = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)] #Se defininen los vértices del cuadrado

    #Extraer las coordenadas x & y de los vértices  
    xs = [vertice[0] for vertice in vertices]
    ys = [vertice[1] for vertice in vertices]

    plt.plot(xs, ys) # Se grafica el cuadrado usando la función plot


def dibujar_triangulo():
    vertices = [(0, 0), (1, 0), (0.5, 0.5), (0, 0)]     # Definir los vértices del triángulo

    xs = [vertice[0] for vertice in vertices]
    ys = [vertice[1] for vertice in vertices]

    plt.plot(xs, ys) # Se grafica el cuadrado usando la función plot


def dibujar_figura(figura):
    if figura == "Cuadrado":
        dibujar_cuadrado()
    elif figura == "Triángulo":
        dibujar_triangulo()

    plt.axis('equal') #Función que establece los límites de los ejes de un gráfico en igual escala
    plt.show() #Enseña el gráfico


#TKINTER
root = tk.Tk()
root.title("Dibujante de Figuras")
root.configure(bg="#FFD9EB")
etiqueta_figura = tk.Label(root, text="Seleccionar Figura:")
etiqueta_figura.pack()
boton_cuadrado = tk.Button(
    root, text="Cuadrado", command=lambda: dibujar_figura("Cuadrado"), fg="fuchsia")
boton_cuadrado.pack()
boton_triangulo = tk.Button(
    root, text="Triángulo", command=lambda: dibujar_figura("Triángulo"), fg="fuchsia")
boton_triangulo.pack()
root.mainloop()
