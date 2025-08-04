#Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)
import random
user_id = input("Enter User Id = ")
password = input("Enter Password = ")

if user_id == 'admin' and password == '12345':
    captcha_number = random.randint(1111,9999)
    print("Captcha :", captcha_number)
    captcha_input = input("Enter Captcha = ")
    if captcha_input == str(captcha_number):
        print("Login Successfully!")
    else:
        print("Invalid Captcha!")
else:
    ("Invalid user Id or Password")
