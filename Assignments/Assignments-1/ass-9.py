# 9. Accept the age, gender (‘M’,’F’), number of days and display the wages accordingly.
# Age , Gender , Wages per day
# >=18 and <30 , M , 700,  F , 750
# >=30 and <=40 , M , 800 , F , 850

age = int(input("Enter the Age: "))
gender = input("Enter the Gender(M, F): ")
days = int(input("Enter the Number of Days: "))

if age >=18 and age < 30:
    if gender == 'M':
        print("The Wages of the Male is Rs ", days * 700)
    elif gender == 'F':
        print("The Wages of the Female is Rs ", days * 750)
    else:
        print("Invalid Gender")
elif age >= 30 and age <= 40:
    if gender == 'M':
        print("The Wages for the Male is Rs ", days * 800)
    elif gender == 'F':
        print("The Wages for the Female is Rs ", days * 850)
    else:
        print("Invalid Gender")
else:
    print("Invalid input!")