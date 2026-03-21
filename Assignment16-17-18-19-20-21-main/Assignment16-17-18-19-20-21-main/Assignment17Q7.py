# write a program which accept a number from user and display velow pattern 
#5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

num=int(input("Enter a number"))


for i in range(num):
    for j in range(1,num + 1):
        print(j,end=" ")
    print()