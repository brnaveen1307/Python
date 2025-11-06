a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

try:
    div = a / b
    print("Result of Division: ", div)
except Exception as e:
    print("Exception: ", e)
else:
    print("Code Executed Successfully!")
