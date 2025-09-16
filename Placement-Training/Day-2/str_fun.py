#String Function

str1 = "Captain"
str2 = "America"

#Concatenation
combined = str1 + " " + str2
print("Concatenation: ", combined)

#Replace
replaced = combined.replace("America", "Shield")
print("After Replace: ", replaced)

#Length
length = len(replaced)
print("Length of string: ", length)

#Repetition
repeated = str1 * 3
print("Repetition: ", repeated)

#Slicing
slice_part = replaced[0 : 7]
print("Sliced Part: ", slice_part)

#Indexing
first_char = replaced[0]
last_char = replaced[-1]
print("First Character: ", first_char)
print("Last Character: ", last_char)

