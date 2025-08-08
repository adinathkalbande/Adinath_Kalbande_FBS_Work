#A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total cost of fencing the field.
cost = 35
l = 50
b = 40
r = 20
pi = 3.14

perimeter = (2*b)+l+(pi*r)
total_cost = perimeter*(cost*5)

print(f"Total cost of fencing field = {total_cost}.")