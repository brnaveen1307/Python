#Dispaly the day name using switch/match case

day_num = int(input("Enter the one number(1-7):"))

day = ""

match (day_num):
    case 1:
        day = "Monday"
              
    case 2:
        day = "Tuesday"
    
    case 3:
        day = "Wednesday"
    
    case 4:
        day = "Thursday"
        
    case 5:
        day = "Friday"
        
    case 6:
        day = "Saturday"
        
    case 7:
        day = "Sunday"
        
    case _:
        day = "Invalid program"

print("Today is :", day)