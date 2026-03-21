# write a programm which accept N number from user and store it into list return addition of all prime number in the
# list main python file accept n number from user pass it number chekprime() funtion is part of our  user define 
# module named as Marvellous.name of the funtion from main python file should be Listprime()
def Chkprime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i ==0:
            return False
    return True


def listprime(lst):
    total = 0
    for num in lst:
        if Chkprime(num):
            total += num
    return total


N = int(input("Enter a number:"))
lst = []

for i in range(N):
    num=int(input(f"enter a element: { i + 1} "))
    lst.append(num)
print(lst)
result=listprime(lst)
print(result)


        
