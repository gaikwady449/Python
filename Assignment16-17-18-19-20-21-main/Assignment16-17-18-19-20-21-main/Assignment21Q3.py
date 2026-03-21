# Design a python application where multiple thread update a shared variable
# use a lock to avoid race condition 
# Each thread should increment the shared counter multiple times
# Display the final value of counter after all thread complete exicution 

import threading
counter= 0
lock=threading.Lock()

def increment():
    global counter 
    for i in range(5):
        lock.acquire()
        counter += 1
        lock.release()




t1=threading.Thread(target=increment,name="Thread-1")
t2=threading.Thread(target=increment,name="Thread-2")
t3=threading.Thread(target=increment,name="Thread-3")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("final count of counter:",counter)

