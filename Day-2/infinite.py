print("Enter two numbers: ")
a, b = (int(input()), int(input()))

while(True):
    choice = int(input("Enter your choice: 1-Add, 2-Sub, 3-Mul, 4-Div, 5-Exit: "))
    if(choice == 1):
        res = a + b
        print("Sum of ", a, "and ", b, "is ", res)
    elif(choice == 2):
        res = a - b
        print("Difference of ", a, "and ", b, "is ", res)

    elif(choice == 3):
        res = a * b
        print("Product of ", a, "and ", b, "is ", res)

    elif(choice == 4):
        res = a / b
        print("Division of ", a, "and ", b, "is ", res)

    elif(choice == 5):
        break

    else:
        print("Invalid choice!")