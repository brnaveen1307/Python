# Marks Entry System: Ask a teacher to enter marks of students until “-1” is entered. 
# Then print the average marks of the class

arr = []
while(True):
    marks = int(input("Enter the Marks or To exit enter -1 : "))
    if marks != -1:
         arr.append(marks)
    else:
         break
    
if len(arr) > 0:
    avg = sum(arr) / len(arr)
    print("The average marks of the class is", avg)
else:
    print("No marks were entered.")