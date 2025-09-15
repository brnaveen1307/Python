num = int(input("Enter a number: "))
sum = 0
temp = num
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** digits)
    temp = temp // 10

if sum == num:
    print(num, "is a Armstrong number")
else:
    print(num, "is not a Armstron number")