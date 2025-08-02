gender = input("Enter Your Gender : ")
age = int(input("Enter Your Age : "))

if ((gender == 'M' and age >= 21) or (gender == 'F' and age >= 18)):
    print("You are eligible for marriage. ")
else:
    print("You are not eligible for marriage. ")

#