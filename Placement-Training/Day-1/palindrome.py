# n = input("Enter a String: ")

# if n == n [::-1]:
#     print(n, "is a Palindrome")
# else:
#     print(n, "is not a Palindrome")


num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    d = num % 10
    rev = rev * 10 + d
    num = num // 10

if original == rev:
    print(original, "is a Palindrome")
else:
    print(original, "is not a Palindrom")