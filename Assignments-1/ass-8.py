# 8. A company decided to give bonus to employee according to following criteria:
# Time period of service , Bonus
# More than 10 Years , 10%
# >=6 and <=10 Years , 8%
# Less than 6 years , 5%
# Ask user for their salary and years of service and print the bonus amount.

salary = int(input("Enter the Salary: Rs "))
year = int(input("Enter the Number of Years of Service: "))

if year > 10:
    print("The Bonus for the Employee is Rs", salary * 0.10)
elif year >= 6 and year <= 10:
    print("The Bonus for the Employee is Rs", salary * 0.08)
else:
    print("The Bonus for the Employee is Rs", salary * 0.05)