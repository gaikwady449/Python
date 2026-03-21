#write a lambda funtion which accept a three number and return largest num in that three

a=int(input("enter 1st number: "))
b=int(input("enter 2st number: "))
c=int(input("enter 1st number: "))

largest= lambda a,b,c: a if a > b and a > c else (b if b > c else c)

print(largest(a,b,c))