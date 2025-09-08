# 6. You’re shopping at a store that offers a discount if you spend $50 or more. Write a 
# JAVA / PYTHON program to check if the user is eligible for the discount based on their 
# total purchase amount. 

amount = int(input("Enter your total purchase amount: "))

if amount >= 50:
    print("You are eligible for a discount on your purchase.")
else:
    print("You need to spend at least $50 to be eligible for a discount.")