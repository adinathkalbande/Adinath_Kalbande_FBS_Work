#Write a program to solve the following series :
#N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)

N = int(input("Enter value of N = "))
i = 1
total = 0

while(i <= N):
    total+= N**i
    i+=1

print(f"Total = {total}")


#Using for loop
N = int(input("Enter value of N = "))
total = 0

for i in range (1, N+1):
    total+= N**i
    
print(f"Total = {total}")