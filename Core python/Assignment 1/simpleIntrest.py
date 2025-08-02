#Write a program to enter P, T, R and calculate simple Interest.
p=int(input("Enter value of principle amount :"))
t=int(input("Enter value of Tax :"))
r=int(input("Enter value of Time :"))

si=(p*t*r)/100

print(f"Simple intrest = {si}")