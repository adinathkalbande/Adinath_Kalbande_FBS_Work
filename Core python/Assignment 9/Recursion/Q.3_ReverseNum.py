#Write a program to reverse a given number using recursive function.
def reverse_num(num, rev=0):
    if num == 0:
        return rev
    else:
        return reverse_num(num//10, rev*10+num%10)
    
num = int(input("Enter Number want to reverse = "))
res = reverse_num(num)
print(res)