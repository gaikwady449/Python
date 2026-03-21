# write a programm which accept N number from user and store it into list return Minimum number from the list 

N = int(input("Enter a number:"))
lst = []


for i in range(N):
    num=int(input(f"enter a element: { i + 1} "))
    lst.append(num)
    print(lst)
    print(min(lst))