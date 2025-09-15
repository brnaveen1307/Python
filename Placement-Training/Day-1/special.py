num = int(input("Enter a two-digit number: "))

if num < 10 or num > 99:
    print("Please enter a valid two-digit number")
else:
    first = num // 10
    second = num % 10
    result = (first * second) + (first + second)

    if(result == num):
        print(num, " is a Special number")
    else:
        print(num, " is not a Special number") 