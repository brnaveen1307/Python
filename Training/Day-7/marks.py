marks = {}.fromkeys(['Maths', 'Science', 'English'], 100)

print("Dictionary marks: ", marks)
print("---------------------------------------------")

for i in marks.items():
    print(i)
print("---------------------------------------------")

print("Keys: ", marks.keys())
print("Values: ", marks.values())
print("---------------------------------------------")

print("Sorted: ", sorted(marks))
print("Reverse Sorted: ", sorted(marks, reverse = True))
print("---------------------------------------------")

print("Sorted Items: ", sorted(marks.items()))
print("Reverse Sorted Items: ", sorted(marks.items(), reverse = True))