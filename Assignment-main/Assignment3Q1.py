# write a program which accept one numbers and check it is prime or not 

def Chkprime(N):
    if N <= 1:
        return False
    for i in range(2,int(N**0.5)+1):
        if N % i ==0:
            return False
    return True

x=int(input("Enter a number:"))
if Chkprime(x):
    print("prime number")
else:
    print("Not a prime number")