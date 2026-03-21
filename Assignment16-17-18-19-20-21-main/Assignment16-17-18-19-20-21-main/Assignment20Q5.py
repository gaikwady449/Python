# Design a python application that create two thread named thread1 and thread2
# Thread 1 should display number from 1 to 50 
# Thread 2 should display number from 50 to 1 in reverse order 
# Ensure that  thread 2 startexicution after a thread 1 is complet

import threading

def number(num):
    for i in range(1,num):
        print(i)

def revrse(num):
    for i in range(num,0,-1):
      print(i)

if __name__ == "__main__":

  num=int(input("Enter a number:"))

  t1=threading.Thread(target=number,args=(num,))
  t2=threading.Thread(target=revrse,args=(num,))

  t1.start()
  t1.join()

  t2.start()
  t2.join()