from PIL import Image, ImageDraw

def flood_fill(width, height, x, y, color):
    
    """Crea una imagen en blanco del tamaño especificado y realiza un flood fill en ella
    a partir del punto (x, y) con el color especificado."""
    
    im = Image.new("RGB", (width, height), (255, 255, 255))
    original_color = im.getpixel((x, y))
    stack = [(x, y)]
    
    while stack:
        x, y = stack.pop()
        if x < 0 or x >= width or y < 0 or y >= height:
            continue
        if im.getpixel((x, y)) != original_color:
            continue
        im.putpixel((x, y), color)
        stack.append((x+1, y))
        stack.append((x-1, y))
        stack.append((x, y+1))
        stack.append((x, y-1))
    
    return im

# Ejemplo de uso:
im = flood_fill(200, 100, 50, 50, (255, 0, 0))  # Crea una imagen de 100x100 y la rellena con rojo a partir del punto (50, 50)
im.show()