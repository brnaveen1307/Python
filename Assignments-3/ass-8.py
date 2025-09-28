# Bank ATM Cash Dispenser: Simulate dispensing money from an ATM. For a withdrawal 
# amount, use loops to print how many notes of 2000, 500, 200, and 100 are given.

amount = int(input("Enter the amount to be withdrawn: "))

if amount % 100 != 0:
    print("Please enter amount in multiples of 100.")
else:
    notes_2000 = notes_500 = notes_200 = notes_100 = 0
    remaining = amount

    notes_2000 = remaining // 2000
    remaining = remaining % 2000

    notes_500 = remaining // 500
    remaining = remaining % 500
    
    notes_200 = remaining // 200
    remaining = remaining % 200

    notes_100 = remaining // 100
    remaining = remaining % 100

    print("Dispensed notes for ₹", amount)
    print("2000: ", notes_2000)
    print("500: ", notes_500)
    print("200: ", notes_200)
    print("100: ", notes_100)