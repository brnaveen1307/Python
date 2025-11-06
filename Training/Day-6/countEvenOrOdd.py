tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Tuple: ", tup)

even = 0
odd = 0

for i in tup:
    if i % 2 == 0:
        even += 1
    else: 
        odd += 1

print("The number of even numbers in Tuple: ", even)
print("The number of odd numbers in Tuple: ", odd)