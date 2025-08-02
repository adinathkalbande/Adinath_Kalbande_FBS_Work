#WAP to calculate selling price of book based on cost price and discount.

cost_price = int(input("Enter cost price = "))
discount = int(input("Enter discount ="))

total_discount = (cost_price * discount) / 100

selling_price = cost_price + total_discount

print(f"Selling Price = {selling_price}")