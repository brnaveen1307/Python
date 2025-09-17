numbers = [1, 2, 3, 4, 5]

rotated = [numbers[-1]] + numbers[:-1]
print("Rotated Right: ", rotated)

numbers = [6, 7, 8, 9, 10]

rotated = numbers[1:] + [numbers[0]]
print("Rotated Left: ", rotated)