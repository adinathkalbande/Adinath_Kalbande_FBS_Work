#Write a program to accept 3 digit number. If first digit is double of second digit and half of 
# third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
# Eg : - 428 , 214 etc.

num = int(input("Enter three digit number = "))
temp = num

d1 = temp//100
temp = temp% 100

d2 = temp//10
temp = temp%10

d3 = temp

if (d1==d2*2) and (d1==d3/2):
    print("Yes")
else:
    print("Please try next time!")

