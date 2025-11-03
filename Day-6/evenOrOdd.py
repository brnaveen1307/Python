tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Tuple: ", tup)

even = []
even_count = 0
odd = []
odd_count = 0

for i in tup:
    if i % 2 == 0:
        even.append(i)
        even_count += 1
    else:
        odd.append(i)
        odd_count += 1

print("List of Odd Numbers: ", odd)
print("The count of Odd Numbers: ", odd_count)
print("List of Even Numbers: ", even)
print("The count of Even Numbers: ", even_count)