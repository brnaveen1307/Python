productNames = []

productPrices = []

while True:
    choice = int(input("Choices: 1-Enter the Product Details 2-Exit: "))
    if choice == 1:
        productNames.append(input("Enter the name of the product: "))
        productPrices.append(float(input("Enter the price of the product: ")))
    elif choice == 2:
        break
    else:
        print("Invalid Choice!")

print("---------------Cart Details---------------")

for i in range(len(productNames)):
    print(productNames[i], "---", productPrices[i])

# print("The total cost of all the items in the Cart is ", sum(productPrices))

sum = 0

for i in range(len(productPrices)):
    sum += productPrices[i]
print("The Total Cost of all the items in the Cart is", sum)