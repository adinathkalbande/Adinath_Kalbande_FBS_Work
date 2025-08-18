#Write a program to check if entered year is a leap year or not.
def leapYear(year):
    if (year % 400 == 0) or (year % 100 !=0 and year % 4==0):
        return True
    else:
        return False
    
year = int(input('Enter Year = '))
result = leapYear(year)

if result:
    print(f"{year} is leap year.")
else:
    print(f"{year} is not leap")
