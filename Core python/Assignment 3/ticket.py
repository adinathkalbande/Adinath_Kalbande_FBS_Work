#Accept age of five people and also per person ticket amount and then calculate totalamount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

per1 = int(input("Enter age of First Person = "))
per2 = int(input("Enter age of Second Person = "))
per3 = int(input("Enter age of Third Person = "))
per4 = int(input("Enter age of Fourth Person = "))
per5 = int(input("Enter age of Fifth Person = "))

ticket_price = int(input("Enter price of ticket = "))

if per1 < 12:
    discount = ticket_price*0.3
    ticket_amt_1 = ticket_price - discount
elif per1 > 59:
    discount = ticket_price*0.5
    ticket_amt_1 = ticket_price - discount
else:
    ticket_amt_1 = ticket_price
    
if per2 < 12:
    discount = ticket_price*0.3
    ticket_amt_2 = ticket_price - discount
elif per2 > 59:
    discount = ticket_price*0.5
    ticket_amt_2 = ticket_price - discount
else: 
    ticket_amt_2 = ticket_price

if per3 < 12:
    discount = ticket_price*0.3
    ticket_amt_3 = ticket_price - discount
elif per3 > 59:
    discount = ticket_price*0.5
    ticket_amt_3 = ticket_price - discount
else: 
    ticket_amt_3 = ticket_price

if per4 < 12:
    discount = ticket_price*0.3
    ticket_amt_4 = ticket_price - discount
elif per4 > 59:
    discount = ticket_price*0.5
    ticket_amt_4 = ticket_price - discount
else: 
    ticket_amt_4 = ticket_price

if per5 < 12:
    discount = ticket_price*0.3
    ticket_amt_5 = ticket_price - discount
elif per5 > 59:
    discount = ticket_price*0.5
    ticket_amt_5 = ticket_price - discount
else: 
    ticket_amt_5 = ticket_price

total_ticket = ticket_amt_1+ticket_amt_2+ticket_amt_3+ticket_amt_4+ticket_amt_5

print(f"Total ticket of Five person is {total_ticket} Rs.")


    
