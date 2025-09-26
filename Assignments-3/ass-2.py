# Train Seat Allocation: A train coach has 72 seats. Write a program that marks every 8th seat as a 
# 'Window Seat' and prints which seats are window seats.

window_seats = []

for i in range(1, 73):
    if i % 8 == 0:
        window_seats.append(i)

print(window_seats)