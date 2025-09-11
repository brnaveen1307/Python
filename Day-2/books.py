#Take input the number of days being late to return the books and calculate the fine per book
# for 1 day as Rs 1 and finally Calculate the total fine for all the books

fine = 0
for i in range(1, 5):
    days = int(input(f"Enter the number of days being late to return book {i} : "))
    totalFine = 1 * days
    print("The fine for book ", i, "is Rs", totalFine)
    fine += totalFine
print("The total fine for all the books: ", fine, " Rs")