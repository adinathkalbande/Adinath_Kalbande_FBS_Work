#check profit or loss

cost_price = int(input("Enter value of cost_price = "))
selling_price = int(input("Enter value of selling price = "))

if selling_price > cost_price:
    print("Wow! You have Profit.")
elif selling_price == cost_price:
    print("Not Profit and Not Loss.")
else:
    print("Aree! You have Loss.")