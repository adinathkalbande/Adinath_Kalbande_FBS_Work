#Write a program to check if given number is Armstrong number or not. 
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4).

num = int(input("Enter no to check Armstrong number = "))
temp = num
total= 0
digit = len(str(num))

while temp > 0:
    d = temp % 10
    total += d ** digit
    temp //= 10

if num == total:
    print(f"{num} is Armstrong number. ")
else:
    print(f"{num} is not Armstrong number.")