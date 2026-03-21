# Design a python application that creat two thread 
# Thread1 should calculate and display the maximum element from list
# Thread2 dhould calculate and display the minimum element from list 
# the list should accept from user 
import threading
def find_max(lst):
    print("maximum element is=:", max(lst))

    
def find_min(lst):
    print("minimum element is=:", min(lst))

lst=list(map(int,input("enter a list of int:").split()))

t1=threading.Thread(target=find_max,args=(lst,))
t2=threading.Thread(target=find_min,args=(lst,))

t1.start()
t1.join()

t2.start()
t2.join()
