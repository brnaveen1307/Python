# Question 9: Exam Evaluation 
# answers = ['A', 'C', 'B', 'D', 'A', 'C'] 
# student = ['A', 'B', 'B', 'D', 'A', 'C'] 

# Print: 
# 1. Correct count. 
# 2. Percentage score. 
# 3. Indices of incorrect answers. 

# Expected Output: 
# Correct: 5 
# Percentage: 83.33 
# Incorrect_Indexes: [1]

answers = ['A', 'C', 'B', 'D', 'A', 'C'] 
student = ['A', 'B', 'B', 'D', 'A', 'C']

correct = 0
incorrect = []
for i in range (len(student)):
    if student[i] == answers[i]:
        correct += 1
    else:
        incorrect.append(i) 
print("Correct: ", correct)

per = (correct / len(answers)) * 100

print("Percentage: ", per)
print("Inorrect_Indexes : ", incorrect)