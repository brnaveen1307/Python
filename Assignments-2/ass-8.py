# 8. You need to determine the cost of renting a car based on the number of days rented: 
# For up to 3 days, the rate is $50 per day. 
# For 4 to 7 days, the rate is $40 per day for days 4 through 7. 
# For rentals longer than 7 days, the rate is $30 per day for the days beyond 7, with 
# previous rates still applicable. 
# Write a program to calculate the total rental cost. 

days = int(input("Enter the number of days you want to rent the car: "))

if days <= 3:
    print("The total rental cost is $", days * 50)
elif days >=4 and days <= 7:
    print("The total rental cost is $", (3 * 50) + ((days -3) * 40))
else:
    print('The totla rental cost is $', (3 * 50) + (4 * 40) + ((days- 7) * 30))