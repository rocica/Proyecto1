import turtle
import tkinter as tk

def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    err = dx - dy
    while x0 != x1 or y0 != y1:
        turtle.goto(x0, y0)
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    turtle.goto(x1, y1)

def dibujar_cuadrado():
    vertices = [(0, 0), (100, 0), (100, 100), (0, 100), (0, 0)]

    for i in range(len(vertices) - 1):
        x0, y0 = vertices[i]
        x1, y1 = vertices[i+1]
        bresenham_line(x0, y0, x1, y1)

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

def dibujar_rectangulo():
    vertices = [(0, 0), (200, 0), (200, 100), (0, 100), (0, 0)]

    for i in range(len(vertices) - 1):
        x0, y0 = vertices[i]
        x1, y1 = vertices[i+1]
        bresenham_line(x0, y0, x1, y1)

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

#BOTONES TKINTER
def on_boton_cuadrado():
    turtle.clear()
    dibujar_cuadrado()

def on_boton_rectangulo():
    turtle.clear()
    dibujar_rectangulo()

#pantalla de turtle
pantalla = turtle.Screen()
pantalla.bgcolor("white")

#objeto turtle
turtle = turtle.Turtle()
turtle.speed(0)

#TKINTER
root = tk.Tk()
root.title("Dibujante de Formas")
root.configure(bg="white")
boton_cuadrado = tk.Button(root, text="Cuadrado", command=on_boton_cuadrado, fg="pink")
boton_cuadrado.pack()
boton_rectangulo = tk.Button(root, text="Rectángulo", command=on_boton_rectangulo, fg="pink")
boton_rectangulo.pack()
root.mainloop()

turtle.done() #mantiene la ventana abierta, si se quita no abre
