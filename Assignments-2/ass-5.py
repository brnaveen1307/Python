# 5. You determine the appropriate coffee size based on the amount of coffee you 
# consume. Write a JAVA / PYTHON program that takes the volume of coffee in 
# milliliters and recommends a coffee size. If the volume is more than 350 ml, 
# recommend a “Large” size; if it’s between 200 ml and 350 ml, recommend a 
# “Medium” size; and if it’s less than 200 ml, recommend a “Small” size. 

volume = int(input("Enter the volume of coffee in milliliters: "))

if volume > 350:
    print("Recommend you to go for a Large size coffee.")
elif volume >= 200 and volume <= 350:
    print("Recommend you to go for a Medium size coffee.")
else:
    print("Recommend you to go for a Small size coffee.")