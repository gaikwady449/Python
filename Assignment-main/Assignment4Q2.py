#wap a program which accept a num print fact of this num

def Factor(num):
    for i in range(1,num+1):
        if num % i ==0 :
            print(i)

n=int(input("enter a number"))
Factor(n)
     