# 7. You want to check your bank balance before making a purchase. If your balance is 
# below $100, you receive an alert that your funds are low. Otherwise, you’re told that 
# your balance is sufficient.

balance = int(input("Enter your bank balance: "))

if balance < 100:
    print("Alert: Your funds are low!")
else:
    print("Your balance is sufficient.")