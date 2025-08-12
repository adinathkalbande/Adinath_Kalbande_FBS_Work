#Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.
correct_Id = "admin"
correct_password = 12345
attempts = 0

while (attempts < 3):
    user_id = input("Enter User Id = ")
    password = int(input("Enter Password = "))

    if user_id==correct_Id and password==correct_password:
        print("Login Successfully!")
        break
    else:
        print("Invalid creadintial!")
        attempts+=1

if (attempts==3):
    print("Too many attemts! program terminated.")