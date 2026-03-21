# Design a python application that create two thread named even or odd
# the even thread should display first 10 even number
# thr odd thread should display first 10 odd number
# both thread should execute independantly using threading module
# Ensure proper thread creation and execcution 

import threading 

def even(Num):
    for i in range(Num):
        if i % 2 ==0:
            print("even:",i)

def odd(Num):
    for i in range(Num):

        if i % 2 != 0:
            print("odd:",i)

if __name__ == "__main__":

   Num =21

   thread1 =threading.Thread(target=even,args=(Num,))
   thread2=threading.Thread(target=odd,args=(Num,))

   thread1.start()
   thread2.start()


   thread1.join()
   thread2.join()




