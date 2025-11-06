
a = 10
b = 10

try: 
    div = a / b
    print('Result of Division: ', div)

except ZeroDivisionError as e:
    print("You are trying to divide an int num by zero")
    print("e Value: ", e)


print("Value of a: ", a)
print("Value of b: ", b)