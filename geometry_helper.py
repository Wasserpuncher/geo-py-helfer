import math

# 2D Shapes

def circle_area(radius: float) -> float:
    """Calculates the area of a circle."""
    if radius <= 0:
        raise ValueError("Radius muss positiv sein.")
    return math.pi * (radius ** 2)

def circle_circumference(radius: float) -> float:
    """Calculates the circumference of a circle."""
    if radius <= 0:
        raise ValueError("Radius muss positiv sein.")
    return 2 * math.pi * radius

def rectangle_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle."""
    if length <= 0 or width <= 0:
        raise ValueError("Länge und Breite müssen positiv sein.")
    return length * width

def rectangle_perimeter(length: float, width: float) -> float:
    """Calculates the perimeter of a rectangle."""
    if length <= 0 or width <= 0:
        raise ValueError("Länge und Breite müssen positiv sein.")
    return 2 * (length + width)

def triangle_area(base: float, height: float) -> float:
    """Calculates the area of a triangle (given base and height)."""
    if base <= 0 or height <= 0:
        raise ValueError("Basis und Höhe müssen positiv sein.")
    return 0.5 * base * height

# 3D Shapes

def cube_volume(side: float) -> float:
    """Calculates the volume of a cube."""
    if side <= 0:
        raise ValueError("Seitenlänge muss positiv sein.")
    return side ** 3

def cube_surface_area(side: float) -> float:
    """Calculates the surface area of a cube."""
    if side <= 0:
        raise ValueError("Seitenlänge muss positiv sein.")
    return 6 * (side ** 2)

def sphere_volume(radius: float) -> float:
    """Calculates the volume of a sphere."""
    if radius <= 0:
        raise ValueError("Radius muss positiv sein.")
    return (4/3) * math.pi * (radius ** 3)

def sphere_surface_area(radius: float) -> float:
    """Calculates the surface area of a sphere."""
    if radius <= 0:
        raise ValueError("Radius muss positiv sein.")
    return 4 * math.pi * (radius ** 2)
