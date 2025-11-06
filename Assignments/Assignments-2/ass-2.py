# 2. You’re at an amusement park, and you want to know if you can ride a roller coaster. 
# The park requires that riders must be at least 120 cm tall. Write a program that takes 
# your height as input and tells you whether you can ride the roller coaster. 

height = int(input("Enter your height(in cm): "))

if height >= 172:
    print("You are eligible to ride a Roller Coaster.")
else:
    print("You have to be atleast 120 cm tall to ride a Roller Coaster.")