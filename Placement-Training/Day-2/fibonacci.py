#Fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
terms = int(input("Enter the number of terms: "))
series = [fibonacci(i) for i in range(terms)]
print("Fibonacci Series: ", series) #[0 1 1 2 3 5 8 13 21 34]


#Another way for Fibonacci

# def fibonacci_linear(n, a = 0, b = 1):
#     if n == 0:
#         return
#     print(a, end = " ")
#     fibonacci_linear(n - 1, b, a + b)

# num = int(input("Enter the number of terms: "))
# fibonacci_linear(num)