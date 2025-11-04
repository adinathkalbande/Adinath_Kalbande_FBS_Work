
from SY.sy import SYMARKS
from TY.ty import Tymarks

class Student(SYMARKS, Tymarks):
    def __init__(self, rollNo, name, computer, math, ele, theory, pract):
        SYMARKS.__init__(self, computer, math, ele)
        Tymarks.__init__(self, theory, pract)
        self.roll = rollNo
        self.name = name

    def calculateMarks(self):
        computerTotal = self.com + self.theory + self.pract
        Percentage = (computerTotal/300)*100

        if Percentage >= 70:
            grade = 'A'
        elif Percentage >= 60:
            grade = 'B'
        elif Percentage >= 50:
            grade = 'C'
        elif Percentage >= 40:
            grade = 'Pass'
        else:
            grade = 'Fail'

    # def showData(self):
        print(f'Name of Student : {self.name}')
        print(f'Roll No of Student : {self.roll}')
        print('------- SY MARKS ---------')
        self.displayMarks()
        print('------- SY MARKS ---------')
        self.showData()
        print('------- Computer Total ---------')
        print(f'Total Marks  : {computerTotal}')
        print(f'Percentage : {Percentage}')
        print(f'Grade : {grade}')
    
        
def main():
    s1 = Student(101, 'Adinath', 80, 86, 90, 60, 50)
    s1.calculateMarks()
main()