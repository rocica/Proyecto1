import turtle

# Crear el turtle
t = turtle.Turtle()
t.speed('normal')  # Velocidad del cursor
t.pencolor('red')
t.fillcolor('pink')

# Función que dibuja rectángulo


def draw_rectangle():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    ancho = 100
    alto = 50
    t.begin_fill()
    for i in range(2):
        t.forward(ancho)
        t.right(90)
        t.forward(alto)
        t.right(90)
    t.end_fill()


draw_rectangle()

t.clear()

# Rota el cursor 45°
t.right(45)
draw_rectangle()

turtle.done()
