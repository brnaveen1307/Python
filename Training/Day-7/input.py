dict1 = {}

for i in range(1, 6):
    key = int(input("Enter the key: "))
    value = input("Enter the value: ")
    # dict1[key] = value
    dict1.update({key: value})
    print("Updated Dictionary: ", dict1)

