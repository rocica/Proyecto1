import matplotlib.pyplot as plt


def draw_rectangle_dda(x1, y1, x2, y2):
    """
    Draw a rectangle using DDA algorithm.
    Args:
        x1 (int): x-coordinate of top-left corner
        y1 (int): y-coordinate of top-left corner
        x2 (int): x-coordinate of bottom-right corner
        y2 (int): y-coordinate of bottom-right corner
    """
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steps = max(dx, dy)
    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1

    points = []
    for i in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_increment
        y += y_increment

    return points


# Draw a rectangle with DDA algorithm
x1 = 0
y1 = 0
x2 = 100
y2 = 50
rectangle_points = draw_rectangle_dda(x1, y1, x2, y2)

# Draw a square with DDA algorithm
x1 = 40
y1 = 60
x2 = 80
y2 = 80
square_points = draw_rectangle_dda(x1, y1, x2, y2)

# Plot the points using matplotlib
for x, y in rectangle_points:
    plt.plot(x, y, 'r.')  # red dots for rectangle
for x, y in square_points:
    plt.plot(x, y, 'g.')  # green dots for square

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Rectangle and Square using DDA Algorithm')
plt.grid(True)
plt.show()
