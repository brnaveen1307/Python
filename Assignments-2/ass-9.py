# 9. You need to calculate the utility bill based on the total number of units consumed: 
# For up to 100 units, the charge is $0.50 per unit. For units between 101 and 200, the 
# rate is $0.75 per unit for the units beyond the first 100. For units exceeding 200, the 
# cost is $1.00 per unit for units above 200, while the previous rates still apply. 
# Write a program to compute the total utility bill based on these rates. 

units = float(input("Enter the total number of units consumed: "))

if units <= 100:
    print("The total utility bill is $", units * 0.50)
elif units >= 101 and units <= 200:
    print("The total utillity bill is $", (100 * 0.50) + ((units - 100) * 0.75))
else:
    print("The total utility bill is $", (100 * 0.50) + (100 * 0.75) + ((units - 200) * 1.00))