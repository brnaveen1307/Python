
a = 10
b = 0

try:
    div = a / b
    print("Result of Division: ", div)

except IndexError as e:
    print("e Vaule: ", e)

finally:
    print("Finally block code")