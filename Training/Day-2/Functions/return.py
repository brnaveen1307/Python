print("Function with return values")

def add(a, b):
    sum = a + b
    mul = a * b
    return sum, mul

add, prod = add(30, 10)
print("Add is: ", add)
print("Mul is: ", prod)