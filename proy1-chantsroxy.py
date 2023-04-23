import matplotlib.pyplot as plt
import tkinter as tk

def draw_square():
    """
    Draw a square using matplotlib.
    """
    # Define the vertices of the square
    vertices = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]

    # Extract x-coordinates and y-coordinates from the vertices
    xs = [vertex[0] for vertex in vertices]
    ys = [vertex[1] for vertex in vertices]

    # Plot the square
    plt.plot(xs, ys)

def draw_triangle():
    """
    Draw an equilateral triangle using matplotlib.
    """
    # Define the vertices of the triangle
    vertices = [(0, 0), (1, 0), (0.5, 0.5), (0, 0)]

    # Extract x-coordinates and y-coordinates from the vertices
    xs = [vertex[0] for vertex in vertices]
    ys = [vertex[1] for vertex in vertices]

    # Plot the triangle
    plt.plot(xs, ys)

def draw_shape(shape):
    """
    Draw the shape based on the user's choice.
    """
    if shape == "Square":
        draw_square()
    elif shape == "Triangle":
        draw_triangle()

    # Set the aspect ratio to 'equal' to ensure square shape
    plt.axis('equal')
    # Show the plot
    plt.show()

# Create the tkinter window
root = tk.Tk()
root.title("Shape Drawer")

# Set the background color to soft pink
root.configure(bg="#FFD9EB")

# Create a label for the shape selection
shape_label = tk.Label(root, text="Select Shape:")
shape_label.pack()

# Create buttons for shape selection with fuchsia color
square_button = tk.Button(root, text="Square", command=lambda: draw_shape("Square"), fg="fuchsia")
square_button.pack()
triangle_button = tk.Button(root, text="Triangle", command=lambda: draw_shape("Triangle"), fg="fuchsia")
triangle_button.pack()

# Start the tkinter event loop
root.mainloop()
