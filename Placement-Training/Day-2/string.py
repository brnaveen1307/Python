#String Immutable

text = "hello"
print("Original String: ", text)

try:
    text[0] = "H"
except TypeError as e:
    print("Error: ", e)

new_text = "H" + text[1:]
print("Modified String: ", new_text)