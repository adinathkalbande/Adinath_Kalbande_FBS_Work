#Write a program to check if given number is Armstrong or not using recursive function.
def armstrong(num, digits):
    if num == 0:
        return 0
    else:
        last = num % 10
        return (last**digits)+armstrong(num//10, digits)

def check_armstrong(num):
    digits = len(str(num))
    if num == armstrong(num, digits):
        print(f'{num} is armstrong number.')
    else:
        print(f'{num} is not armstrong number.')

num = int(input("Enter number = "))
check_armstrong(num)
