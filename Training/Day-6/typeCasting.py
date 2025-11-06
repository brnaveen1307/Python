lst = []

for i in range(1, 6):
    n = int(input("Enter an element: "))
    lst.append(n)

tup = tuple(lst) #TypeCasting
print("Tuple: ", tup)