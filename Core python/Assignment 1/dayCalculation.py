#year and weak calculation in given days
days = int(input("Enter days :"))

years = days // 365

days = days % 365

weeks = days // 7

days = days % 7

print(f" In the given days to calculate {years} years, {weeks} week and {days} day")