# Design a python application that creat three thread named small,capital and digit
# all thread should accept a string as input 
# the small thread should count and display a number of lowercase charecter
# the capital thread should display a number of capital charecter 
# the digit thread should display a number of numeric digit 
# each thread must also display  1 thread id.thread name
import threading
def chkLower(str):
    print("Thread Name:",threading.current_thread().name)
    print("THread id:",threading.get_ident())
    count= 0 
    for ch in str :
        if ch.islower():
            count +=1
    print("number of lowrecase charector=",count)
    print()

def chkCapital(str):
    print("Thread Name:",threading.current_thread().name)
    print("THread id:",threading.get_ident())
    count= 0 
    for ch in str :
        if ch.isupper():
            count += 1
    print("number of capital charector are=",count)
    print()

def chkdigit(str):
    print("Thread Name:",threading.current_thread().name)
    print("THread id:",threading.get_ident())
    count= 0
    for ch in str :
        if ch.isdigit():
            count+= 1
    print("number of digit is=",count)
    print()

if __name__ == "__main__":

    str=input("Enter a string:")

    t1=threading.Thread(target=chkLower,args=(str,),name="lowercaseThread")
    t2=threading.Thread(target=chkCapital,args=(str,),name="capitalcaseThread")
    t3=threading.Thread(target=chkdigit,args=(str,),name="digitThread")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()






    