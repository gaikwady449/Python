#Create on module named as arithmetic which contains 4 function as add( ) for addition sub( ) for substraction mul( )
# for multiplication div( ) for division. All Function accept two parameters as number and perform the operation 
# write on python which call all the functions from arithmetic module by accepting the parameters from user


def Add(a,b):
    return a + b
def sub(a,b):
    return a - b
def Mul(a,b):
    return a*b
def div(a,b):
    return a / b



num1=int(input("Entera 1st number: "))
num2=int(input("enter 2nd number:"))

print(Add(num1,num2))
print(sub(num1,num2))
print(Mul(num1,num2))
print(div(num1,num2))