str1 = input("Enter the first string: ").lower().replace(" ", "")
str2 = input("Enter the second string: ").lower().replace(" ", "")

if sorted(str1) == sorted(str2):
    print("The strings are Anagrams")
else:
    print("The strings are not Anagrams")

print(sorted(str1))
print(sorted(str2))