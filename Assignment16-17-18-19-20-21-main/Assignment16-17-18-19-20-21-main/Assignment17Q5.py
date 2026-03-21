#write a program which accept from user and check it is prime or not


n = int(input("Enter a number"))

if n <= 1:
    print("it is not a prime number")
else:
    for i in range(2,n):
        if n % i == 0:
            print("it is not a prime number")
            break
    else:
        print("it is a primre number")