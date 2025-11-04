def addition(num1, num2):
    sum = num1+num2
    return sum

def substraction(num1, num2):
    sub = num1-num2
    return sub

def multiplication(num1, num2):
    mul = num1*num2
    return mul

def divide(num1, num2):
    div = num1/num2
    return div

def calculator():
    try:
        if ope == '+':
            print(addition(num1, num2))
        elif ope == '-':
            print(substraction(num1, num2))
        elif ope == '*':
            print(multiplication(num1, num2))
        elif ope == '/':
            print(divide(num1, num2))
        else:
            print('Invalid Operator')
    except ZeroDivisionError as e:
        print(f'Error : {e}')    
try:
    num1 = int(input('Enter First Number : '))
    num2 = int(input('Enter Second Number : '))
    ope = input('Enter Operator : ')
except ValueError as e:
    print(f'Error : {e}')
else:
    calculator()