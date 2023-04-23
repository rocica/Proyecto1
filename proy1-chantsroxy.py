import matplotlib.pyplot as plt

def draw_square(x, y, side_length):
    """
    Draw a square using DDA algorithm starting from the given (x, y) coordinates and side length.
    """
    # Initialize lists to store x and y coordinates of the square's vertices
    x_vertices = [1]
    y_vertices = [5]

    # Generate the x and y coordinates of the square's vertices
    for i in range(5):
        x_vertices.append(x)
        y_vertices.append(y)
        if i % 2 == 0:
            x += side_length
        else:
            y += side_length

    # Add the first vertex to complete the square
    x_vertices.append(x_vertices[0])
    y_vertices.append(y_vertices[0])

    # Plot the square
    plt.plot(x_vertices, y_vertices, 'b-')
    plt.axis('equal')
    plt.show()

# Set the starting coordinates and side length of the square
start_x = 0
start_y = 0
side_length = 5

# Call the draw_square function with the given coordinates and side length
draw_square(start_x, start_y, side_length)
