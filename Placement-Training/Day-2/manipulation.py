# String Manipulation

text = "captain"
print("Original: ", text)
print("Length of the String: ", len(text))

# String  Manipulation 
text = "Captain"
print("Length of the string:", len(text))

# Case Conversion
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())
print("Capitalize", text.capitalize())
print("SuperCase:", text.swapcase())

# Whitspace Handling
print("Stripped:", text.strip())
print("Leftstrip:", text.lstrip())
print("Rightstrip:", text.rstrip())

# Serach Count
print("Count of 'e':", text.count('e'))
print("Find 'Iron':", text.find('Iron'))
print("Index of 'Captain':", text.index('Captain'))
 
# Replace and Split
replaced = "Iron Man"
print("Replace 'Iron Man' with 'Captain America':", text.replace('Iron Man'))
print("Split by space: ", text.split())
