# Design a python application that create two thread named is evenfactor and odd factor 
# both thread should be accept one intager number  parameter
# the even factor thread should be idntify all evenfactor of given number and addition of all evenfactor
# the odd factor thread should identify all oddfactor of given number and addition of all odd factor
# after both thread complete execution 
import threading
def Evenfactor(num):
    Sum_evenfactor=0
    print("even factor are:")
    for i in range(1,num+1):
        if num % i == 0 and i % 2 ==0:
            print(i)
            Sum_evenfactor += i
      
    print("sum of all evenfactor:",Sum_evenfactor)

def Oddfactor(num):
    sum_oddfactor=0
    print("odd factor are:")
    for i in range(1,num+1):
        if num % i == 0 and i % 2 != 0:
            print(i)
            sum_oddfactor += i
    print("sum of all oddfactor :",sum_oddfactor)

if __name__ == "__main__":

    num=int(input("Enter a number:"))

    Thread1=threading.Thread(target=Evenfactor,args=(num,))
    Thread2=threading.Thread(target=Oddfactor,args=(num,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()
