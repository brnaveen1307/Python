
#Sum of Digits

def sum_of_digits(n, sum = 0):
    if n == 0:
        return sum
    return sum_of_digits(n // 10, sum + (n % 10))

num = int(input("Enter a number: "))
print("Sum of Digits of", num, "is", sum_of_digits(num))