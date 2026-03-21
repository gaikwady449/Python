# write a funtion which accept a number from user and display below pattern
# 5     * * * * *
#       * * * * *
#       * * * * *


num=int(input("Enter a number:"))

for i in range(num):
    for j in range(num):
        print("*",end=" ")
    print()
