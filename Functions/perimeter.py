def calculate_perimeter(shape, dimensions):
    if shape == "rectangle":
        length = dimensions["length"]
        width = dimensions["width"]
        return 2 * (length + width)

    elif shape == "square":
        side = dimensions["side"]
        return 4 * side

    elif shape == "circle":
        radius = dimensions["radius"]
        return 2 * 3.1416 * radius

    else:
        return "Unsupported shape"

perimeter = calculate_perimeter(
    "rectangle",
    {"length": 30, "width": 20}
)
print("Fence needed:", perimeter, "meters")
