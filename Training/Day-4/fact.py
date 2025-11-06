def fact(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n * fact(n - 1)

n = int(input("Enter a number: "))
print("Factorial of", n , "is", fact(n))

# lst = [1, 2, 3, 4, 5]
#     prod = 1
#     for i in lst:
#         prod = i * lst
# print(lst)