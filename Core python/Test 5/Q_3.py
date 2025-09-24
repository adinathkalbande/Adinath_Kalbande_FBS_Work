# A list contains sublist with Emp information as follows: 
# Data = [[101, 'Seema', 45000],[340, "Rajani", 13000],[210, "Tannu", 14000], [320, "Suresh", 35000]]
# Write a program to sort the list based on salary.

def sortedList(data):
    for i in range(1,len(data)):
        for j in range(0, len(data)-1):
            if data[j][2] > data[j+1][2]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

data = [[101, 'Seema', 45000],[340, "Rajani", 13000],[210, "Tannu", 14000], [320, "Suresh", 35000]]
res = sortedList(data)
print(res)