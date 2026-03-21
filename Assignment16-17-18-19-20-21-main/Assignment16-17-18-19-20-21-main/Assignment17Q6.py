# write a program which accept a number from user and display velow payyern
#5
# * * * * * 
# * * * *
# * * *
# * *
# *

num=int(input("Enter a number"))


for i in range(num,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()  