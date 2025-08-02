#Write a program to calculate the percentage of student based on marks of any 5 subjects.
s1=int(input("Enter marks of Computer Science :"))
s2=int(input("Enter marks of Physics :"))
s3=int(input("Enter marks of Chemistry :"))
s4=int(input("Enter marks of Marathi :"))
s5=int(input("Enter marks of English :"))

gain_marks=s1+s2+s3+s5+s4

percentage=(gain_marks/500)*100

print(f'Percentage of student based on marks of 5 subjects is {percentage}%')

