#Write a program to calculate the total cost of painting. The interior of building with four equal sized walls.
cost = int(input("Enter cost of painting for one wall = "))
area = int(input("Enter area of walls = "))

interior_wall = 4

total_cost = 4*cost*area

print(f"Total cost of painting for wall is = {total_cost}")