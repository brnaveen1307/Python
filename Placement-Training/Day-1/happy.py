num = int(input("Enter a number: "))

while num != 1 and num != 4:
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit * digit
        temp //= 10
    num =sum

if num == 1:
    print("Happy number")
else:
    print("Not a happy number")