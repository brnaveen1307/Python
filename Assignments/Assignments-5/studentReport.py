# Question 3: Student Report 
# You are given: 
# students = [['Alice', 78], ['Bob', 45], ['Charlie', 89], ['David', 56], ['Eve', 91]] 

# Perform: 
# 1. List of students scoring >60. 
# 2. Print the top scorer. 
# 3. Add 5 grace marks to each (max 100). 

# Expected Output: 
# Above_60: ['Alice', 'Charlie', 'Eve'] 
# Topper: Eve 
# Updated_Scores: [['Alice', 83], ['Bob', 50], ['Charlie', 94], ['David', 61], ['Eve', 96]] 

students = [['Alice', 78], ['Bob', 45], ['Charlie', 89], ['David', 56], ['Eve', 91]]

st = []
topper = " "
for i in students:
    if i[1] > 60:
        st.append(i[0])
    if i[1] <= 100:
        i[1] += 5
    

print("Above_60: ", st)

topper = max(students)
print("Topper: ", topper[0])
print("Updated_Scores: ", students)