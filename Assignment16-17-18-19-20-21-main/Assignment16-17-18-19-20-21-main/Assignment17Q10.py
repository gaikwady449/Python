# write a program which accept number from user and return addition of all digit 

num=int(input("enter a number:"))
sum=0
while num > 0:
    digit=num % 10
    sum += digit
    num = num // 10
print("sum of ALL DIGIT:",sum)

