# create a package “SY” which has class SYMARKS (Computer Total, MathsTotal, ElectronicsTotal).
class SYMARKS:
    def __init__(self, computer, math, ele):
        self.com = computer
        self.math = math
        self.ele = ele

    def displayMarks(self):
        print(f'Computer Total :{self.com}')
        print(f'Math Total :{self.math}')
        print(f'Electronics Total :{self.ele}')