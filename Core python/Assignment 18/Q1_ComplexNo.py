# Create a class Complex Number with data members as real and imag and add following methods

class ComplexNo:
    def __init__(self, real, img):
        self.real = real 
        self.img = img

    def __add__(self, other):
        lhs = self.real  + other.real 
        rhs = self.img + other.img
        return f'{lhs} i + {rhs} j'
    
    def destructor(self):
        print('This is destructor...')
    
c1 = ComplexNo(10, 20)
c2 = ComplexNo(40, 50)

# del c2
print(c1 + c2)
c1.destructor()


