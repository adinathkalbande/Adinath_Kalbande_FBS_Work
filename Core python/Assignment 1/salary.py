#Calculate total salary employees according to da(10%), ta (12%) and hra (15)% of basic salary.

salary=int(input("Enter your salary ="))

da = (salary*10)/100        #(salary*0.1)

ta = (salary*12)/100        #(salary*0.12)

hra= (salary*15)/100        #(salary*0.15)

total_salary= salary+da+ta+hra

print(f'Total salary = {total_salary}')