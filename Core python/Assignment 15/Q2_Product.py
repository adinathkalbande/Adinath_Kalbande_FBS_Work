# Create a class product with members as pid, pname, price and quantity. Add following methods.
# d. Constructor
# e. Destructor
# f. Show data

class Product:
    def __init__(self, pid, pname, price, quantity=24):
        self.p = pid
        self.pn = pname
        self.pr = price
        self.q = quantity
    def showProduct(self):
        print('Product Id   =   ',self.p )
        print('Product Name =   ', self.pn)
        print('Price        =   ', self.pr)
        print('Quantity     =   ', self.q)
    def __del__(self):
        print('Destructor is called.')
p1 = Product('Can-1878', 'Canon Camera', 115000)
p1.showProduct()
del p1
print('------------------------------------------------')
p2 =Product('Apple-1234', 'Iphone 17', 98000)
p2.showProduct()    