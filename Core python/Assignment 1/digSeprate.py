#Digit Separate
num=int(input("Enter four digit number :"))
temp=num

di=temp%10
temp=temp//10

d2=temp%10
temp=temp//10

d3=temp%10
temp=temp//10

d4=temp%10
temp=temp//10

print(f"Separate of four digit number = Di : {di}, D2 : {d2}, D3 : {d3}, D4 : {d4} ")


