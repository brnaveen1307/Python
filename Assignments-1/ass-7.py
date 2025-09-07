# 7. Accept the following inputs from the user and calculate the percentage of class
# attended:
# a. Total number of working days
# b. Total number of days for absent
# After calculating show that if the percentage is less than 75% then student will not
# be able to take the exams.

work_days = int(input("Enter the number of Working Days: "))
absent_days = int(input("Enter the number of Absent Days: "))

percentage = (absent_days / work_days) * 100

if percentage < 75:
    print("You are not eligible to take the exams as your attendance is ", percentage, "%")
else:
    print("You are eligible to take the exams as your attendance is ", percentage, "%")