#write a program which accept  one number and print factorial of that numbers

def factorial(No):
    fact=1
    for i in range(1,No + 1):
        fact=fact*i
        print("fatorial of number", No,"is",fact)

x=int(input("Enter a number:"))
factorial(x)