#Convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter feet = "))
inches = int(input("Enter inches ="))

total_inches = (feet * 12) + inches

total_cm = (total_inches * 2.54)

meters = (total_cm) // 100
centimeter = (total_cm) % 100

print(f"Meters = {meters}, Centimeters = {centimeter}")