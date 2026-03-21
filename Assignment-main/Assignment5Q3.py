#Write a program which accept one number and check it is perfect or not

num=int(input("Enter a number:"))
sum=0

for i in range(1,num):
    if num % i == 0:
        sum += i
    
if sum== num:
    print(num,"it is a perfect number")
else:
    print(num,"It is not a perfect number")

