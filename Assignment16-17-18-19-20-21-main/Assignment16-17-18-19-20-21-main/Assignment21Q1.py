# Design a python application that creat two thread named prime and nonprime
# Both thread should accept A list of integers
# the prime thread should display  all prime number  in list
# The numprime thread should dispaly all non prime number in the list 
import threading
def prime(num):
    if num <= 1 :
        return False
    for i in range(2,num):
        if num % i == 0 :
            return False
        return True
    
def Chkprime(lst):
    print("prime number:")
    for num in lst:
        if prime(num):
            print(num,end=" ")
    print()

def Nonprime(lst):
    print("non prime:")

    for num in lst :
        if not prime(num):
            print(num,end=" ")
    print()

lst=list(map(int,input("enter a list of int:").split()))

t1=threading.Thread(target=Chkprime,args=(lst,))
t2=threading.Thread(target=Nonprime,args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()
