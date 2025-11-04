# Create another package “TY” which has a class TYMarks (Theory, Practical).

class Tymarks:
    def __init__(self, theory, practical):
        self.theory = theory
        self.pract = practical

    def showData(self):
        print(f'Theory : {self.theory}')
        print(f'Practical : {self.pract}')