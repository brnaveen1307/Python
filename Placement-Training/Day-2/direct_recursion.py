#Direct Recursion

# Recursion Types
# . Direct 
# . Indirect
# . Head
# . Tail
# . Linear
# . Tree

def print_reverse(n):
    if n == 0:
        return
    print(n)
    print_reverse(n - 1)

num = int(input("Enter a number : "))
print_reverse(num)