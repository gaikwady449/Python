#wap a program which accept a num and print that many number in reverse order

def reverse(num):
    for i in range(num,0,-1):
        print(i,end='')

x=int(input("enter a number:"))
reverse(x)