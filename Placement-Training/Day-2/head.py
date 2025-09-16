#Head Recursion

def print_up(n):
    if n == 0:
        return
    print_up(n - 1)
    print(n)

num = int(input("Enter a number: "))
print_up(num)