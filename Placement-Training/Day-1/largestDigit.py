def largest_digit(num):
    digits = str(num)

    max_digit = '0'

    for digit in digits:
        if digit > max_digit:
            max_digit = digit

    return int(max_digit)

number = int(input("Enter a number(minimum of 6-digits): "))
print("Largest digit of", number, "is", largest_digit(number))