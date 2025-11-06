# Digital Sum: Keep taking digits of a number and sum them until you reach a single 
# digit (ex: 238  → 2+3+8=13 → 1+3=4) 

num = int(input("Enter a number(Multi-digit): "))

while num >= 10:
    sum_digits = 0
    for digit in str(num):
        sum_digits += int(digit)
    num = sum_digits
    
print("Digital sum is: ", num)