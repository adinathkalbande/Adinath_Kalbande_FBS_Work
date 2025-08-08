#Write a program to accept year from user and check if it is a leap year or not.
year = int(input("Enter Year = "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            Print(f"{year} is leap year.")
        else:
            print(f"{year} is not leap year.")
    else:
        print(f"{year} is leap year.")
else:
    print(f"{year} is not leap year.")