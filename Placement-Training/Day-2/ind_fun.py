#Indirect Recursion

def even(n, limit):
    if n > limit:
       return
    print("Even:", n + 1)
    odd(n + 1, limit)

def odd(n, limit):
    if n > limit:
        return
    print("Odd:", n - 1)
    even(n + 1, limit)

n = int(input("Enter the limit: "))

odd(0,  n) 