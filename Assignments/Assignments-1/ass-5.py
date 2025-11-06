# 5. Write a python program to accept the cost price of a bike and display the road tax to
# be paid according to following criteria:
# Cost price in Rs , Tax
# >100000 , 15%
# >50000 and <=100000 , 10%
# <=50000 , 5%

cost = int(input("Enter the cost price of the bike: Rs "))

if cost > 100000:
    print("The Road Tax that is to be paid is Rs", cost * 0.15)
elif cost > 50000 and cost <= 100000:
    print("The Road Tax that is to be paid is Rs", cost * 0.10)
else:
    print("The Road Tax that is to be paid is Rs", cost * 0.05)