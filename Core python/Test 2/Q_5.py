#A man goes for shopping. He buys 5 products. Accept the price of all products and display the total bill after adding 18% GST
pro_1 = int(input("Enter price of first product = "))
pro_2 = int(input("Enter price of secong product = "))
pro_3 = int(input("Enter price of third product = "))
pro_4 = int(input("Enter price of fourth product = "))
pro_5 = int(input("ENter price of fourth product = "))

price = pro_1+pro_2+pro_3+pro_4+pro_5
gst = (price * 18)/100
total_price = price+gst

print(f"GST = {gst} and Total Price = {total_price}.")


