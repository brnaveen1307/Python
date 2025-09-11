marks = int(input("Enter marks: "))
if marks >= 81 and marks <= 100:
    print("Grade : A")
elif marks >=71 and marks <= 80:
    print("Grade :B")
elif marks >= 61 and marks <= 70:
    print("Grade :C")
elif marks >= 51 and marks <= 60:
    print("Grade :D")
elif marks >=0 and marks <= 50:
    print("Grade :F")
else:
    print("Invalid Input!")
