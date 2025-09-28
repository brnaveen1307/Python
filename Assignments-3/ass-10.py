# Bus Reservation: A bus has 30 seats. Keep asking passengers to book until all seats 
# are filled. Show 'House Full' when seats run out.

seats = 30
while seats > 0:
    print("Seats Available: ", seats)
    name = input("Enter passenger name to book a seat: ")
    print("Seat booked successfully for", name)
    seats -= 1

print("House Full! No more seats available")
