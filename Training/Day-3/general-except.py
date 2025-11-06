lst = [1, 3, 5, 7]
a = 10
b = 10

try:
    div = a / b
    print("Result of Division: ", div)
    print("lst[1] is : ", lst[1])
    print("lst[2] is : ", lst[2])
    print("lst[3] is : ", lst[3])
    print("lst[4] is : ", lst[4])

except ZeroDivisionError as e:
    print("You are trying to divide an int number by zero.")
    print("e Value: ", e)
except Exception as e:
    print("e Value: ", e)

