class Book:
    count = 0
    def __init__(self, bid, bname, price, author='Shivaji Sawant'):
        Book.count +=1
        self.bid = bid
        self.nm = bname
        self.pri = price
        self.author = author
    def showData(self):
        print('Book Id : ', self.bid)
        print('Book Name : ', self.nm)
        print('Price : ', self.pri)
        print('Author : ', self.author)

    def staticMethod():
        print('Count of Books = ', Book.count)

    def destructor(self):
        print('Destructor is called...')

b1 = Book(121, 'Chhawa', 650)
b1.showData()
del b1
print('-------------------------------')

b2 = Book(124, "Fires of wings", 450, 'APJ Abdul Kalam')
b2.showData()
print('-------------------------------')

b3 = Book(155, 'Rich Dad Poor Dad', 250, 'Robert Kiosaki')
b3.showData()
print('-------------------------------')
Book.staticMethod()




