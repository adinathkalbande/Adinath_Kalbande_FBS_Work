# Create a book with members as bid, bname, price and author, add following methods:
# a. constructor
# b. Destructor
# c. Showbook

class Book:
    def __init__(self, bname, price, author ="Dr. APJ Kalam"):
        self.b = bname
        self.p = price
        self.a = author
    def shoBook(self):
        print("Book Name    =   ", self.b)
        print("Price        =   ", self.p)
        print("Author       =   ", self.a)
    def __del__(self):
        print("Destructor is called.")

b1 = Book('Chhava', 668, 'Shivaji Sawant')
b1.shoBook()
del b1
print('------------------------------------------')
b2 = Book('Fires wings', 1250)
b2.shoBook()
