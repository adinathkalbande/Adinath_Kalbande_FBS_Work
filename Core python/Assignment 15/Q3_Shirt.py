# Create a class Shirt with members as sid, sname, type(format etc), price and size(small, large, etc). Add following methods.
# d. Constructor
# e. Destructor
# f. Show data

class Shirt:
    def __init__(self, sid, sname, type, prize, size):
        self.s = sid
        self.sn = sname
        self.t = type
        self.p = prize
        self.sz = size
    def showData(self):
        print("Shirt Id   =   ", self.s)
        print('Shirt Name =   ', self.sn )
        print('Type       =   ', self.t)
        print('Prize      =   ', self.p)
        print('Size       =   ', self.sz)
    def __del__(self):
        print('Destructor is called.')
p1 = Shirt(111, 'T-Shirt', 'Over Sized', 550, 'Xl')
p1.showData()