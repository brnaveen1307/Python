# Using update() function

student = {}

student.update({"Name": "Naveen Msd", "USN": "1VA23CS027", "Email": "naveen@gmail.com", "Mobile": "1234567890"})

print("Student Details: ")
print(student)

student['Marks'] = [90, 95, 99]
print("Updated Student Details: ")
print(student)

student['Address'] = { "City": "Bangalore", "State": "Karnataka", "Pin Code": "560 064"}
print("Updated Student Details: ")
print(student)
