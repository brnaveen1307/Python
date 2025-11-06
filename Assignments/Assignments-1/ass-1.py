# Write a Python program to display "hello" if a number entered by user is multiple of 5, otherwise print "bye"

num = int(input("Enter a number: "))
i = 5

if num % i == 0:
    print("Hello")
else:
    print("Bye")