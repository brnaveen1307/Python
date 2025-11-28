f = open("myfile1.txt", mode="r")

words = f.read().split()
print("Words: ", words)

max_len = max(len(i) for i in words)
print("Maximun Length: ", max_len)

longest_word = [i for i in words if max_len == len(i)]
print("The Longest Word: ", longest_word)


f.close()