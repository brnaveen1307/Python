# Question 6: Temperature Cleanup 
# readings = [32, None, 30, 33, 'error', 36, 31, None, 34] 

# Perform: 
# 1. Remove invalid values (None, 'error'). 
# 2. Calculate average of valid readings. 
# 3. Replace missing (None) with average value. 

# Expected Output: 
# Valid_Readings: [32, 30, 33, 36, 31, 34] 
# Average: 32.67 
# Cleaned_Readings: [32, 32.67, 30, 33, 'error', 36, 31, 32.67, 34]

readings = [32, None, 30, 33, 'error', 36, 31, None, 34] 

valid = []
for i in readings:
    if i != None and  i != "error":
        valid.append(i)

avg = round(sum(valid) / len(valid), 2)
print("Valid_Readings: ", valid)

print("Average: ", avg)

cleaned =[]
for i in readings:
    if i == None:
        cleaned.append(avg)
    else:
        cleaned.append(i)

print("Cleaned_Readings: ", cleaned)