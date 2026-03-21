# write a program which accept number from user and check whether that number positive or negative or zero

def Chknum(Num):
    if Num > 0:
        print("positive Number")
    elif Num < 0 :
        print("Negative number")
    else:
        print("zero")

X=int(input("Enter a number:"))
Chknum(X)