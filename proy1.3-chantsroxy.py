import turtle

# Crear el turtle
t = turtle.Turtle()
t.speed('normal')  # Velocidad del cursor
t.pencolor('red')
t.fillcolor('pink')

# Función que dibuja rectángulo


def draw_rectangle(size):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    ancho = 100 * size
    alto = 50 * size
    t.begin_fill()
    for i in range(2):
        t.forward(ancho)
        t.right(90)
        t.forward(alto)
        t.right(90)
    t.end_fill()


draw_rectangle(1)

t.clear()

# Resize
draw_rectangle(3)

turtle.done()
