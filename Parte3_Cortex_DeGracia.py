
'''
import turtle

# create a turtle object
t = turtle.Turtle()

# draw a rectangle
t.penup()
t.goto(-100, -50)
t.pendown()
t.color("red")
for i in range(2):
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)

# rotate the rectangle 45 degrees clockwise
t.right(45)

# keep the window open
turtle.done()
'''


import turtle

# create a turtle object
t = turtle.Turtle()

# set the turtle speed
t.speed('normal')

# set the turtle's pen color
t.pencolor('red')

# set the turtle's fill color
t.fillcolor('pink')

# move the turtle to the starting position of the rectangle
t.penup()
t.goto(0, 0)
t.pendown()

# draw a rectangle
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

# rotate the rectangle 45 degrees clockwise
t.right(45)

# move the turtle to the new starting position
t.penup()
t.goto(0, 0)
t.pendown()

# redraw the rectangle with the same dimensions
t.begin_fill()
for i in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
t.end_fill()

# keep the turtle window open
turtle.done()
