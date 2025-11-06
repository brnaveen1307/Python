# Class Attendance: There are 30 students in a class. Write a program to take attendance 
# ("P" for present, "A" for absent) and count how many are present and absent

present = []
absent = []
for i in range(1, 31):
    at = input("Enter P for Present and A for Absent: ")
    if at.lower() == 'p':
        present.append(i)
    elif at.lower() == 'a':
        absent.append(i)
    else:
        print("NA")

pr = len(present)
ab = len(absent)

print("The number of students present is", pr)
print("The number of students present is", ab)