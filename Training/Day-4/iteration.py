lst = [2, 3, 4]

print("List: ", lst)

sum = 0
for i in lst:
    print(i)
    sum += 1
avg = sum / len(lst)
print("Sum: ", sum)
print("Avg: ", avg)