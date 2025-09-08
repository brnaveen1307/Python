# 10.  You’re driving and want to avoid a speeding ticket. The speed limit is 60 km/h. If you 
# drive within the speed limit, you’re safe. If you exceed the limit by up to 10 km/h, 
# you get a warning. If you exceed it by more than 10 km/h, you receive a ticket. Write 
# a JAVA / PYTHON program to check the speed and assign a ticket for violating the 
# conditions. 

speed = int(input("Enter your driving speed(in km/h): "))

if speed <= 60:
    print("You are driving within the speed limit. You are safe.")
elif speed <= 70:
    print("Warning: You are exceeding the speed limit. Please slow down.")
else:
    print("You have exceeded the speed limit by more than 10 km/h. Please pay the ticket now.")