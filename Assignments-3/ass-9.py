# Prime Numbers in Range: Ask the user for a number N and print all prime numbers up to 
# N using a loop

n = int(input("Enter a number: "))
print("The prime numbers upto", n, "are")

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")