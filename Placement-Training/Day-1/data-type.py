#String
name = input("Enter your name: ")
print("Hello, ", name)
print("Type of name: ", type(name))

#Integer
age = int(input("Enter your age: "))
print("You are", age, "years old")
print("Type of age : ", type(age))

#Float
height = float(input("Enter your height(in meters): "))
print("Your height is ", height, "meters")
print("Type of height: ", type(height))

#Dictionary
person = {"name": "Naveen", "age": 20}
print("Dictionary", person, type(person))

#Set
unique_numbers = {1, 2, 3, 2, 1}
print("Set", unique_numbers, type(unique_numbers))

#Tuple
numbers = (1, 2, 3, 4, 5)
print("Tuple", numbers, type(numbers))