# 2) Students & Subjects 
# Given: 
# student_subjects = {"Asha": ["Math", "Science"], "Ravi": ["English"], "John": ["Math", 
# "English", "Science"]} 

# Task: Find which student is enrolled in the maximum number of subjects. 
# Approach: Use max() on dictionary keys with key=len on the list of subjects.

student_subjects = {"Asha": ["Math", "Science"], "Ravi": ["English"], "John": ["Math", "English", "Science"]} 

st = max(student_subjects, key=lambda name:len(student_subjects.get(name)))

print(st)