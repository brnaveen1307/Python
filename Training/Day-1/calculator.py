a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

choice = int(input("Enter the choice: 1-Add, 2-Sub, 3-Mul, 4-Div, 5-Exit: "))

if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice == 3:
    print(a * b)
elif choice == 4:
    print(a / b)
else:
    exit(0)