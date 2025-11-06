# Temperature Logger: Take daily temperature for 7 days and print the average temperature, 
# highest, and lowest.

temps = []

for i in range(1, 8):
    temp = int(input(f"Enter the temperature for day {i}: "))
    temps.append(temp)

# lst = list(set(temps))
# lst.sort()
# print("The highest temperture is", lst[-1])
# print("The lowest temperture is", lst[0])

print("The highest temperture is", max(temps))
print("The lowest temperture is", min(temps))

avg = sum(temps) / len(temps)
print("The average temperature is", avg)   
