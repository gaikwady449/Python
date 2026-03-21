def chkDivisible(No):

    if No % 3 == 0 and No % 5 == 0 :
        print("no is divisible by 3 and 5")
    else:
        print("no is not divisible by 3 and 5")

x=int(input("Enter a number:"))
chkDivisible(x)