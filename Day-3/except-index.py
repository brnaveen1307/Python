lst = [1, 3, 5, 7]

try:
    print("lst[1] is : ", lst[1])
    print("lst[2] is : ", lst[2])
    print("lst[3] is : ", lst[3])
    print("lst[4] is : ", lst[4])

except IndexError as e:
    print("You are trying to access the index which is out of range.")
    print("e Value: ", e)

