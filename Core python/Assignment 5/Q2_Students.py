#Enter number of students from user. For those many students accept marks of 5  subject marks from user and calculate percentage. Display all percentage and average percentage of students.
n = int(input("Enter number of students = "))
percentage = []

for i in range (n):
    total = 0
    for j in range (5):
        marks = float(input(f"Enter Marks of subjects {j + 1} for Students {i+1} = "))
        total += marks
    perc = (total/500)*100
    percentage.append(perc)

for i in range (n):
    print(f"Student {i+1} Percentage = {percentage [i]:.2f}%")

avg = sum(percentage)/n
print(f"Average Percentage = {avg:.2f}%")
