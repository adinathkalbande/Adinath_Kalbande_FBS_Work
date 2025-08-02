#Calculate the cost of painting the following building’s walls (both interior and exterior). You need to accept area (one wall) and cost of both interior and exterior wall.
area = int(input("Enter area of walls : "))
int_cost = int(input("Enter Interior cost of walls :"))
ext_cost = int(input("Enter Exterior cost of walls :"))

interior_walls = 8
exterior_walls = 7

interior_cost = interior_walls*area*int_cost
exterior_cost = exterior_walls*area*ext_cost
total_cost = interior_cost + exterior_cost

print(f"Interior cost of painting = {interior_cost}")
print(f"Exterior Cost of painting = {exterior_cost}")
print(f"Total cost of painting = {total_cost} rs. ")

