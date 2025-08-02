#Calculate numbers of notes in given amount
amount=int(input("Enter amount = "))
temp=amount
two_thousand=temp//2000
temp=temp%2000

five_hundred=temp//500
temp=temp%500

two_hundrad=temp//200
temp=temp%200

one_hundred=temp//100
temp=temp%100

fifty=temp//50
temp=temp%50

twenty=temp//20
temp=temp%20

ten=temp//10
temp=temp%10

total_notes=two_thousand+five_hundred+two_hundrad+one_hundred+fifty+twenty+ten

print(f"Total notes = {total_notes}")

