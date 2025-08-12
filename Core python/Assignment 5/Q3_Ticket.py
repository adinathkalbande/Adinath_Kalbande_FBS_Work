#Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#. Senior citizen (above 59) = 50% discount
#c. Others need to pay full

n = int(input("Enter Number of Passengers = "))
cost = int(input("Enter Ticket cost = "))

total_amount = 0

for i in range (n):
    age = int(input("Enter age of passenger = "))

    if age < 12:
        discount = cost*0.7
    elif age > 59:
        discount = cost*0.5
    else:
        discount = cost
    total_amount+= discount

print(f"Total ammount of all passengers = {total_amount} Rs.")