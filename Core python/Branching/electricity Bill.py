#Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill

unit = int(input("Enter Electricity Unit = "))

if unit <  50:
    charges = 0.50
elif unit > 50 and unit < 100:
    charges = 0.75
elif unit > 150 and unit < 250:
    charges = 1.20
else:
    charges = 1.20

surchur = charges * 0.20
total_bill = unit + surchur

print(f"Total Electricity Bill = {total_bill}")