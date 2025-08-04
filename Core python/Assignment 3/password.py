#Write a program to check if user has entered correct userid and password.
user_id = input("Enter User Id = ")
password = input("Enter Password = ")

if user_id == 'admin123' and password == '12345':
    print ("Correct! User Id and Password.")
elif user_id != 'admin123' and password == '12345':
    print("Invalid User Id.")
elif user_id == 'admin123' and password != '12345':
    print("Invalid Password!")
else:
    print("Invalid User Id and Password!")

