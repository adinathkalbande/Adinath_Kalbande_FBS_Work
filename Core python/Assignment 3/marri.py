#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
gender = input("Enter Your Gender (Mele/Female) : ")
age = int(input("Enter Your Age = "))

if gender == 'male' and age >= 21:
    print("You are eligible for Marry.")
elif gender == 'female' and age >= 18:
    print("You are eligible for Marry.")
else: print("You are not eligible for Marry.")