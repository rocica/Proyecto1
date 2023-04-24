import turtle

# Crear el turtlr
t = turtle.Turtle()

# Velocidad del cursor
t.speed('normal')

# Color de la pluma
t.pencolor('red')

# Color interno
t.fillcolor('pink')

# Donde la pluma empieza
t.penup()
t.goto(0, 0)
t.pendown()

# Se dibuja el rectangulo
width = 100
height = 50
t.begin_fill()
for i in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
t.end_fill()

t.clear()

# Rota el cursor 45°
t.right(45)

# Mover el cursor para la figura rotada
t.penup()
t.goto(0, 0)
t.pendown()

# Se hace el mismo rectangulo en una direección diferente
t.begin_fill()
for i in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
t.end_fill()

# Mantiene la pantalla
turtle.done()
