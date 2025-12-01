# Question 7: Flight Booking 
# seats = ['A1', 'A2', 'A3', 'A4', 'A5'] 
# booked = ['A1', 'A3'] 

# Print available seats, then assign the first available one to a new passenger. 
# Expected Output: 
# Available: ['A2', 'A4', 'A5'] 
# Booked_After_Assignment: ['A1', 'A3', 'A2'] 

seats = ['A1', 'A2', 'A3', 'A4', 'A5'] 
booked = ['A1', 'A3'] 

available = []
for i in seats:
    if i not in booked:
        available.append(i)

print("Available: ", available)

booked.append(available[0])

print("Booked_After_Assignment: ", booked)