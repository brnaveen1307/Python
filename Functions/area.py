import math

def calculate_area(shape, dimensions):
    if shape == "rectangle":
        length = dimensions["length"]
        width = dimensions["width"]
        return length * width

    elif shape == "circle":
        radius = dimensions["radius"]
        return math.pi * radius ** 2

    elif shape == "triangle":
        base = dimensions["base"]
        height = dimensions["height"]
        return 0.5 * base * height

    else:
        return "Unknown shape"

area = calculate_area(
    "rectangle",
    {"length": 10, "width": 8}
)

print(f"Floor area to paint: {area} sq meters")
