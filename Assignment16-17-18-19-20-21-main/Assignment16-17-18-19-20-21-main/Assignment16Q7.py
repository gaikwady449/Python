# write a program which contain one funtion which accept one number from user and return true if it is divisible by 
# 5 otherwise False

def divisible(Num):
    if Num % 5 == 0:
        print("True")
    else:
        print("False")

x=int(input("Enter a number:"))
divisible(x)

