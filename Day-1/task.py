#upto 10 km fixed charge is 80 rupees
#11-20 km - fixed charges + 6rs per km
#21-30 km - fixed charges + 5rs per km
#31-40 km - fixed charges + 4rs per km

km = int(input("Enter the number of Kilometers travelled: "))
fixedCharges = 80

if km <= 10:
    print("The cost of travel is : Rs", 80)
elif km >= 11 and km <= 20:
    print("The cost of travel is : Rs", fixedCharges + ((km - 10) * 6))
elif km >= 21 and km <= 30:
    print("The cost of travel is : Rs", fixedCharges + ((km - 10) * 5))
elif km >= 31 and km <= 40:
    print("The cost of travel is : Rs", fixedCharges + ((km - 10) * 4))
elif km > 40:
    print("The cost of travel is : Rs", fixedCharges + ((km - 10) * 3))
else:
    print("Invalid Input!")