class Shirt:
    size = 0
    def __init__(self, sid, sname, type, price, size):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
    @staticmethod
    def calculation(base_price, size):
        if size == 's':
            return base_price
        elif size == 'm':
            return base_price*1.1
        elif size == 'l':
            return base_price*1.2
        elif size == 'xlarge':
            return base_price*1.3
        else:
            return 'This type of shirt is not available...'
        
    def showData(self):
        final_price = Shirt.calculation(self.price, self.size)
        return f'ID : {self.sid}\nNAME : {self.sname}\nTYPE : {self.type}\nPRICE : {self.price}\nSIZE : {self.size}\nFinal Price : {final_price}'
    def destructor(self):
        print('Destructor is called...')
size = input('Enter size : ')
s1 = Shirt('1DFR4', 'Linen', 'Formal', 3000, size)
print(s1.showData())
s1.destructor()
del s1

        



# size = input('Enter size = ')
# s1 = Shirt('12XX4', "Linen", "Formal", 1000, size)