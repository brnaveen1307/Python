# List Comprehension

list1 = [i for i in range(1, 5)]
print("List: ", list1)

list2 = [i for i in range(1, 10) if i % 2 == 0]
print("List of Even Numbers: ", list2)

list3 = [i for i in range(1, 10) if i % 2 != 0]
print("List of Odd Numbers: ", list3)

list4 = [i ** 2 for i in range(1, 5)]
print("List of Squares: ", list4)