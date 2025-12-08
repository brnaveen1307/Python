# 5) Student Marks to Grades 
# Given: 
# marks = {"Asha": 85, "Ravi": 55, "John": 72, "Anu": 91} 

# Task: Convert marks to grades using boundaries and produce new dict name -> grade. 
# Approach: Iterate and map using if/elif conditions

marks = {"Asha": 85, "Ravi": 55, "John": 72, "Anu": 91} 

grades = {}

for name, score in marks.items():
    if score >= 90:
        grades[name] = "A"
    elif score >= 75:
        grades[name] = "B"
    elif score >= 50:
        grades[name] = "C"
    else:
        grades[name] = "D"

print(grades)