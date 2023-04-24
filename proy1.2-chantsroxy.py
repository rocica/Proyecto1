from PIL import Image, ImageDraw
import tkinter as tk
from PIL import ImageTk

# Crear una imagen
ancho = 300
alto = 200
image = Image.new("RGB", (ancho, alto), "white")
draw = ImageDraw.Draw(image)

# Vértices del triángulo
vertices = [(50, 150), (150, 50), (250, 150)]

# Triángulo
draw.polygon(vertices, fill=None, outline="black")

# Función Flood Fill


def flood_fill(image, x, y, fill_color):
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


# Llamar a la función
flood_fill(image, ancho//2, alto//2, (255, 0, 255))

# Tkinter
root = tk.Tk()
root.title("Flood Fill")
root.geometry(f"{ancho}x{alto}")
label = tk.Label(root)
label.pack()
image_tk = ImageTk.PhotoImage(image)
label.config(image=image_tk)
label.image = image_tk

root.mainloop()
