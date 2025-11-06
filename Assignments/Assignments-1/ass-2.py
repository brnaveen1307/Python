#Write a Python program to check whether a person is eligible to vote or not

name = input("Enter the name of the person: ")
age = int(input("Enter the age: "))

if age >= 18:
    print(name, "is eligible to vote as his age is ", age)
else:
    print(name, "is not eligible to vote as his age is ", age)