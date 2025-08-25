#WAP to check if number is palindrone or not using recursion.

def reverse(num, rev=0):
    if num == 0:
        return rev
    else:
        return reverse(num//10, rev*10+(num%10))

def palindrone(num):
    if num == reverse(num):
        print(f"{num} is palindrone.")
    else:
        print(f"{num} is not palindrone.") 
    
num= int(input("ENter number = "))
palindrone(num)