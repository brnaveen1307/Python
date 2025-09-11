# A user is allowed to enter a ATM PIN maximum for three times. Write a loop to validate 
# the PIN, if the current pin is entered print Access is granted otherwise after entering 
# the wrong pin for 3 times print as blocked

PIN = 1234

for i in range(3):
    pin = int(input("Enter the PIN: "))

    if (pin == PIN):
        print("Access Granted")
        break
else:
    print("Your Card is Blocked!")
