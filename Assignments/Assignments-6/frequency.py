# 3) Character Frequency 
# Task: Take a string input and create a dictionary of {character: frequency}, ignoring spaces. 
# Approach: Iterate characters, skip spaces, use dict.get or collections.Counter.

str = input("Enter a String: ")
 
freq = {}

for i in str:
    if i == " ":
        continue
    freq[i] = freq.get(i, 0) + 1

print(freq)