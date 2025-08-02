#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amount = int(input("Enter amount = "))

temp = amount

two_thou = temp // 2000
temp = temp % 2000

five_hund = temp // 500
temp = temp % 500

two_hund = temp // 200
temp = temp % 200

one_hund = temp // 100
temp = temp % 100

fifty = temp // 50
temp = temp % 50

twenty = temp // 20
temp = temp % 20

ten = temp // 10
temp = temp % 10

total_notes = two_thou+five_hund+two_hund+one_hund+fifty+twenty+ten

print(f"Total notes = {total_notes}")