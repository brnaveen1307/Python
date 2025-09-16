#indirect Recursion

def function_a(n):
    if n <= 0:
        return
    print("A:", n)
    function_b(n - 1)

def function_b(n):
    if n <= 0:
        return
    print("B:", n)
    function_a(n - 1)

function_a(5)