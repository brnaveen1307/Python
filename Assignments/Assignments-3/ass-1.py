# Shopping Cart: Allow the user to add multiple items with prices until they type 'checkout'. Then 
# display the bill with 10% GST 

total = 0

while(True):
    price = input("Enter the Item price or Type checkout to exit: ")
    if(price.lower() == "checkout"):
        break
    else:
        total += float(price)  #Coverting string to float
        gst = total * 0.1
        Total = total + gst

print("💵 The Total Bill is: ", Total) #windows + . (for emojis)