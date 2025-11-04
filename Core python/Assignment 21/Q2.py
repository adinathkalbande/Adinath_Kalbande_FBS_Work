class Television:
    def __init__(self, modelNo, screen, price):
        self.model = modelNo
        self.screen = screen
        self.price = price

    def member(self):
        try:
            self.model = int(input('Enter Model No : '))
            if self.model > 9999:
                raise ValueError('Model Number must be 4 digit')
            
            self.screen = int(input('Enter Screen Size : '))
            if self.screen < 12 and self.screen > 70:
                raise ValueError('Screen Number must be greater than 12 or smaller than 70. ')

            self.price = int(input('Enter Screen Size : '))
            if self.price < 0 and self.price > 5000:
                raise ValueError('Price must be less than 5000')
        except ValueError as e:
            print(e)
            print("All values are reset to 0.")

            self.model = 0
            self.screen = 0
            self.price = 0

    def displayData(self):
        print(f'Model Number : {self.model}')
        print(f'Screen Size : {self.screen}')
        print(f'Price : {self.price}')  

def main():
    s1 = Television(0, 0, 0)
    s1.member()
    s1.displayData()

if (__name__ == '__main__'):
    main()
