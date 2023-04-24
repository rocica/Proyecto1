import turtle
import tkinter as tk

def dibujar_cuadrado():
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.penup()
    t.goto(0, 0)
    t.pendown()

def dibujar_rectangulo():
    t.penup()
    t.goto(-100, -50)
    t.pendown()
    for _ in range(2):
        t.forward(200)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.penup()
    t.goto(0, 0)
    t.pendown()

#BOTONES TKINTER
def on_boton_cuadrado():
    dibujar_cuadrado()
    t.clear()

def on_boton_rectangulo():
    dibujar_rectangulo()
    t.clear()

#pantalla de turtle
pantalla = turtle.Screen()
pantalla.bgcolor("white")

#objeto turtle
t = turtle.Turtle()

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
