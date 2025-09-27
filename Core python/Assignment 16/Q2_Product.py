class Product:
    discount = 0
    def __init__(self, pid, pname, price, quan):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quan
    def showdata(self):
        print("Product Id = ", self.pid)
        print("Product Name = ", self.pname)
        print("Price = ", self.price)
        print("Quantity = ", self.quantity)
    def total_discount(self):
        total_price = self.price * self.quantity
        total_discount = (Product.discount/100)*total_price
        final_price = total_price - total_discount
        return final_price
    def destructor(self):
        print("Destructur called...")

Product.discount = int(input('Enter discount = '))
p1 = Product(1189, 'Mouse', 500, 2)
p1.showdata()
print(p1.total_discount())
p1.destructor()
    
        