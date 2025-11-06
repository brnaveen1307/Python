# Car Parking Charges: For N cars, input parking hours and calculate charges 
# (Rs 30 per hour), then display total collection 

N = int(input("Enter the number of cars: "))
total_collection = 0
for i in range(N):
    car = int(input("Enter the Car number: "))
    parking_hours = int(input(f"Enter the number of parking hours for Car {car}: "))
    total_collection += parking_hours * 30

print("The total collection is Rs", total_collection)