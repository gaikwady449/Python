#write a program which accept a number from user and display its factorial

n = int(input("enter a number:"))
fact = 1

for i in range(1 , n + 1):
    fact = fact*i

print(fact)