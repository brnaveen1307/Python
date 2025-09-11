# A loan of Rs 10,000 is being repaid in installments of 1k each month. 
# Write a loop to display the balance of the each payment until the loan is cleared

balance = 10000

for i in range(1, 11):
    input = int(input("Enter 1 if you want to pay the loan otherwise 0: "))
    if input == 1:
        print("The balance is Rs ", balance - 1000)
        
    else:
        print("You do not have any loan")