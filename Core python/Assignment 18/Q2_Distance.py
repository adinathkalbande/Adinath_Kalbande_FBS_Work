# Create a class Distance with data members as km,m and cm and add following methods :
class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __add__(self, other):
        cm = self.cm + other.cm
        m = cm // 100
        cm = cm % 100

        m = self.m + other.m+m
        km = m // 1000
        m = m % 1000

        km = self.km + other.km+km
        return f'{km} Km, {m} M, {self.cm} Cm'
    
d1 = Distance(10, 500, 100)
d2 = Distance(20, 700, 100)
print(d1 + d2)