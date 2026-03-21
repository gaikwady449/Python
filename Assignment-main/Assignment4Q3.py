# write a program which accept two number and print addition,substraction sivision and multiplication of num

def  operation(a,b):
    add=a+b
    sub=a-b
    div=a%b
    mul=a*b
    print(add,sub,div,mul)
x=int(input("enter a 1st number"))
y=int(input("enter a 2nd number"))
operation(x,y)
