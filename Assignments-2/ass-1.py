# 1. Write a program that takes the current temperature as input and suggests the 
# appropriate clothing. If the temperature is above 25°C, recommend wearing a shirt; 
# otherwise, recommend wearing a jacket. 

temp = int(input("Enter the Current Temperature(in Degrees): "))

if temp > 25:
    print("Recommend you to wear a shirt made up of cotton maybe.")
else:
    print("Recommend you to wear a jacket as it is freezing.")