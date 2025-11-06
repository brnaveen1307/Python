a = 10
b = 10

lst = [2, 3]

try:
    div = a / b
    print("Result of Division: ", div)
    print("lst[1] is: ", lst[1])
except Exception (IndexError, ZeroDivisionError) as e:
    print("e Value:", e)