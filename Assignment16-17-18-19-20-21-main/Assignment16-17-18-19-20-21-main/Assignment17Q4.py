# write a program which accept number from user and display factor of that number


n=int(input("Enter a number"))
total=0
for i in range(1,n+1):
    if n % i == 0:
        print(i)
        total +=i
print("addithion of all factoris:",total)