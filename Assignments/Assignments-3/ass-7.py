# Word Vowel Counter: Take a word from the user and use a loop to count how many vowels 
# it has. 

vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Enter a word to check vowels in it: ")

count = 0
for char in word:
    if char.lower() in vowels:
        count += 1
print("The number of vowels in the word", word, "is", count)