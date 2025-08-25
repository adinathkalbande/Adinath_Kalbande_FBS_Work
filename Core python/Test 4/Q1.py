#Write a function to which we pass a parameter and print the factors of a given number.
def factors(num):
    for i in range (1, num+1):
        if num % i == 0:
            print(i, end=" ")
            
num = int(input("Enter number = "))
factors(num)
 
        