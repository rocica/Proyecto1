import turtle
from tkinter import *
from turtle import ScrolledCanvas

# create a turtle object
t = turtle.Turtle()

# draw a closed square shape
t.penup()
t.goto(-100, 100)
t.pendown()
t.color("green")
for i in range(4):
    t.forward(100)
    t.right(90)

# create a scrolled canvas widget
root = Tk()
canvas = ScrolledCanvas(root, width=400, height=400)
canvas.pack(fill=BOTH, expand=YES)

# get the graphics context of the canvas
tcontext = canvas._canvas

# get the pixel data of the canvas
pixel_data = tcontext.tk.call(
    "::tk::photo", "get", tcontext._photo, "-format", "RGB")

# convert the pixel data to a 2D list of pixel values
pixel_values = [[0] * canvas.winfo_width()] * canvas.winfo_height()
for y in range(canvas.winfo_height()):
    for x in range(canvas.winfo_width()):
        r, g, b = pixel_data[y][x]
        if r == g == b == 255:  # white color
            pixel_values[y][x] = 0
        else:  # green color
            pixel_values[y][x] = 1

# apply flood fill algorithm to fill the square with blue color


def flood_fill(image, x, y, target_color, replacement_color):
    """
    Fill a closed area of an image with a new color using the flood fill algorithm.

    Parameters:
    image (list[list[int]]): The image represented as a 2D list of pixel values.
    x (int): The x-coordinate of the starting pixel.
    y (int): The y-coordinate of the starting pixel.
    target_color (int): The color of the pixels to be replaced.
    replacement_color (int): The color to replace the target color with.

    Returns:
    None: The image is modified in place.
    """
    if target_color == replacement_color:
        return

    rows = len(image)
    cols = len(image[0])

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        if image[x][y] == target_color:
            image[x][y] = replacement_color
            if x > 0:
                stack.append((x-1, y))
            if x < rows-1:
                stack.append((x+1, y))
            if y > 0:
                stack.append((x, y-1))
            if y < cols-1:
                stack.append((x, y+1))


flood_fill(pixel_values, 100, 50, 1, 2)

# convert the modified pixel data to a list of RGB tuples
modified_pixel_data = []
for y in range(canvas.winfo_height()):
    row = []
    for x in range(canvas.winfo_width()):
        if pixel_values[y][x] == 0:  # black color
            row.append((0, 0, 0))
        else:  # blue color
            row.append((0, 0, 255))
    modified_pixel_data.append(row)

# put the modified pixel data back to the canvas
tcontext.tk.call(tcontext._photo, "put", " ".join(
    [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in modified_pixel_data]), "-format", "RGB")
