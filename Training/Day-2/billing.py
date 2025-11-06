# A restaurant  takes multiple orders until the customer types "Done".
#  Use a loop to ask for item prices and calculate the Total Bill

total = 0

while(True):
    price = input("Enter the Item price or Type done to exit: ")
    if(price.lower() == "done"):
        break
    else:
        total += float(price)  #Coverting string to float

print("❤️ The Total Bill is: ", total) #windows + . (for emojis)
