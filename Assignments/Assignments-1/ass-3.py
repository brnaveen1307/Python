# 3. Write a program to calculate the electricity bill (accept number of units from user)
# according to the following criteria:
# a. Read customer name and customer ID.
# b. Print customer name and customer ID.
# c. Print electricity bill.
# Unit , First 100 units, No charge
# Next 100 units , Rs 5 per unit
# After 200 units , Rs 10 per unit
# Example: if unit is 350 then total bill amount is Rs 2500

cname = input("Enter the Customer Name: ")
cid = int(input("Enter the Customer ID: "))
units = int(input("Enter the Number of Units: "))

print("\n************************************************\n")

print("Customer Name: ", cname)
print("Customer ID: " , cid)
print("Number of Units: ", units)

if units <= 100:
    print("The electricity bill is Rs 0 as it is free of cost")
elif units <= 200:
    print("The electricity bill is Rs", (units - 100) * 5)
else:
    print("The electricity bill is Rs", (units -100) * 10)