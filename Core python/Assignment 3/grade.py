#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
s1 = int(input("Enter Marks of Marathi = "))
s2 = int(input("Enter Marks of Hindi = "))
s3 = int(input("Enter Marks of History = "))
s4 = int(input("Enter Marks of Social Science = "))
s5 = int(input("Enter Marks of Math = "))

total_marks = s1+s2+s3+s4+s5
grade = (total_marks/500)*100
print(f"Percentage = {grade}")

if grade >=90:
    print("Grade A")
elif grade >=75:
    print("Grade B")
elif grade >= 60:
    print("Grade C")
elif grade>=35:
    print("You Pass!")
else:
    print("Fail!")