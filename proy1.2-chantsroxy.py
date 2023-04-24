from PIL import Image, ImageDraw
import tkinter as tk
from PIL import ImageTk

# Crear una imagen con fondo blanco
ancho = 300
alto = 200
image = Image.new("RGB", (ancho, alto), "white")
draw = ImageDraw.Draw(image)

# Definir los vértices del triángulo
vertices = [(50, 150), (150, 50), (250, 150)]

# Dibujar el triángulo
draw.polygon(vertices, fill=None, outline="black")

# Realizar el algoritmo de relleno de área (flood fill) comenzando desde un punto


def flood_fill(image, x, y, fill_color):
    """
    Realizar el algoritmo de relleno de área (flood fill) en una imagen comenzando desde (x, y)
    con el color de relleno fill_color.
    """
    ancho, alto = image.size
    pixels = image.load()
    target_color = pixels[x, y]

    if target_color == fill_color:
        return

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if x >= 0 and x < ancho and y >= 0 and y < alto:
            if pixels[x, y] == target_color:
                pixels[x, y] = fill_color
                stack.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])


# Realizar el algoritmo de relleno de área (flood fill) comenzando desde el centro del triángulo
flood_fill(image, ancho//2, alto//2, (255, 0, 255))

# Crear ventana de Tkinter
root = tk.Tk()
root.title("Flood Fill")
root.geometry(f"{ancho}x{alto}")

# Crear una etiqueta (Label) para mostrar la imagen
label = tk.Label(root)
label.pack()

# Convertir la imagen a un objeto PhotoImage
image_tk = ImageTk.PhotoImage(image)

# Actualizar la etiqueta con la imagen
label.config(image=image_tk)
label.image = image_tk

# Ejecutar el ciclo de eventos de Tkinter
root.mainloop()
