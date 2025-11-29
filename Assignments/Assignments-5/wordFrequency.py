# Question 5: Word Frequency 
# sentence = "the quick brown fox jumps over the lazy dog the fox was fast" 

# Print word frequencies (as list of tuples), sorted by highest frequency then 
# alphabetically. 

# Expected Output: 
# [('the', 3), ('fox', 2), ('brown', 1), ('dog', 1), ('fast', 1), ('jumps', 1), ('lazy', 1), ('over', 
# 1), ('quick', 1), ('was', 1)]

sentence = "the quick brown fox jumps over the lazy dog the fox was fast"

words = sentence.split(" ")

frequency = {}
for i in words:
    frequency[i] = frequency.get(i, 0) + 1

result = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

print(result)