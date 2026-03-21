# Disign a python application that create two thread named as evenlist and oddlist 
# Both thread should accept list of integers
# The evenlist should Extract of all even element from list and calculate and display sum 
# The odd list thread Should Extract all odd elemnt from list and caalculate and display sum
# thread should run concurrently  
import threading
def evenlist(num):
    
    even=[n for n in num if n % 2 == 0]
    print("even elements :",even)
    print("sum of all even elemntes:",sum(even))

def oddlist(num):
    odd=[n for n in num if n % 2 != 0]
    print("odd number : ",odd)
    print("sum of all odd number:",sum(odd))


num=list(map(int,input(f"Enter the number:").split()))

t1=threading.Thread(target=evenlist,args=(num,))
t2=threading.Thread(target=oddlist,args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()