# Write a Python Program to find the largest number in the list without using built in method

numbers = [5, 8, 2, 10, 26, 99, 73, 45]
max = 0

for i in numbers:
    if i > max:
        max = i

    else: 
        continue

print(numbers)
print("The largest number in the above list is: ", max)