###percentage of best of five subject
marathi=int(input("Enter marks of subject Marathi :"))
hindi=int(input("Enter marks of subject Hindi :"))
history=int(input("Enter marks of subject History :"))
math=int(input("Enter marks of subject Mathematics :"))
science=int(input("Enter marks of subject Science :"))

gain_marks=marathi+hindi+history+marathi+science

percentage=(gain_marks/500)*100

print(f"Percentage is {percentage}%")
