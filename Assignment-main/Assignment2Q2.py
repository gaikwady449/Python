#write a program whitch accept one number print sum of first N natural number

def sumNatural(No):
    sum=0
    for i in range(1,No+1):
        sum=sum+i
        print("sum Natural number is ",sum)

x=int(input("Enter a number:"))
sumNatural(x)