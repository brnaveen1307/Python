#Catalan Series

def catalan(n):
    if n == 0 or n == 1:
        return 1
    result = 0
    for i in range(n):
        result += catalan(i) * catalan(n - 1 - i)
    return result

terms = int(input("Enter the number of terms: "))
series = [catalan(i) for i in range(terms)]
print("Catalan Series: ", series) 