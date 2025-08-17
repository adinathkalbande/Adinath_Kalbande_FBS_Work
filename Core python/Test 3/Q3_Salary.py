#Write a program to accept basic salary of n emp. (n should be accepted from user).

n = int(input("Enter no of employees = "))

total = 0
all_emp = 0
for i in range (n):
    salary = int(input("Enter basic salary = "))
    if salary <= 20000:
        da = salary*0.1
        ta = salary*0.12
        hra = salary* 0.15
        
    else:
        da = salary*0.15
        ta = salary*0.18
        hra = salary*0.20
        
    total = salary+da+ta+hra
    print(f"Total Salary of employees {i+1}= {total}")
    all_emp += total

print(f"Total of each employees = {all_emp}")

