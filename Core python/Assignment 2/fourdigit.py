#four digit

num = int(input("Enter Four digit number = "))
temp = num

a = temp // 1000
temp = temp % 1000

b = temp // 100
temp = temp % 100

c = temp // 10
temp = temp % 10

d = temp // 1

reversed_num = (d*1000)+(c*100)+(b*10)+a

print(f"Reversed Number = {reversed_num}.")