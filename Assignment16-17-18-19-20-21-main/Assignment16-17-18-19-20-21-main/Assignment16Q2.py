# write a program which contain one funtion named is chkNum() which accept one parameter as number if number is even print 
# even number otherwise display ODD


def chkNum(Num):
    if Num % 2 == 0:
        print("even number")
    else:
        print("Odd number")



Num=int(input("enter a number:"))
chkNum(Num)