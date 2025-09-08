# 4. You’re using a fitness app that rewards you if you log more than 1000 steps in a day. 
# Write a program in JAVA / PYTHON that takes the number of steps logged as input 
# and tells you if you’ve earned a reward. 

steps = int(input("Enter the number of steps logged: "))

if steps > 1000:
    print("Congratulations! You have earned a reward for logging more than 1000 steps today.")
else:
    print("Keep going! You need to log more than 1000 steps to earn a reward.")