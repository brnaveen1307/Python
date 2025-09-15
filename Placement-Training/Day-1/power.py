num = int(input("Enter a number: "))

if num > 0 and (num & (num - 1)) == 0:
    print("Power of 2")
else:
    print("Not a Power of 2")